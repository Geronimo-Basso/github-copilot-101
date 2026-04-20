# Lab 03 — GitHub Copilot Agent Mode

Drive **GitHub Copilot's** built-in agent through a real multi-file change with terminal access and tests, choose the right **Permission level** for the risk at hand, ship **a small toolbox of custom agents** (a planner, a reviewer, and a test author) to see different patterns in action, and extend the agent with a **Model Context Protocol (MCP)** server you build yourself.

## Table of Contents

- [What You'll Learn](#what-youll-learn)
- [Pre-Lab Setup](#pre-lab-setup)
- [Part 1 — Theory](#part-1--theory)
  - [1.1 The agent loop](#11-the-agent-loop)
  - [1.2 Permission levels](#12-permission-levels)
  - [1.3 Custom agents](#13-custom-agents)
  - [1.4 Model Context Protocol (MCP)](#14-model-context-protocol-mcp)
- [Part 2 — Hands-on](#part-2--hands-on)
  - [Exercise A — Agent loop in practice](#exercise-a--agent-loop-in-practice)
  - [Exercise B — Permission levels (read-through)](#exercise-b--permission-levels-read-through)
  - [Exercise C — Build a custom-agent toolbox](#exercise-c--build-a-custom-agent-toolbox)
    - [C.1 — Plan-first scaffolder with handoff](#c1--plan-first-scaffolder-with-handoff)
    - [C.2 — Read-only code reviewer](#c2--read-only-code-reviewer)
    - [C.3 — Scope-locked test author](#c3--scope-locked-test-author)
  - [Exercise D — Consume + create an MCP server](#exercise-d--consume--create-an-mcp-server)
    - [D.1 — Consume the filesystem MCP server (OPTIONAL)](#d1--consume-the-filesystem-mcp-server-optional)
    - [D.2 — Build your own MCP server (REQUIRED)](#d2--build-your-own-mcp-server-required)
    - [D.3 — Use an off-the-shelf MCP from a registry (Microsoft Learn MCP) (OPTIONAL)](#d3--use-an-off-the-shelf-mcp-from-a-registry-microsoft-learn-mcp-optional)
    - [D.4 — Browser automation with the Playwright MCP (OPTIONAL)](#d4--browser-automation-with-the-playwright-mcp-optional)

## What You'll Learn

By the end of this lab you will be able to:

- **Drive Agent through the full loop** — plan → edit → run → observe → iterate — across multiple files with terminal and tests.
- **Pick the right Permission level** (Default Approvals, Bypass Approvals, Autopilot Preview) for the risk in front of you, knowing exactly what each one trades away.
- **Author workspace-scoped custom agents** at `.github/agents/<name>.agent.md` demonstrating three patterns: **handoffs** (planner → executor), **least-privilege** (read-only reviewer), and **scope-locking** (test-only author).
- **Consume** an existing MCP server in VS Code and **author your own** ~30-line `FastMCP` server in Python that exposes data the model cannot otherwise see.

---

## Pre-Lab Setup

Get the boring stuff out of the way before the clock starts.

### Required ✅

1. **Clone or open this repository in VS Code**, with the **GitHub Copilot** and **Python** extensions installed and enabled.

2. **Create and activate a virtual environment at the workspace root.** The MCP server you'll build later expects to be launched from `.venv`:

   ```bash
   python3 -m venv .venv                # macOS / Linux
   # python -m venv .venv               # Windows  (or: py -3 -m venv .venv)
   source .venv/bin/activate            # macOS / Linux
   # .venv\Scripts\activate             # Windows
   ```

3. **Install the lab dependencies** (this includes `mcp[cli]>=1.0` and `pytest`, both new in this lab):

   ```bash
   pip install -r agents/requirements.txt
   ```

4. **Run the app to confirm it boots.** From the workspace root, start the FastAPI server and open the frontend:

   ```bash
   # Start the API (leave running in its own terminal)
   uvicorn agents.backend.app:app --reload --port 8000

   # In a second terminal, sanity-check the API
   curl http://127.0.0.1:8000/activities
   ```

   Then open `agents/frontend/index.html` in your browser (or right-click → **Open with Live Server** in VS Code) — it talks to the API on `127.0.0.1:8000`. Stop the server with `Ctrl+C` when you're done; you can restart it any time with the same `uvicorn` command.

5. **Confirm Agent Mode is available.** Open Copilot Chat, click the chat input's mode picker, and check that **Agent** is in the list. If it isn't, your org admin has disabled `chat.agent.enabled` — fix that before continuing.

6. **Confirm `chat.mcp.discovery.enabled` is on.** The repo ships a `.vscode/settings.json` that already sets this. If you opened the workspace and accepted the workspace-trust prompt, you're good.

### Optional 🌱

7. **Check for Node.js** (only needed for the optional consume half of [Exercise D](#exercise-d--consume--create-an-mcp-server)):

   ```bash
   node --version
   ```


> ✅ **You should now see:** an active `.venv`, `pip list` showing `mcp`, `pytest`, `fastapi`, and either a Node version string or "command not found" (both are fine).

---

## Part 1 — Theory

Read straight through Part 1 before touching the keyboard. Every exercise in Part 2 assumes the vocabulary below.

### 1.1 The agent loop

Agent mode isn't a one-shot autocomplete. It runs a **loop**:

```
plan → edit → run → observe → iterate
  ↑                              │
  └──────── self-correct ────────┘
```

Each turn the agent decides what to do next based on what it just observed (a failing test, a missing file, a stack trace). You see the loop happen live in the chat panel: tool calls render inline, edits show up in the diff overlay (accept/reject per file), and a **Stop** button is always one click away. The loop ends when the model decides it's done — or when you stop it.

The two skills that matter:

- **Reading the loop.** Watch the inline tool calls. If the agent is in a "running tests → reading output → editing" rhythm, you're fine. If it's editing the same file 5 times in a row without running anything, *stop it*.
- **Steering with prompts.** A vague prompt produces a vague loop. A **plan-first** prompt ("first, show me your plan and wait for me to confirm") gives you a checkpoint before any code is touched.

### 1.2 Permission levels

Permission levels control how much the agent can do **without asking you**. There are three:

| Level | Behavior | Trade-off |
| --- | --- | --- |
| **Default Approvals** | Confirmation dialog for every "risky" tool call (run command, edit file, MCP tool, etc.). | Safe but noisy. Approval fatigue is real on long tasks. |
| **Bypass Approvals** | All tool calls auto-approved. Agent auto-retries on errors. | Fast but blind — no chance to stop a bad command. |
| **Autopilot (Preview)** | Bypass + the agent answers its own clarifying questions instead of stopping to ask. | Fastest, most autonomous, hardest to course-correct mid-loop. |

Rule of thumb: **Default for any task you can't `git reset` out of**. Bypass when the change is contained and you're watching. 

### 1.3 Custom agents

A **custom agent** is a *new persona* in the agent picker, defined by a single Markdown file at `.github/agents/<name>.agent.md`. It has:

- A **`description`** — shown in the picker, also tells the model when to use this agent.
- A **`tools:`** whitelist — the only tools this persona can use (security boundary + smaller tool surface = better accuracy).
- A pinned **`model:`** — so behavior is reproducible across teammates.
- Optional **`handoffs:`** — buttons that appear after the agent's response to transition to *another* agent with a pre-filled prompt (Plan → Agent → Reviewer, etc.).
- A **system-prompt body** below the frontmatter — house rules in plain English.

In Exercise C you'll build three of them — a planner, a reviewer, and a test author — to see the surface in three different shapes.

> 🪧 **Disambiguation:** A custom agent is **not** the same as `AGENTS.md` (covered in Lab 2). `AGENTS.md` adds always-on instructions to *every* agent in your repo. A custom agent is *its own persona* with its own tool whitelist, model pin, and handoffs. They compose.

### 1.4 Model Context Protocol (MCP)

**Model Context Protocol (MCP)** is "USB-C for AI tools" — a standard way for an AI client (Copilot Agent) to talk to a server that exposes capabilities (tools, resources, prompts).

```
┌──────────────┐      MCP       ┌──────────────────┐
│ Copilot Chat │  ◀──────────▶  │ MCP Server       │
│  (client)    │   stdio/JSON   │ list_activities  │
└──────────────┘                │ get_signups_count│
                                └──────────────────┘
```

Two important properties:

- **Each MCP server runs as a separate process.** That's the security boundary. Copilot can't accidentally read your filesystem because of an MCP bug — only what the server explicitly exposes.
- **You register servers in `.vscode/mcp.json`.** VS Code launches them on demand, you accept a trust prompt the first time, and the tools show up in **Configure Tools** in the chat input.

Today you're going to **consume** one off-the-shelf MCP server (optional, requires Node) and then **build** one yourself in ~30 lines of Python (required — this is the load-bearing exercise).

---

## Part 2 — Hands-on

Now that the vocabulary is in place, run the four exercises in order. They build on each other (Exercise A installs `pytest` and `mcp[cli]`; Exercise B is a read-through walk of the Permission levels; Exercise C builds three custom agents that work together in a mini code-review pipeline; Exercise D's MCP server imports from the `app.py` Exercise A fixed).

### Exercise A — Agent loop in practice

The activities sign-up endpoint at `agents/backend/app.py` has two bugs you can spot by reading [`signup_for_activity`](./backend/app.py):

1. **No duplicate-email guard.** A student can sign up for the same activity twice (and so can their evil twin from a typo).
2. **No capacity check.** Activities have a `max_participants`, but `signup_for_activity` cheerfully appends past it.

You're going to let Agent fix both, write tests for them, and iterate until `pytest` is green. We'll do this in **two prompts** (one per concern) — that's a Copilot best practice: smaller, focused prompts produce tighter loops than one giant ask.

1. Make sure your chat is set to **Agent**, **Local** target, **Default Approvals**.

2. Drag `agents/backend/app.py` into the chat panel so it's pinned as context, then send **Prompt 1 — fix the bugs**:

   > ![Static Badge](https://img.shields.io/badge/-Prompt%201-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Two bugs in agents/backend/app.py signup_for_activity:
   >   1. It allows the same email to sign up twice for the same activity.
   >   2. It doesn't check max_participants — it lets the list grow past capacity.
   >
   > Fix both. When the duplicate case is hit, return HTTP 400 with detail
   > "Already signed up". When the capacity case is hit, return HTTP 400 with
   > detail "Activity is full".
   >
   > Do not write tests yet — just the fix.
   > ```

3. **Watch the loop on the fix.** Approve each tool call. You should see Agent read `app.py`, propose edits in the diff overlay, and stop once the two guards are in place.

4. Once the fix is accepted, send **Prompt 2 — add the tests**:

   > ![Static Badge](https://img.shields.io/badge/-Prompt%202-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Now create agents/tests/__init__.py and agents/tests/test_app.py with
   > four pytest cases covering the signup endpoint: happy path, duplicate
   > email, capacity reached, and 404 (unknown activity). Use FastAPI's
   > TestClient.
   >
   > Then run `pip install -r agents/requirements.txt` and
   > `pytest agents/tests/ -v` from the integrated terminal until all four
   > tests pass. Iterate if any fail.
   > ```

5. **Watch the loop on the tests.** Agent should:

   - Create `agents/tests/__init__.py` and `agents/tests/test_app.py`.
   - Run `pip install -r agents/requirements.txt` (this is where `pytest` and `mcp[cli]` resolve).
   - Run `pytest agents/tests/ -v` and read the output.
   - If anything failed: edit, re-run, repeat.

6. **Manually verify the duplicate guard from a separate terminal** — start the server (`uvicorn agents.backend.app:app --reload`) and:

   ```bash
   curl -X POST "http://127.0.0.1:8000/activities/Chess%20Club/signup?email=test@mergington.edu"
   curl -X POST "http://127.0.0.1:8000/activities/Chess%20Club/signup?email=test@mergington.edu"
   ```

   The first call returns success; the second returns `400 Already signed up`.

> ✅ **You should now see:** `pytest agents/tests/ -v` reports **4 passed** in the integrated terminal, and the second `curl` returns the 400 error above.

#### 🪧 Mid-exercise callout — Re-prompt with the plan-first pattern

Now revert your changes (`git checkout agents/backend/app.py && rm -rf agents/tests` — PowerShell: `git checkout agents/backend/app.py; Remove-Item -Recurse -Force agents/tests`) and re-run the **same task** with a tighter, plan-first prompt:

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
>
> ```prompt
> Same two bugs as before in agents/backend/app.py signup_for_activity
> (duplicate-email guard, capacity check) plus the four pytest cases.
>
> Before you write anything: produce a numbered plan listing every file
> you'll touch and every test name. Stop after the plan and wait for me
> to reply "go". Only then make changes.
> ```

Notice the difference: Agent stops after the plan, you eyeball it, type `go`, and *then* the loop runs. This is the **plan-first** pattern — it's a prompting technique you can apply inside Agent without switching personas. (Exercise C will show the alternative: switching to the dedicated **Plan** built-in agent.)

> ✅ **You should now see:** Agent posts a numbered plan and waits. After you reply `go`, it executes and ends with **4 passed** again.

---

### Exercise B — Permission levels (read-through)

> 📖 **No hands-on this round.** This exercise is a walk-through — read it, build a mental model of how the three Permission levels behave, and move on. (We're skipping the three reverts-and-re-runs because the back-and-forth `git checkout` dance is more friction than learning.)

The scenario: you give Agent the **same trivial prompt** three times, only changing the **Permission** picker between runs. Here's what you'd see in each case.

**The prompt (the one we'd send for runs 1 and 2):**

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
>
> ```prompt
> Add a GET /healthz endpoint to agents/backend/app.py that returns
> {"status": "ok"}. Then start the server (or assume it's running) and
> `curl http://127.0.0.1:8000/healthz` from the integrated terminal to
> verify the response.
> ```

#### Run 1 — Default Approvals (what would happen)

Agent pauses on **every tool call**: "read this file?", "apply this edit?", "run this command?". You click through each one. Slow, but you see (and can stop) every action before it touches your machine. **Pick this when:** you don't fully trust the prompt, or the change is hard to undo.

#### Run 2 — Bypass Approvals (what would happen)

Zero dialogs. The agent edits `app.py`, runs `curl`, and reports back without pausing once. Fast, but if the prompt was wrong you only find out after the fact. **Pick this when:** the change is contained, you're watching the chat live, and you have `git` to bail out with.

#### Run 3 — Autopilot Preview (what would happen) — with a deliberately vague prompt

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
>
> ```prompt
> Add a health check.
> ```

Under Default or Bypass, the agent would stop and ask: "what kind of health check? what path? what response?". Under Autopilot it **answers its own clarifying question** and just does *something* — usually a `GET /health` returning `{"status": "ok"}`, but the exact shape is up to the model. **Pick this when:** you're in a sandbox, you have a coffee, and the cost of "wrong but recoverable" is low.

> ✅ **You should now see** (mentally): why each tier exists, and which one you'd reach for in three different situations — a production hotfix, a routine refactor on a feature branch, and a Saturday-afternoon spike in a throwaway repo.

---

### Exercise C — Build a custom-agent toolbox

You'll build three custom agents, each demonstrating a different angle of the surface — **handoffs** (workflow chaining), **least-privilege** (read-only tools), and **scope-locking** (edit boundaries). Together they form a mini code-review pipeline: the scaffolder plans a feature, Agent builds it, the reviewer audits it, and the test author adds edge-case coverage.

---

#### C.1 — Plan-first scaffolder with handoff

You'll create a custom agent whose only job is to **scaffold a FastAPI endpoint with matching tests** — and whose handoff button transfers the plan to **Agent** for execution.

1. Open the Command Palette → **Chat: New Custom Agent**. Name it `endpoint-scaffolder`. Accept `.github/agents/` as the location. VS Code creates `.github/agents/endpoint-scaffolder.agent.md`.

2. **Replace the generated frontmatter** with this exact block (copy verbatim — the keys matter):

   ```yaml
   ---
   description: Scaffold a FastAPI endpoint in the agents/ app with matching tests and minimal frontend wiring.
   tools: [codebase, editFiles, runCommands, findTestFiles]
   model: gpt-5
   user-invocable: true
   disable-model-invocation: true
   handoffs:
     - agent: agent
       label: Implement this plan
       prompt: "Implement the plan above. Run pytest agents/tests/ -v and don't stop until green."
   ---
   ```

   Key points:
   - **No `infer:`** — that frontmatter key is deprecated. Use `user-invocable` (shows up in the picker) and `disable-model-invocation` (won't be auto-invoked by other agents).
   - **`tools:` is a whitelist.** `codebase` (read), `editFiles` (write), `runCommands` (terminal), `findTestFiles` (locate tests). No MCP tools, no anything else.
   - **`handoffs:`** defines the button label and the canned prompt the next agent receives.

3. **Below the frontmatter, paste this system-prompt body verbatim:**

   ````markdown
   You are an endpoint scaffolder for the FastAPI app under `agents/`. Follow these house rules without deviation:

   1. **Plan first, code never.** Your output is a numbered plan only — list every file you will create or modify, every test name, and every new endpoint signature. Do **not** apply edits yourself; the human will use the "Implement this plan" handoff to transfer execution to Agent.
   2. **Match the existing app shape.** New endpoints belong in `agents/backend/app.py`. New tests belong in `agents/tests/test_app.py` and use `fastapi.testclient.TestClient`.
   3. **One endpoint, one feature, one PR.** Keep the surface area small. If the request implies more than one endpoint, list the others as "out of scope for this plan" and stop.
   4. **Tests are mandatory.** Every plan must include at least one happy-path test and one error-case test (404 or 400).
   5. **Frontend wiring is optional.** Mention it as a one-line follow-up in the plan only if the prompt explicitly asks for UI changes.
   ````

4. **Save the file.** It should now be visible in the agent picker as `endpoint-scaffolder` with the description string from the frontmatter.

5. **Switch the chat picker to `endpoint-scaffolder`** (your custom agent, not Plan or Agent).

6. Send:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Scaffold a `GET /activities/{name}/spots-left` endpoint. It should return
   > {"spots_left": <int>} based on max_participants minus current
   > participants. 404 if the activity is unknown.
   > ```

   The scaffolder produces a structured plan following the five house rules above (file list, endpoint signature, test names, no edits applied yet).

7. **Click the "Implement this plan" handoff button** that renders below the scaffolder's response. Control transfers to the **Agent** built-in agent with the canned prompt pre-filled. Agent then executes — editing `agents/backend/app.py`, adding tests to `agents/tests/test_app.py`, and running `pytest` until green.

> ✅ **You should now see:** `endpoint-scaffolder` in the agent picker with its description visible · a numbered plan from your custom agent · a clickable **Implement this plan** button on the response · after the handoff, `pytest agents/tests/ -v` passes (now with at least 5 tests counting the new spots-left coverage) · `curl http://127.0.0.1:8000/activities/Chess%20Club/spots-left` returns `{"spots_left": <int>}`.

---

#### C.2 — Read-only code reviewer

You'll create a **read-only** custom agent that reviews code but never edits — demonstrating the **least-privilege** security boundary. Its tool whitelist excludes `editFiles` and `runCommands`.

1. Open the Command Palette → **Chat: New Custom Agent**. Name it `code-quality-reviewer`. Accept `.github/agents/` as the location.

2. **Replace the generated frontmatter** with this exact block:

   ```yaml
   ---
   description: Review code for blocking issues, security vulnerabilities, and logic errors. Read-only — no edits, no style nits.
   tools: [codebase, findTestFiles, search]
   model: gpt-5
   user-invocable: true
   disable-model-invocation: true
   ---
   ```

   Key points:
   - **Tools: `[codebase, findTestFiles, search]` only.** NO `editFiles`, NO `runCommands`. This is the security boundary — the agent can read, but cannot modify anything.
   - **No handoffs.** This is a terminal reviewer — it outputs a report and stops.

3. **Below the frontmatter, paste this system-prompt body verbatim:**

   ````markdown
   You are a code-quality reviewer for the `agents/` app. Follow these rules without deviation:

   1. **Review only the files explicitly mentioned by the user.** Never roam the codebase uninvited. If the user says "review app.py", read `agents/backend/app.py` only.
   2. **Output a structured report** with three sections:
      - **Blocking issues** — bugs, security vulnerabilities, unhandled errors, or missing critical validations. Empty if none found.
      - **Suggestions** — opportunities to improve correctness, error handling, or test coverage. Empty if none found.
      - **Nits** — minor observations. Keep this section very short or omit it entirely.
   3. **Anchor every finding to a `file:line` reference** so the user can jump directly to the issue.
   4. **No code rewrites.** Describe the fix in prose. Never paste replacement code — if the user wants the fix applied, they can ask Agent separately.
   5. **Stay scoped: correctness, security, error handling, test coverage.** Do NOT comment on style, formatting, or naming — linters do that.
   ````

4. **Save the file.** It should now be visible in the agent picker as `code-quality-reviewer`.

5. **Switch the chat picker to `code-quality-reviewer`**.

6. Send:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Review agents/backend/app.py, focusing on the spots-left endpoint we just added.
   > ```

   The reviewer reads `app.py` and outputs a structured report with **Blocking issues** / **Suggestions** / **Nits** sections. Each finding anchors to a `file:line` reference.

> ✅ **You should now see:** A structured review report with section headings · findings anchored to line numbers (e.g., `agents/backend/app.py:42`) · no code snippets pasted as "fixes" · **no edits applied** (the agent has no access to `editFiles`).

---

#### C.3 — Scope-locked test author

You'll create a custom agent that writes **only** test files under `agents/tests/` — demonstrating **scope-locking** via system-prompt enforcement. It has `editFiles`, but the prompt constrains where it can write.

1. Open the Command Palette → **Chat: New Custom Agent**. Name it `test-author`. Accept `.github/agents/` as the location.

2. **Replace the generated frontmatter** with this exact block:

   ```yaml
   ---
   description: Write test files for the agents/ app. Creates or modifies files ONLY under agents/tests/.
   tools: [codebase, editFiles, runCommands, findTestFiles]
   model: gpt-5
   user-invocable: true
   disable-model-invocation: true
   handoffs:
     - agent: agent
       label: Fix the bug this test caught
       prompt: "The test above is failing because of a real bug in production code. Fix the bug, then re-run pytest agents/tests/ -v until green."
   ---
   ```

   Key points:
   - **Tools: includes `editFiles` and `runCommands`**, but the system prompt will constrain edits to `agents/tests/` only.
   - **Handoff: back to Agent** if a test reveals a real bug.

3. **Below the frontmatter, paste this system-prompt body verbatim:**

   ````markdown
   You are a test author for the `agents/` app. Follow these rules without deviation:

   1. **You may only create or modify files under `agents/tests/`.** If the user asks for production code changes, politely decline and suggest switching to Agent.
   2. **Use `fastapi.testclient.TestClient`.** Mirror the existing test style in `agents/tests/test_app.py`.
   3. **Every test you write MUST be runnable.** Finish each session by running `pytest agents/tests/ -v` and reporting pass/fail counts.
   4. **Prefer adding edge-case tests over duplicating happy paths the suite already covers.** Read the existing tests first.
   5. **If you discover a real bug while writing a test**, leave the failing test in place and use the "Fix the bug this test caught" handoff to ask Agent to fix the production code. Do NOT silently skip the test or modify production code yourself.
   ````

4. **Save the file.** It should now be visible in the agent picker as `test-author`.

5. **Switch the chat picker to `test-author`**.

6. Send:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Add edge-case tests for the spots-left endpoint: (1) activity with zero signups,
   > (2) activity where max_participants is 0, (3) activity name that needs URL encoding
   > (e.g. "Dungeons & Dragons").
   > ```

   The test author creates new test cases in `agents/tests/test_app.py`, then runs `pytest agents/tests/ -v` to verify they pass.

7. **Manually verify the URL-encoding case works** — start the server (`uvicorn agents.backend.app:app --reload`) and:

   ```bash
   curl "http://127.0.0.1:8000/activities/Dungeons%20%26%20Dragons/spots-left"
   ```

   (The activity doesn't exist in the seed data, so you'll get a 404 — but that proves the URL encoding was handled correctly.)

> ✅ **You should now see:** New test cases added to `agents/tests/test_app.py` (edge cases: zero signups, max=0, URL-encoded names) · `pytest agents/tests/ -v` reports at least 8 passed · **no edits outside `agents/tests/`** (the agent declined to touch production code).

---

**🎁 You now have three personas in your picker.** The pattern scales — teams keep these in `.github/agents/` so every contributor inherits the same tooling. Custom agents are the cheapest way to encode "how this team works."

---

### Exercise D — Consume + create an MCP server

#### D.1 — Consume the filesystem MCP server (OPTIONAL)

> ⚠️ **Optional — skip if you don't have Node.js.** Run `node --version` in the integrated terminal. If it errors, jump to Activity D.2 (the create half). The rest of the lab does not depend on this section.

The repo already ships:

- `agents/sample-data/school-policies.txt` — a small text file Agent doesn't have open in the editor.
- `.vscode/mcp.json` — already wired up with the **`school-files`** filesystem MCP server pointing at `agents/sample-data/`.
- `.vscode/settings.json` — `"chat.mcp.discovery.enabled": true`.

Open `.vscode/mcp.json` and inspect the entry:

```jsonc
{
  "servers": {
    "school-files": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "${workspaceFolder}/agents/sample-data"
      ]
    }
  }
}
```

1. Open the Command Palette → **MCP: List Servers** → select `school-files` → **Start Server**. Accept the trust prompt the first time.

2. Open **Configure Tools** in the chat input. You should see filesystem tools (`read_file`, `list_directory`, etc.) under `school-files`.

3. With Agent selected, send:

   > 💡 The first time you run this, `npx` downloads the filesystem MCP server (~5–15 seconds). Subsequent runs are instant — don't hit Stop.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Read `school-policies.txt` from the school-files MCP server and
   > summarise the participation rules.
   > ```

> ✅ **You should now see:** an inline `read_file` tool call against `school-files` in the chat transcript, followed by Agent's summary of the seven policies. The summary is grounded in a file Agent could not otherwise see.

#### D.2 — Build your own MCP server (REQUIRED)

You're going to expose the in-memory `activities` dict from `agents/backend/app.py` as an MCP server, so that Agent can answer questions like "which activity is closest to full?" by calling tools instead of guessing.

1. **Confirm `mcp[cli]` is installed.** It was added to `agents/requirements.txt` in Exercise A. Re-run the install just to see it resolve:

   ```bash
   pip install -r agents/requirements.txt
   ```

2. **Confirm the package skeleton exists.** The repo ships an empty `agents/mcp/__init__.py` so Python treats `agents/mcp/` as a package.

3. **Open `agents/mcp/activities_server.py`.** It's already authored for you — the full ~30-line server lives at [`agents/mcp/activities_server.py`](./mcp/activities_server.py):

   ```python
   """Mergington activities MCP server — exposes the in-memory activities dict
   to MCP-aware clients (e.g. GitHub Copilot Agent Mode)."""

   from mcp.server.fastmcp import FastMCP
   from agents.backend.app import activities

   mcp = FastMCP("mergington-activities")


   @mcp.tool()
   def list_activities() -> list[str]:
       """Return the names of all extracurricular activities."""
       return list(activities.keys())


   @mcp.tool()
   def get_signups_count(activity: str) -> int:
       """Return the number of students signed up for a given activity.

       Raises ValueError if the activity is unknown.
       """
       if activity not in activities:
           raise ValueError(f"Unknown activity: {activity!r}")
       return len(activities[activity]["participants"])


   if __name__ == "__main__":
       mcp.run()
   ```

   Read it top to bottom — it's the entire server. Two tools, typed signatures, docstrings. The docstrings are how Agent decides when to call each tool, so they earn their keep.

4. **Confirm the `.vscode/mcp.json` registration.** Already wired:

   ```jsonc
   {
     "servers": {
       "mergington-activities": {
         "type": "stdio",
         "command": "${workspaceFolder}/.venv/bin/python",
         "args": ["-m", "agents.mcp.activities_server"]
       }
     }
   }
   ```

   > 🪟 **Windows:** in the snippet above, change `"command"` to `"${workspaceFolder}/.venv/Scripts/python.exe"`. Everything else is identical.

   (If you also did the consume half, both `school-files` and `mergington-activities` are present — both servers coexist happily.)

5. Open the Command Palette → **MCP: List Servers** → select `mergington-activities` → **Start Server**. Accept the trust prompt.

6. Open **Configure Tools** and verify both `list_activities` and `get_signups_count` show up under `mergington-activities`.

7. **Demo prompt — single tool call:**

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Use the mergington-activities MCP server to list all activities.
   > ```

8. **Demo prompt — chained tool calls:**

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Which activity is closest to full? Use the mergington-activities MCP.
   > ```

   This is the "aha" prompt — Agent must call `list_activities()` once, then `get_signups_count(...)` for each result, then compare against the `max_participants` it can see in `app.py`. The chain of tool calls is visible inline in the transcript.

9. **Negative-case prompt** — see how a tool error surfaces:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Get the signup count for `Knitting Club`.
   > ```

   `Knitting Club` doesn't exist; the tool raises `ValueError`; Agent reports it gracefully (and may suggest `list_activities()` first).

> ✅ **You should now see:** the chat transcript shows a `list_activities()` call followed by multiple `get_signups_count(...)` calls **before** Agent's final answer about which activity is closest to full. That visible chain is MCP earning its keep.

#### D.3 — Use an off-the-shelf MCP from a registry (Microsoft Learn MCP) (OPTIONAL)

D.1 had you consume a local filesystem MCP. D.2 had you build one from scratch. This activity demonstrates the third — and most common — pattern in production use: pulling a maintained MCP server off a public registry and connecting Agent to it. The **Microsoft Learn MCP** is an ideal example: it gives Copilot grounded access to official Microsoft documentation across Azure, .NET, Copilot itself, and more. Answers cite real `learn.microsoft.com` URLs instead of being synthesized from training data alone.

> 💡 **Note:** This activity has a different shape from D.1 and D.2. You're not building or configuring a local server; you're installing a maintained registry MCP and learning how to drive it with prompts that force authoritative sources.

1. **Install the Microsoft Learn MCP Server**

   Follow the installation instructions for your IDE here:

   [`https://github.com/mcp/microsoftdocs/mcp#-installation--getting-started`](https://github.com/mcp/microsoftdocs/mcp#-installation--getting-started)

   The upstream README handles cross-IDE details — we won't duplicate them here. For VS Code users, this typically means a one-click **Install** from the registry page that automatically adds an entry to `.vscode/mcp.json`. Accept the trust prompt the first time VS Code launches the server.

2. **Verify it's running**

   Open the Command Palette → **MCP: List Servers** → confirm `microsoft-learn` (or whatever name the registry assigned) appears in the list and is started.

3. **Try a research prompt**

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > I need to understand MCP in GitHub Copilot end-to-end (agent mode, registries, server setup). Search Microsoft docs.
   > ```

   This prompt forces Agent to search official Microsoft documentation for MCP concepts rather than relying solely on its training data.

4. **Try a follow-up that forces source citations**

   After Agent responds, send:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Cite the exact Microsoft Docs URLs you used.
   > ```

   This demonstrates the grounded-research angle: the MCP server fetched real documentation, and Agent can cite the specific pages.

5. **Tip: Phrases that improve responses with this MCP**

   | Goal | Add These Phrases |
   |------|-------------------|
   | Force official sources | `search Microsoft docs`, `fetch full doc` |
   | Depth | `deep dive`, `implementation details` |
   | Validation | `cite sources`, `list doc URLs` |

> ✅ **You should now see:** the MCP tool calls rendered inline in the transcript, the answer grounded in fetched documentation, and (after the follow-up) actual `learn.microsoft.com` URLs cited in the response.

#### D.4 — Browser automation with the Playwright MCP (OPTIONAL)

> ⚠️ **Optional — skip if you don't have Node.js.** Run `node --version` in the integrated terminal. If it errors, skip this section. D.4 is not a dependency for later labs.

D.1 and D.2 showed MCPs that expose **file access** and **database queries**. D.3 demonstrated **documentation research**. D.4 demonstrates a completely different shape of MCP: **stateful browser automation**. The Playwright MCP gives Agent a real Chromium browser with tools to navigate, screenshot, and extract structured data from JavaScript-rendered pages. Concrete uses: scaffolding end-to-end tests, scraping dynamic sites where `curl` returns empty shells, generating screenshots for documentation or PRs, reproducing UI bugs with exact browser state, or automating repetitive web flows (form submission, multi-page data collection).

> 💡 **Note:** This activity mirrors D.3's structure — you're consuming a registry MCP and learning prompt patterns that drive it effectively.

1. **Install the Playwright MCP Server**

   Follow the installation instructions at [`https://github.com/mcp/microsoft/playwright-mcp`](https://github.com/mcp/microsoft/playwright-mcp).

   For VS Code users, add this entry to `.vscode/mcp.json`:

   ```jsonc
   {
     "servers": {
       "playwright": {
         "type": "stdio",
         "command": "npx",
         "args": ["@playwright/mcp@latest"]
       }
     }
   }
   ```

   > 💡 The first time you run this, `npx` downloads the Playwright browser binaries (~200MB, one-time). The initial launch may take 30–60 seconds — don't hit Stop.

   After adding the entry, open the Command Palette → **MCP: List Servers** → select `playwright` → **Start Server**. Accept the trust prompt.

2. **Verify it's running**

   Open the Command Palette → **MCP: List Servers** → confirm `playwright` appears in the list and is started.

3. **Try it — capture a screenshot**

   <details>
   <summary><strong>Show Prompt for Screenshot Goal</strong></summary>

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Use the Playwright MCP with Microsoft Edge (headed). Go to https://www.nba.com/standings.
   > Maximize window.
   > Wait for network idle and the main standings table to be visible.
   > If a cookie/consent banner appears, accept or close it.
   > Scroll the full page to trigger any lazy-loaded content.
   > Return a short status JSON with:
   > {
   >   "ok": true/false,
   >   "title": "<page title>",
   >   "url": "<final url>",
   >   "detectedTables": <count>,
   >   "screenshot": "<path-to-screenshot>"
   > }
   > Also save a full-page PNG screenshot as ./artifacts/01_open_standings.png and include its path.
   > ```

   </details>

   This prompt demonstrates Playwright's value-add: it sees the **rendered DOM** after JavaScript execution, consent banners, and lazy-loaded content — things `curl` or static scrapers miss.

4. **Try it — extract structured data**

   <details>
   <summary><strong>Show Prompt for Data Extraction Goal</strong></summary>

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > From https://www.nba.com/standings in the current session, extract the full regular season standings table into a clean JSON array.
   >
   > Requirements:
   > One JSON object per team with fields:
   > { "rank", "team", "conference", "wins", "losses", "winPct", "gamesBehind", "streak", "home", "away", "last10" }
   > Normalize team names (e.g., "L.A. Clippers" → "LA Clippers"). Parse numbers as numbers.
   > If the site separates by conferences, include the correct "conference" value.
   > Validate: no empty rows, rank is numeric and unique within a conference.
   >
   > Output:
   > Return the JSON array (pretty-printed).
   > Save it to ./data/standings_raw.json and confirm file path in your reply.
   > ```

   </details>

   This is where the LLM + browser combination shines: Agent navigates, evaluates JavaScript to extract table rows, normalizes inconsistent formatting, and returns typed JSON — all in one call chain.

5. **(Optional within optional) — Multi-page enrichment**

   For advanced scraping patterns, try this prompt to visit the top teams' pages and extract arena or coach details:

   > For the top 4 teams per conference in `./data/standings_raw.json`, navigate to each team's official NBA page and extract visible `arena` or `coach` name. Save merged data to `./data/standings_enriched.json`.

   This demonstrates multi-page workflows: Playwright maintains session state (cookies, localStorage) across navigations — ideal for authenticated flows or paginated datasets.

6. **Tip: Phrases that improve responses with this MCP**

   | Goal | Add These Phrases |
   |------|-------------------|
   | Reliability | `wait for network idle`, `wait for selector`, `accept any cookie banner` |
   | Reproducibility | `headed`, `Microsoft Edge`, `maximize window`, `save screenshot to ./artifacts/` |
   | Structured output | `return JSON with fields...`, `parse numbers as numbers`, `normalize team names` |

> ✅ **You should now see:** the Playwright MCP tool calls rendered inline in the transcript (navigate → screenshot → evaluate), an actual PNG file landed in `./artifacts/`, and structured JSON in `./data/`. You just gave Agent a real browser.

#### 📖 Wrap: What we skipped

- **Resources** — MCP's other primitive (think files/URIs the model can read). We only built **tools** today. Resources are a great follow-up.
- **The MCP host/client** — we used Copilot Chat *as* the client. Writing a custom MCP host is a different lab.
- **The MCP registry** — explore [`https://github.com/mcp`](https://github.com/mcp) for hundreds of community servers (GitHub, Sentry, Postgres, ...).

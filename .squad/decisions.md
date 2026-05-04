# Squad Decisions

## Lab 3 Planning (2026-04-20)

Three planning agents (Zoe / Book / River) produced reference material
for Lab 3 — "GitHub Copilot Agent Mode". Their full deliverables are
preserved below as input for Kaylee.

**Open contradictions Kaylee must resolve:**

1. Cloud Coding Agent in Lab 3? Zoe = yes (payoff); Book = defer.
2. Custom-agent file path: use **`.github/agents/*.agent.md`**
   (Book's correction), not `.github/chatmodes/*.chatmode.md`.
3. Exercise 2 feature: River chose "unregister"; Zoe notes Lab 1
   already ships it. Pick a non-overlapping replacement.

---

### Zoe — Lab 3 Plan (Lead)

# Lab 3 Plan — Agent Mode in GitHub Copilot

**Owner:** Zoe (Lead) · **Status:** Draft for Book & River review · **Duration:** 90 min

---

## 0. Framing pushback (read this first)

The user's idea — *"how to create custom agents"* — is the right instinct but too narrow to fill a 90-min lab and too narrow to justify a third lab in this curriculum. Lab 1 already taught Agent Mode at the "press the button, fix a bug, add a feature" level. Lab 2 taught how to *shape* Copilot's behavior with files (`AGENTS.md`, prompt files, skills). The gap Lab 3 must close is **what Agent Mode actually is under the hood, and how a developer extends, controls, and offloads it to do real work** — not a tour of one feature.

So Lab 3 is reframed as: **"Extending Agent Mode — custom chat modes, MCP, and delegating work to the cloud."** Custom agents (custom chat modes) are the spine. MCP is the multiplier. Delegating to the cloud Coding Agent is the payoff that makes the whole thing feel grown-up.

---

## 1. Learning objective

By the end of this lab, the learner can **extend GitHub Copilot Agent Mode with a custom chat mode, connect it to an external tool via an MCP server, and delegate a follow-up task to the cloud-hosted Coding Agent** — using the existing `agents/` school activities app as the playground.

(One objective. Three concrete capabilities feeding into it. Do not split into two objectives.)

---

## 2. Audience & prerequisites

**Audience:** developers who have completed Lab 1 and Lab 2. They know what Agent Mode is, they have used Plan Agent, they have written `copilot-instructions.md`, an `AGENTS.md`, a prompt file, and a skill.

**Must already have:**
- VS Code with the GitHub Copilot + Python extensions, signed in to a Copilot-enabled account.
- Python 3.10+, ability to run `uvicorn`.
- The repo cloned, `agents/` app runnable locally (we will give them the one-liner).
- Comfort reading FastAPI + vanilla JS at the level of Lab 1.

**Explicitly NOT required:** prior MCP knowledge, prior knowledge of VS Code chat mode files, any GitHub Actions experience.

---

## 3. 90-minute time budget

| Time | Block | What happens |
|------|-------|--------------|
| **0–8** | Intro & orientation | Recap Lab 1/2, frame the gap, run `agents/` app, confirm everyone sees it on `localhost:8000`. |
| **8–20** | Theory block 1 — *Anatomy of Agent Mode* | What an "agent" actually is: model + system prompt + tools + autonomy loop. Where custom chat modes, MCP, and the cloud Coding Agent each plug in. **12 min hard cap.** |
| **20–45** | Hands-on 1 — *Build a custom chat mode* | Create `.github/chatmodes/activities-architect.chatmode.md`, scope its tools, give it a persona aligned with the `agents/` codebase, use it to add a real feature (see §7). |
| **45–52** | Theory block 2 — *MCP in 7 minutes* | What MCP is, why it matters, the client/server model, how VS Code consumes it. **No slides longer than this.** |
| **52–75** | Hands-on 2 — *Wire an MCP server into the custom chat mode* | Add the GitHub MCP server (already familiar) **and** a filesystem or SQLite MCP server to `.vscode/mcp.json`, restrict which tools the custom chat mode can call, use it to do something the bare agent could not do cleanly. |
| **75–85** | Hands-on 3 — *Delegate to the cloud* | Open an issue in the learner's fork describing a follow-up enhancement, assign it to Copilot (Coding Agent), watch it open a draft PR. Brief because it runs async. |
| **85–90** | Wrap | Recap the three layers (local custom mode → MCP tools → cloud delegation), point at autonomy controls (allowed tools, checkpoints, undo), preview what we deliberately left out. |

Theory totals **19 min** across two blocks, neither exceeding 12 min. Hands-on totals **58 min**. Within budget.

---

## 4. Lab arc (5 sections)

1. **Step 1 — What Agent Mode actually is.** Theory + a 2-minute "look at the tools picker" tour in VS Code. Sets the mental model for the rest of the lab.
2. **Step 2 — Build your first custom chat mode.** Create the `.chatmode.md` file, give it a focused persona for the activities app, restrict its tools, invoke it from the chat mode picker, and use it to ship a small feature.
3. **Step 3 — Give your agent superpowers with MCP.** Configure `.vscode/mcp.json`, add 1–2 MCP servers, expose only the tools the custom chat mode is allowed to use, demonstrate a task that requires an external tool.
4. **Step 4 — Delegate work to the cloud Coding Agent.** Show the GitHub.com side: assign an issue to Copilot, review the draft PR it opens, discuss when this beats local Agent Mode.
5. **Step 5 — Controlling the agent.** Short closing section on autonomy controls — tool allowlists, checkpoints, reverting changes, when to use Plan Agent first. Wraps the lab.

---

## 5. What we WILL cover

1. **The agent loop & tool ecosystem** — model + instructions + tools + autonomy. The mental model that makes everything else click. (Theory only, ~12 min.)
2. **Custom chat modes (`.chatmode.md`)** — VS Code's mechanism for "custom agents": persona, model selection, restricted tool list, invocation from the mode picker. **This is the user's "custom agents" ask, sharpened.**
3. **MCP servers in Agent Mode** — `.vscode/mcp.json`, adding a server (GitHub MCP + one more), exposing tools to the agent, scoping which tools the custom mode can use.
4. **Cloud Coding Agent (delegation)** — assigning an issue to Copilot on GitHub.com, reviewing the resulting draft PR, when async delegation is the right call vs local Agent Mode.
5. **Autonomy controls (woven through, recapped at the end)** — tool allowlists per chat mode, auto-approve vs ask, checkpoints / undoing agent edits.

These are non-overlapping with Lab 2:
- Lab 2's `AGENTS.md` = *instructions injected into every agent run*.
- Lab 3's `.chatmode.md` = *a whole new agent persona with its own tool surface*.
- Lab 2's prompt files = *reusable user prompts*.
- Lab 3's MCP = *new tools the agent can call*.
- Lab 2's skills = *domain knowledge bundles Copilot reads*.
- Lab 3's Coding Agent = *running the agent off your machine entirely*.

---

## 6. What we will NOT cover (and why)

- **Ask vs Edit vs Agent vs Plan deep-dive.** Already in Lab 1. We reference it in 30 seconds, don't re-teach.
- **Writing your own MCP server from scratch.** Worth a whole separate lab. We *consume* MCP, we don't *build* MCP. Mentioned in the wrap as "next step."
- **Copilot Extensions / GitHub Apps.** Different surface, different audience (publishers, not consumers). Out of scope.
- **Inline completions, edit mode, code review in PRs.** Not Agent Mode. Out of scope.
- **Model selection theory** (which LLM to pick). One-line mention inside the chatmode file, no comparison matrix.
- **`AGENTS.md` and prompt files.** Done in Lab 2. We *use* the existing `AGENTS.md` from Lab 2, we don't re-author it.
- **Org-level MCP governance / policy.** Enterprise concern, scope creep, skip.
- **Evaluations / prompt optimization.** Foundry/eval territory. Out of scope.

---

## 7. Hands-on exercise spine

**Constraint:** every hands-on must produce a visible change in the running `agents/` app or in the learner's GitHub fork. No toy code.

**Step 2 — Custom chat mode delivers a real feature.**
Create `.github/chatmodes/activities-architect.chatmode.md` with:
- Persona: "Mergington activities backend specialist. Always update the in-memory store, the FastAPI route, and the frontend together. Prefer minimal diffs."
- Tools: `codebase`, `editFiles`, `runCommands`, `problems` (no web search, no terminal-wide tool).
- Model: pick a strong default.

Then use that mode to ship **"add an `unregister` endpoint + a Remove button on each activity card"** — a concrete user-facing feature that touches `app.py`, `index.html`, and `app.js`. Visible result: clicking Remove drops a participant from the list and the count updates.

> Note: Lab 1 already adds an "unregister" feature. Need to replace this with a different non-overlapping feature — see Open Question Q1 below.

**Step 3 — MCP-powered task the bare agent could not do cleanly.**
Add to `.vscode/mcp.json`:
- The **GitHub MCP server** (already known, low-friction).
- A **SQLite MCP server** (or filesystem MCP server — Book to confirm easiest cross-platform option).

Restrict the custom chat mode's tool list to add only the specific MCP tools it needs. Then prompt it to: *"Look at the open issues in this repo labeled `lab3-task`, pick the one about activity categories, and implement it."* The agent reads the issue via GitHub MCP, then implements **activity categories** (e.g. Sports / Arts / Academic) — backend field, frontend filter dropdown. Visible result: filter UI works.

**Step 4 — Delegate to the cloud Coding Agent.**
Learner opens an issue in their fork: *"Add a 'spots remaining' badge styling and a 'Full' state to the activity cards."* Assigns it to Copilot. Within a few minutes, a draft PR appears. Learner reviews the diff, leaves a comment, optionally merges. Visible result: a real PR in their fork.

This three-step spine takes the learner from **local custom agent → local custom agent + external tools → fully delegated agent**. That progression *is* the lab.

---

## 8. Open questions for Book & River

**For Book (research / accuracy):**
- **Q1.** Lab 1 already implements "unregister." Confirm a replacement first feature for Step 2 — candidates: (a) "mark activity as cancelled," (b) "duplicate an activity into next term," (c) "add a difficulty level field with badge." Which has the cleanest 20-min footprint and best showcases multi-file agent edits?
- **Q2.** Confirm the **exact current syntax** for VS Code custom chat mode files: filename (`*.chatmode.md`), location (`.github/chatmodes/` vs `.vscode/`), frontmatter keys (`description`, `tools`, `model`), and how the mode appears in the picker. Docs have shifted; we need the version that ships in the GA build at lab-recording time.
- **Q3.** Confirm `.vscode/mcp.json` is still the right config surface (vs `settings.json` `chat.mcp.servers`). Pick the one that's stable and discoverable.
- **Q4.** Pick the second MCP server. SQLite needs a DB file we'd have to seed. Filesystem MCP needs path scoping. Which one gives a cleaner 20-min hands-on without yak-shaving?
- **Q5.** Cloud Coding Agent prerequisites: does the learner need anything beyond a Copilot-enabled account and a fork? Any org policy gate that will block half the room? If yes, we need a fallback path.

**For River (learner experience / pacing):**
- **Q6.** Step 3 (MCP wiring) is the highest-risk block for getting stuck. Should we ship a pre-baked `.vscode/mcp.json` in the repo on a `lab3-start` branch that learners copy, and have them only edit the chat mode's tool allowlist? My instinct: yes.
- **Q7.** Step 4 runs async (cloud agent takes minutes). Should we kick it off at minute 75 and *return to the local diff while waiting*, instead of staring at a spinner? Need a filler micro-activity.
- **Q8.** Do we need a "if Copilot cloud is disabled in your org" escape hatch — e.g. show a recorded GIF and move on — to keep the 90-min budget?

---

## Notes for Kaylee (when she writes the lab)

- Match Lab 2's structure: `## Step N` → `### 📖 Theory` → `### Activity` → prompt blocks in the badge style.
- Reuse the `agents/` app **as-is**. Do not reorganize folders. Do not rename files.
- Each prompt the learner copies into Copilot must be in a fenced block with the Copilot prompt badge, exactly like Lab 2.
- End with a "Key Takeaways" + "What's Next?" section pointing at: writing your own MCP server, Copilot Extensions, evals.

---

### Book — Agent Mode Capability Inventory (Copilot Expert)

# Capability Inventory — GitHub Copilot Agent Mode (VS Code)

**Author:** Book (Copilot Expert)
**Requested by:** Geronimo Basso
**Purpose:** Authoritative scoping input for Lab 3 — "GitHub Copilot Agent Mode" (90 min)
**Sources accessed:** 2026-04-20 (all `code.visualstudio.com/docs` URLs cited inline)

> ⚠️ **Naming note up front.** What the community still calls "Agent Mode" is, in current VS Code docs, structured as: a **Local agent session** running the built-in **Agent** persona. The picker calls it **Agent**. "Mode" is no longer the official noun — but it's still the term learners search for, so the lab title is fine. Internally, refer to it as the **Agent built-in (local) agent**.

---

## 1. What Agent Mode IS

The **Agent** built-in agent is a **local, autonomous coding agent** that runs inside VS Code's Chat view: you give it a high-level goal and it plans the work, edits files across the workspace, runs terminal commands and tools, observes results, and self-corrects until the task is done ([VS Code docs — Local agents, accessed 2026-04-20](https://code.visualstudio.com/docs/copilot/agents/local-agents)). It differs from **Ask** (read-only Q&A about the codebase; produces code blocks you apply manually) and **Plan** (read-only planning persona that produces a structured implementation plan and asks clarifying questions, then hands off) ([same source](https://code.visualstudio.com/docs/copilot/agents/local-agents)). All three are **built-in agents** selected from the agent picker in the Chat view; you can switch between them mid-session.

---

## 2. Stable Capabilities (as of April 2026)

All citations: [VS Code docs, accessed 2026-04-20](https://code.visualstudio.com/docs/copilot/agents/overview) unless noted.

- **Tool calling.** Agent autonomously selects and invokes tools each turn — built-in tools, MCP tools, extension-contributed tools, and tool sets. User can scope per-request via the **Configure Tools** picker, or `#toolName` to force one ([agent-tools](https://code.visualstudio.com/docs/copilot/agents/agent-tools)).
- **Multi-file editing.** Agent edits across the workspace directly in the editor; an overlay lets you navigate, keep, or discard each change ([local-agents](https://code.visualstudio.com/docs/copilot/agents/local-agents)).
- **Terminal command execution + approval flow.** Agent can run shell commands; by default each command surfaces an approval dialog. Approval behavior is governed by the session's **Permission level** (see Auto-approve below) ([agent-tools §Permission levels](https://code.visualstudio.com/docs/copilot/agents/agent-tools)).
- **Running tests / build verification.** Achieved via the terminal tool + task tools; the agent loop reads exit codes / output and iterates until green. Not a separate feature — it's emergent from tool calling + the agent loop.
- **MCP server integration.** Add via `@mcp` in Extensions view, **MCP: Add Server**, or by editing `.vscode/mcp.json` (workspace) / user `mcp.json`. Both `stdio` and remote `http` servers supported. Tools auto-appear in the Configure Tools picker ([mcp-servers](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)).
- **Custom agents (formerly "custom chat modes").** Markdown files with `.agent.md` extension + YAML frontmatter (`description`, `tools`, `model`, `agents` (subagents), `handoffs`, `target`, etc.). Locations:
  - Workspace: **`.github/agents/`** (VS Code native)
  - Workspace: **`.claude/agents/`** (Claude format, also recognized)
  - User profile: **`~/.copilot/agents/`** or VS Code user-data dir
  - Any `.md` in `.github/agents/` is also detected as a custom agent
  - Created via **Chat: New Custom Agent** command or the Chat Customizations editor ([custom-chat-modes](https://code.visualstudio.com/docs/copilot/customization/custom-chat-modes))
- **Always-on instructions for agents.** Three coexisting mechanisms: `.github/copilot-instructions.md` (single file), one or more `AGENTS.md` files (workspace root; subfolder support is experimental), and `CLAUDE.md` (compat). Plus file-scoped `*.instructions.md` with `applyTo` glob ([custom-instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)).
- **Checkpoints / undo / accept-reject.** Editor overlay controls let you step through suggested edits and keep or discard each; agent sessions are tracked in the **sessions list** so you can return to or fork them ([local-agents](https://code.visualstudio.com/docs/copilot/agents/local-agents); [chat-sessions](https://code.visualstudio.com/docs/copilot/chat/chat-sessions)).
- **Model picker.** Per-session model selector in the Chat view; custom agents can pin a `model:` (or a prioritized array of models) in frontmatter. Models known to support Agent today include GPT-5.x family, Claude Sonnet 4.x, plus BYOK providers ([custom-chat-modes](https://code.visualstudio.com/docs/copilot/customization/custom-chat-modes), [language-models](https://code.visualstudio.com/docs/copilot/customization/language-models)).
- **Auto-approve / autonomy controls — Permission levels** (per session, set in chat input area):
  - **Default Approvals** — confirmation dialogs for risky tools.
  - **Bypass Approvals** — auto-approves all tool calls; auto-retries on errors. Stable.
  - **Autopilot (Preview)** — Bypass + auto-responds to clarifying questions; agent runs until done ([agent-tools §Permission levels](https://code.visualstudio.com/docs/copilot/agents/agent-tools)).
- **Subagents.** Custom agents can list other agents in `agents:` frontmatter and invoke them via the `agent` tool ([custom-chat-modes](https://code.visualstudio.com/docs/copilot/customization/custom-chat-modes)).
- **Handoffs.** Frontmatter-defined buttons that appear after a response to transition to another agent with a pre-filled prompt (e.g., Plan → Implementation → Review) ([same](https://code.visualstudio.com/docs/copilot/customization/custom-chat-modes)).
- **Reusability across surfaces.** Custom agents authored locally also run in **Copilot CLI (background)** and **Cloud agents** ([overview](https://code.visualstudio.com/docs/copilot/agents/overview)).

---

## 3. Preview / Experimental

- **Autopilot permission level** — Preview ([agent-tools](https://code.visualstudio.com/docs/copilot/agents/agent-tools)).
- **Browser elements as context / integrated browser agent testing** — Experimental ([overview](https://code.visualstudio.com/docs/copilot/agents/overview)).
- **Image carousel in chat responses** (`imageCarousel.chat.enabled`) — Experimental.
- **Subfolder `AGENTS.md`** discovery — Experimental ([custom-instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)).
- **Hooks scoped to a custom agent** (`hooks` frontmatter, gated by `chat.useCustomAgentHooks`) — Preview.
- **Chat Customizations editor** (`Chat: Open Chat Customizations`) — Preview but recommended UX for managing agents/instructions/MCP in one place.
- **Parent-repo discovery in monorepos** (`chat.useCustomizationsInParentRepositories`) — opt-in setting.
- **Collapsed tool summaries** (`chat.agent.thinking.collapsedTools`) — Experimental.

---

## 4. Recently Changed / Renamed (the lab MUST get these right)

| Old name / behavior | Current (April 2026) | Citation |
|---|---|---|
| **Edit mode** | **Deprecated.** Use Agent for multi-file edits. Re-enable via `chat.editMode.hidden`. The "Plan" agent replaces Edit's planning use case but is **not** a rename of Edit. | [local-agents §Edit mode (deprecated)](https://code.visualstudio.com/docs/copilot/agents/local-agents) |
| "Custom chat modes" / `.chatmode.md` files | Now **custom agents** with **`.agent.md`** extension. Folder is **`.github/agents/`** (not `.github/chatmodes/`). The doc page URL is still `custom-chat-modes` for SEO. | [custom-chat-modes](https://code.visualstudio.com/docs/copilot/customization/custom-chat-modes) |
| `infer: true/false` frontmatter | **Deprecated** in favor of `user-invocable` and `disable-model-invocation`. | [same](https://code.visualstudio.com/docs/copilot/customization/custom-chat-modes) |
| Single "Agent Mode" toggle | Now a multi-axis choice: **Agent Target** (Local / CLI / Cloud / Third-party) × **Agent** (Agent / Plan / Ask / custom) × **Permission level**. | [overview](https://code.visualstudio.com/docs/copilot/agents/overview) |
| Tool approval was a single toggle | Replaced by 3-tier **Permission levels** (Default / Bypass / Autopilot). | [agent-tools](https://code.visualstudio.com/docs/copilot/agents/agent-tools) |

> **Important for the lab title:** The user's framing "Plan mode (formerly Edit)" is **wrong**. Edit mode is deprecated; Plan is a separate built-in agent for planning, not a rename. Correct this in lab intro.

---

## 5. Common Pitfalls / Failure Modes

1. **Approval fatigue.** With Default Approvals, long tasks generate dozens of dialogs; learners click through carelessly. Teach Permission levels explicitly and the security implications of Bypass/Autopilot.
2. **Agent stops mid-task** when it hits a blocking clarifying question — only Autopilot auto-responds. Learners think it "broke."
3. **Context window exhaustion** on multi-file edits in large repos — agent forgets earlier files. Mitigate with focused `#file`/`#codebase` scoping and smaller goals.
4. **Tool overload.** Too many MCP/extension tools enabled degrades model accuracy. Teach the Configure Tools picker and per-agent `tools:` whitelisting.
5. **Custom agent file in wrong location.** `.github/chatmodes/` (old), `.copilot/agents/`, root-level `.agent.md` — none are picked up. Must be `.github/agents/*.agent.md` (or `.md`).
6. **AGENTS.md vs copilot-instructions.md confusion.** Both apply, no defined order, content can conflict. Recommend choosing one for project-wide rules.
7. **`chat.agent.enabled` disabled at org level** — agent picker doesn't appear; not a bug, contact admin.
8. **Terminal commands run from the wrong cwd** in multi-root workspaces. Pin via instructions or explicit prompts.
9. **Edits applied without review** — learners hit "Keep all" and lose ability to undo cleanly. Show the per-edit accept/reject overlay.
10. **MCP server trust prompts** ignored — security risk. Teach the trust model.

---

## 6. Recommendation: Lab 3 Scope (90 min)

Lab 2 already covered: custom instructions, prompt files, skills. To **avoid overlap and maximize value**, Lab 3 should focus on what is *uniquely Agent*:

### Ranked picks (do these 4, in order)

1. **🥇 The Agent loop in practice — multi-file edit + terminal + test iteration** *(~30 min)*
   Build a small failing-test scenario; let Agent diagnose, edit across 2–3 files, run tests, self-correct. Teaches the core agent loop, edit review overlay, and stop button. **Highest signal, zero overlap with Lab 2.**

2. **🥈 Permission levels & the approval flow** *(~15 min)*
   Walk through Default → Bypass → Autopilot on the same task. Discuss security trade-offs explicitly. This is the #1 thing learners get wrong in production. **Non-overlapping, high stakes.**

3. **🥉 MCP server integration in Agent** *(~25 min)*
   Install one MCP server (e.g., GitHub MCP or Playwright), show it appearing in Configure Tools, drive it from Agent. Edit `.vscode/mcp.json` once by hand. **The single biggest "wow" capability and the gateway to everything else.**

4. **Custom agents (`.agent.md`) — Plan → Implementation handoff** *(~20 min)*
   Create a workspace `.github/agents/planner.agent.md` with read-only tools and a handoff to the built-in Agent. Demonstrates personas, tool scoping, frontmatter, **and** corrects the user's "custom agents = one topic" assumption by showing it sits *on top of* Agent mode. **Touches Lab 2 (instructions are similar in spirit) but the mechanism is distinct — frontmatter + tool whitelisting + handoffs are new.**

### Explicitly DEFER to a future lab
- Cloud agents / Copilot CLI background agents (different surface, deserves own lab)
- Subagents and nested workflows (advanced, easy to confuse with handoffs)
- Hooks (Preview, unstable API)
- Third-party agents (Anthropic/OpenAI harnesses)
- BYOK models

### Lab opener correction (1 slide)
Show the picker hierarchy — **Target → Agent → Permission** — and explicitly retract the "Plan = renamed Edit" framing. Edit is deprecated; Plan is a separate persona.

---

## Sources (all accessed 2026-04-20)

- https://code.visualstudio.com/docs/copilot/agents/overview
- https://code.visualstudio.com/docs/copilot/agents/local-agents
- https://code.visualstudio.com/docs/copilot/agents/agent-tools
- https://code.visualstudio.com/docs/copilot/customization/custom-chat-modes
- https://code.visualstudio.com/docs/copilot/customization/custom-instructions
- https://code.visualstudio.com/docs/copilot/customization/mcp-servers
- https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode

---

### River — Lab 3 Hands-On Design (Patterns & Prompting)

# Lab 3 — Agent Mode: Hands-On Design

**Author:** River (Patterns & Prompting)
**For:** Lab 3 — GitHub Copilot Agent Mode (90 min, ~55 min hands-on)
**Codebase:** `agents/` — FastAPI + vanilla JS school activities sign-up app
**Assumes Lab 2 covered:** custom instructions, prompt files, skills. **Do not repeat.**

---

## 1. App-State Assessment

### What it does today
- `agents/backend/app.py` — FastAPI server with **3 hard-coded activities in an in-memory dict** (Chess Club, Programming Class, Gym Class).
- `GET /activities` returns the dict; `POST /activities/{name}/signup?email=...` appends to `participants`.
- `agents/frontend/index.html` + `app.js` + `styles.css` — single-page UI: lists activities as cards, dropdown + email form to sign up, message banner.
- `agents/backend/data/activities.json` exists but is **NEVER READ** by `app.py` (orphan file, contains "(JSON)" suffixed copies of the in-memory data — clearly placeholder).
- `requirements.txt`: `fastapi`, `uvicorn`, `httpx`, `watchfiles`. No `pytest` yet.

### Missing / buggy / incomplete (improvement backlog)

| # | Issue | File(s) | Effort |
|---|---|---|---|
| 1 | `activities.json` exists but is unused — data source mismatch | `backend/app.py`, `backend/data/activities.json` | **S** |
| 2 | **No duplicate-signup guard** — same email can sign up N times for same activity | `backend/app.py:55-67` | **XS** |
| 3 | **No capacity check** — `max_participants` is displayed but never enforced; signup succeeds past the limit | `backend/app.py:55-67` | **XS** |
| 4 | **No unregister endpoint** — frontend has no way to drop a student | `backend/app.py`, `frontend/app.js`, `index.html` | **S** |
| 5 | No tests at all (no `tests/`, no `pytest` in requirements) | new `tests/` dir | **S** |
| 6 | Server-side email validation missing — `email` is a raw `str` query param, no `@` check, no domain check | `backend/app.py:56` | **XS** |
| 7 | Signup uses query-string `?email=` instead of JSON body — non-RESTful, awkward to extend | `backend/app.py`, `frontend/app.js:52` | **S** |
| 8 | No search / filter / category in UI; activity list will not scale past ~10 items | `frontend/app.js`, `index.html`, `backend/app.py` (add `category` field) | **M** |
| 9 | No persistence — restart wipes signups (links back to #1: should write through to `activities.json`) | `backend/app.py` | **S** |
| 10 | No error handling on capacity-full / duplicate in `frontend/app.js` (relies on generic `result.detail`) | `frontend/app.js:60-68` | **XS** |

This is the menu the exercises pull from.

---

## 2. Recommended Hands-On Exercises (3 exercises, ~55 min)

Each exercise is **cumulative**. The narrative arc: *"You inherited a half-finished app. Use Agent Mode to ship it."*

### Exercise 1 — Multi-file bug fix + test scaffolding (≈ 20 min)
**Agent Mode capability demonstrated:** multi-file edits + terminal execution (run `pip install`, run `pytest`).

**Prompt the learner gives the agent (paraphrased — they should write their own):**
> "In `agents/backend/app.py`, the `signup_for_activity` endpoint has two bugs: it allows the same email to sign up twice, and it ignores `max_participants`. Fix both with HTTP 400 errors and clear messages. Then add `pytest` and `httpx` test deps to `agents/requirements.txt`, create `agents/tests/test_app.py` covering: happy-path signup, duplicate rejection, capacity rejection, 404 for unknown activity. Run the tests and make sure they pass."

**What the agent should do (multi-step, in one run):**
1. Edit `backend/app.py` — add two `if` checks before `participants.append`.
2. Edit `requirements.txt` — add `pytest`.
3. Create `tests/__init__.py` and `tests/test_app.py` with FastAPI `TestClient` fixtures.
4. Run `pip install -r agents/requirements.txt` in the integrated terminal.
5. Run `pytest agents/tests/ -v`, observe failures, iterate, and end green.

**Checkpoint:** `pytest -v` shows 4 passing tests in the terminal. Manually POSTing the same email twice via curl returns `400 Already signed up`.

---

### Exercise 2 — Build a feature end-to-end with a "plan-first" prompt (≈ 20 min)
**Agent Mode capability demonstrated:** larger multi-file change spanning backend + frontend + tests, with the **plan-then-execute** pattern.

**Scenario:** "Students need to be able to **unregister** from an activity."

**Prompt pattern (taught explicitly):**
> "**Before writing any code**, list the files you'll touch and the changes you'll make. Wait for me to approve. Then implement."

The learner reviews the plan, approves (or trims it — e.g., "skip the confirmation modal for now"), and lets the agent execute.

**What the agent should do:**
1. Add `DELETE /activities/{name}/signup?email=...` (or proper body) to `backend/app.py` with 404 for unknown activity, 400 if email not registered.
2. Add an "Unregister" button per participant on each activity card in `frontend/index.html` + `app.js` (requires also updating `fetchActivities` to render participants — currently it doesn't show the participant list at all, which the agent should notice).
3. Extend `tests/test_app.py` with unregister cases.
4. Run `pytest`; start `uvicorn agents.backend.app:app --reload`; learner verifies in browser.

**Checkpoint:** Activity card now shows participant emails with an "✕ Unregister" button. Clicking it removes the email and updates the spots-left counter without a page refresh. All tests still green.

---

### Exercise 3 — Custom Agent / Custom Chat Mode for repeatable scaffolding (≈ 15 min)
**Agent Mode capability demonstrated:** **defining a custom chat mode (custom agent)** scoped to this codebase, then using it.

See section 3 for the full spec. Short version: the learner authors `.github/chatmodes/endpoint-scaffolder.chatmode.md`, then invokes it with one line ("scaffold a `categories` endpoint") and watches it produce route + test + frontend wiring **in the project's house style** (because the chatmode file pins conventions).

**Checkpoint:** A new `GET /categories` endpoint exists, returns distinct activity categories, has a test, and the frontend has a category filter dropdown — all generated from a single-line prompt to the custom mode.

---

### (Stretch — only if a group finishes early, ~10 min) Exercise 4 — MCP / external context
Wire up the GitHub MCP server (or filesystem MCP) and ask the agent: *"Open issue #X in this repo, read the description, and implement it."* Demonstrates Agent Mode pulling context from outside the editor. Skip if behind on time. **Book — confirm MCP setup story for the lab environment (see Open Questions).**

---

## 3. Custom Agent / Custom Chat Mode — Concrete Spec

**File:** `.github/chatmodes/endpoint-scaffolder.chatmode.md`
**Name surfaced in Copilot Chat:** `Endpoint Scaffolder`
**Tools allow-list:** `codebase`, `editFiles`, `runCommands`, `findTestFiles` (constrain — no web search, no GitHub tools — so it stays focused).

**File contents (learner authors this in the lab):**

```markdown
---
description: "Scaffold a new FastAPI endpoint in the Mergington activities app, with matching tests and minimal frontend wiring."
tools: ['codebase', 'editFiles', 'runCommands', 'findTestFiles']
---

You scaffold endpoints for the Mergington High School activities app
(`agents/` directory). Always follow the existing conventions:

1. **Backend:** add the route to `agents/backend/app.py`. Use the
   in-memory `activities` dict as the data source. Raise `HTTPException`
   with 404 for missing activities and 400 for validation failures —
   match the style of `signup_for_activity`.
2. **Tests:** add cases to `agents/tests/test_app.py` using
   `fastapi.testclient.TestClient`. Cover happy path + at least one
   error path. Run `pytest agents/tests/ -v` before reporting done.
3. **Frontend:** if the endpoint changes data the UI displays, update
   `agents/frontend/app.js` and `agents/frontend/index.html`. Keep
   vanilla JS — no frameworks, no build step.
4. **Plan first.** Before editing, list files + changes and wait for
   approval. Keep diffs minimal — do not refactor unrelated code.
5. **Out of scope:** do not touch `customize-copilot/` or
   `copilot-chat/`; those are other labs.
```

**Why this is defensible:** every team building features on a small service ends up with implicit "house rules" (where routes live, how errors are raised, what tests look like). Encoding them in a chatmode means the next 20 endpoints all look the same — that's the actual win, not "Copilot wrote a function for me."

---

## 4. Prompting Patterns to Teach (Agent-Mode-specific)

Each pattern = one-liner + before/after.

### P1 — "Plan first, then execute"
Force a plan-approve gate before any file is touched.

- **Before:** *"Add an unregister endpoint."* → agent dives in, edits 6 files, you scroll a 400-line diff.
- **After:** *"List the files you'll touch and the change in each. Stop. Wait for my approval before editing."* → agent returns a 5-bullet plan; you delete bullet 4 ("don't touch styles.css") and say "go."

### P2 — "Verify by running"
Explicitly tell the agent the success criteria is a green command, not "it looks right."

- **Before:** *"Add tests for signup."*
- **After:** *"Add tests for signup. Run `pytest agents/tests/ -v` and don't stop until all tests pass. If a test fails, fix the code or the test and re-run."*

### P3 — "Constrain the blast radius"
Name the files/dirs in-scope and explicitly out-of-scope.

- **Before:** *"Refactor the signup logic."*
- **After:** *"Refactor `signup_for_activity` in `agents/backend/app.py` only. Do not touch the frontend or other endpoints. Do not rename the function."*

### P4 — "Checklist prompts"
For multi-part work, give a numbered checklist; the agent will tick through it instead of inventing scope.

- **Before:** *"Make signup robust."*
- **After:** *"Update `signup_for_activity` so that: (1) duplicate emails return 400, (2) over-capacity returns 400, (3) the error messages mention the activity name, (4) tests in `tests/test_app.py` cover both."*

### P5 — "Show me the diff before committing"
Even with an agent, keep a human gate before `git commit`.

- **Before:** *"Commit your changes."*
- **After:** *"Stage your changes and run `git diff --staged`. Print the diff. Do not commit until I say so."*

---

## 5. Anti-patterns / Common Failure Modes

| Anti-pattern | What goes wrong | Recovery move |
|---|---|---|
| **"Just fix the app"** (vague mega-prompt) | Agent picks 3 random issues, none of them yours; runs for 4 minutes; produces sprawling diff | Stop the run. Re-prompt with a numbered checklist + named files (Pattern P4). |
| **No verification step** | Agent says "✅ Done", but `pytest` was never run; tests are red | Always include "run X and report the output" in the prompt (Pattern P2). |
| **Approving a plan you didn't read** | Agent edits files you didn't expect; hard to untangle later | Read every plan bullet. Reply with edits ("skip 3, do 1 and 2"). Use `git status` / `git diff` before continuing. |
| **Agent invents an API/library** | New endpoint uses `flask` or imports `pydantic.v2` features that aren't installed | Constrain tools/scope (P3) and pin: *"Use only packages already in `requirements.txt`."* |
| **Endless edit-test-edit loop on a flaky test** | Agent keeps "fixing" symptoms instead of root cause | Stop the agent. Read the failure yourself. Re-prompt: *"The test fails because X. Fix X specifically — do not change unrelated assertions."* |
| **Custom chatmode too vague** | "You write good code" → behaves identical to default chat | Chatmode must encode **specific file paths, naming, and tool allow-list** (see section 3). |

---

## 6. Open Questions for Book

1. **Chatmode file location & naming** — current docs reference `.github/chatmodes/<name>.chatmode.md`. Confirm this is still the path Copilot CLI / VS Code Insiders picks up at lab time, and whether `tools:` frontmatter array is honored or ignored. If the syntax has shifted, the Exercise 3 file needs updating.
2. **Does Agent Mode in the lab environment have terminal/run-command access enabled by default?** Exercise 1 and 2 depend on it (running `pip install` and `pytest`). If learners need to flip a setting, that's a pre-lab step Kaylee must script.
3. **MCP availability for stretch exercise** — is the GitHub MCP server preinstalled in the codespace/devcontainer, or do learners install it? If install is non-trivial, drop Exercise 4 entirely rather than half-teach it.
4. **"Approve plan" UX** — does Agent Mode have a built-in plan/approve step now, or do we rely on prompting the model to pause? Pattern P1 is written assuming the latter (prompted pause). Confirm.
5. **Auto-approve vs per-tool confirmation** — what's the default for `runCommands` / `editFiles`? If everything is auto-approved, Pattern P5 (gate before commit) becomes more important and we should call it out louder.
6. **Lab 2 overlap check** — Lab 2 covered "skills". The Exercise 3 chatmode is *adjacent* to skills but distinct (chatmode = mode-switch with tools+system-prompt; skill = invocable capability). Confirm Kaylee is comfortable drawing that line in the lab narrative so learners don't feel déjà vu.

---

**End of design.** Ready for Kaylee to turn into lab steps once Open Questions are answered.


---

## Active Decisions Archive (2026-04-20 to 2026-04-21)

# Lab 3 — MCP Block Proposal (consume + create)

**Author:** Book (Copilot Expert)
**Date:** 2026-04-20
**Requested by:** Geronimo Basso
**Spine:** B — Agent loop → Permission levels → MCP server integration → Custom agents
**Budget for this block:** ~25 min of the 90-min lab

**Reference repo studied:**
[`Geronimo-Basso/github-copilot-workshops-labs-python` → `lab-06-mcp/`](https://github.com/Geronimo-Basso/github-copilot-workshops-labs-python/tree/main/lab-06-mcp).
Single file in that lab: [`lab-06-mcp/README.md`](https://github.com/Geronimo-Basso/github-copilot-workshops-labs-python/blob/main/lab-06-mcp/README.md) (no separate `server.py` / `client.py` / `.vscode` artifacts committed — learner authors them inline).

---

## 1. What the reference lab teaches (5-bullet summary)

- **Scope:** end-to-end MCP — protocol concepts, build a Python `FastMCP` server, write a Python stdio client, register it in VS Code, and then consume two pre-built MCPs (Playwright, Microsoft Learn). Source: README §1–§9 + Part 2 A/B.
- **Structure:** Part 1 = "build your own" (sections 1–9), Part 2 = "use existing MCPs" (Part A Playwright, Part B Microsoft Learn). README §3–§8 walk through `server.py` and `client.py` line-by-line; §9 covers `.vscode/settings.json` + `.vscode/mcp.json` registration.
- **What learner builds:** a `FastMCP("Demo")` server exposing `add` / `subtract` / `multiply` / `divide` tools and a `greeting://{name}` resource (README §3–§4), plus a stdio Python client that lists tools/resources and invokes them (README §7–§8).
- **What learner consumes:** Playwright MCP via `npx @playwright/mcp@latest` to scrape NBA standings into JSON across 3 progressively richer prompts (README Part 2 §A, Goals 1–3); and Microsoft Learn MCP for "search Microsoft docs" prompts (README Part 2 §B).
- **Total time estimate:** ~75–90 min if done end-to-end (build server ~20, client ~15, VS Code registration ~10, Playwright 3-goal scrape ~25, MS Learn prompts ~10). **3× over our 25-min budget** — must be cut hard.

---

## 2. What's reusable for Lab 3

| Piece | Source | How we use it |
|---|---|---|
| `FastMCP` quick-start scaffold (3 lines to a running server) | README §3 | Direct lift as the skeleton of `agents/mcp/activities_server.py`. |
| `@mcp.tool()` decorator pattern with typed args + docstring | README §4 (`add(a:int,b:int)->int`) | Pattern for `list_activities()` and `get_signups_count(activity:str)`. |
| `.vscode/mcp.json` stdio server registration block | README §9.4 | Copy structure verbatim, swap `command`/`args` to point at our venv + `agents/mcp/activities_server.py`. |
| `.vscode/settings.json` `chat.mcp.discovery.enabled: true` line | README §9.2 | Lift as-is — required for VS Code to pick up `mcp.json`. |
| "Open mcp.json → click ▶ → ask Copilot Chat to use the tool" UX flow | README §9.5 | Reuse the exact 4-step instruction; it's the cleanest demo we've seen. |
| Prompt phrasing pattern: *"Use the `<tool>` tool to ..."* | README §9.5–§9.6 | Add to Kaylee's prompt examples — disambiguates intent so the agent actually invokes the MCP server vs. answering from memory. |
| Microsoft Learn MCP install pointer | README Part 2 §B step 1 (`https://github.com/mcp/microsoftdocs/mcp`) | Fallback "consume" option if Geronimo wants no-binary, no-API-key, fully cross-platform. |

---

## 3. What's NOT a fit (and why)

- **The `client.py` Python client (README §7–§8).** Out of scope for Lab 3 — our learner is a Copilot user, not an MCP host author. The Copilot Chat UI is the client. Including this would burn ~15 min teaching `stdio_client` / `ClientSession` plumbing the learner will never write again.
- **The Playwright MCP NBA scraping exercise (Part 2 §A, Goals 1–3).** Cool but heavy: needs `npx`, downloads Chromium, runs ~25 min, demonstrates *web automation*, not the MCP capability we want to highlight (giving the agent context about *our codebase / app*). Stack mismatch with our FastAPI activities app.
- **Math tools (`add` / `subtract` / `multiply` / `divide`).** Pedagogically fine but a missed opportunity — they don't demonstrate *why MCP matters*. The agent can already do arithmetic. Replace with tools that expose **data the agent cannot otherwise see** (the in-memory `activities` dict).
- **The `greeting://{name}` resource (README §4).** Resources are a second MCP primitive worth knowing, but in 25 min we can only land *tools* properly. Mention in a one-line "what we skipped" callout, not in the exercise.
- **Microsoft Learn MCP prompt set (Part 2 §B §3).** The prompts ("Azure Functions end-to-end", "How does Copilot work") are off-topic for an activities-app lab. If we use MS Learn MCP at all, it's as the install target, not for these prompts.
- **`mcp dev server.py` Inspector (README §5).** Nice debugging aid for builders, but adds a tab/port/token dance we don't have time for. Use plain `mcp run` (or let VS Code spawn it via `mcp.json`).

---

## 4. Recommended MCP block structure for Lab 3 (~25 min)

**Opinionated call: do BOTH consume and create, but heavily asymmetric — ~7 min consume, ~15 min create, ~3 min wrap.** Rationale: "create" is where the lasting insight lives (the learner now understands MCP isn't magic, it's a 30-line Python file). "Consume" alone leaves them treating MCP as a black-box marketplace. Doing only "create" misses the fact that 90% of real-world MCP usage is `npm i @some/mcp`. Asymmetric split reflects relative novelty.

### Block layout (25 min)

| Time | Phase | What happens |
|---|---|---|
| 0:00–0:03 | **Frame** | 60-sec MCP elevator pitch ("USB-C for AI tools" — borrowed from reference README §1). Show the two-sided picture: clients (Copilot) ↔ servers (capabilities). State the exercise: we'll *use* one, then *build* one. |
| 0:03–0:10 | **Consume** | Install one external MCP server (see §5 for choice). Register in `.vscode/mcp.json`. Run a single prompt against the agent that demonstrably needs the new tool. Done. |
| 0:10–0:23 | **Create** | Author `agents/mcp/activities_server.py` (~30 lines, see §6). Add a second entry to `.vscode/mcp.json`. Restart MCP servers. Ask Copilot Agent: *"How many students are signed up for Chess Club? Use the activities MCP server."* Observe the tool call. |
| 0:23–0:25 | **Wrap** | Callouts: resources vs. tools (we only did tools), MCP runs as a separate process (security boundary), permissions re-prompt for each MCP tool by default. Pointer to `https://github.com/mcp` for the registry. |

**If running long:** cut the consume phase to a 90-sec demo (Kaylee runs it, learners watch) and protect the create phase. The create phase is the load-bearing teaching moment.

---

## 5. Concrete server choice for the "consume" half

**Recommendation: Filesystem MCP** (`@modelcontextprotocol/server-filesystem`).

### Why it wins against the criteria

| Criterion | Filesystem | GitHub MCP | SQLite MCP | Playwright MCP |
|---|---|---|---|---|
| Setup <5 min | ✅ `npx` one-liner | ⚠️ needs PAT or OAuth | ✅ but needs a `.db` file we'd have to seed | ❌ Chromium download, ~3–5 min cold |
| Cross-platform | ✅ | ✅ | ✅ | ⚠️ heavyweight on Windows |
| No API keys | ✅ | ❌ requires GitHub token | ✅ | ✅ |
| Demonstrates capability bare agent lacks | ✅ scoped, sandboxed FS access outside the workspace folder | ✅✅ (best demo, but token cost) | ⚠️ we don't have a SQLite DB in `agents/` | ✅ but capability ≠ what our lab is about |

**Pick:** filesystem MCP, scoped to a *sibling* directory we create at lab start (e.g., `agents/sample-data/` containing 2–3 plain-text "policy" files like `school-policies.txt`). Prompt the agent with: *"Read `school-policies.txt` from the sample-data MCP server and tell me what the maximum club size policy is."* — this works because the agent doesn't have that file open in the editor, so it *must* go through the MCP tool.

**`.vscode/mcp.json` snippet (consume side):**
```jsonc
{
  "servers": {
    "school-files": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "${workspaceFolder}/agents/sample-data"]
    }
  }
}
```

**Fallback if `npx`/Node isn't guaranteed in lab env:** Microsoft Learn MCP (zero install, hosted) — but it teaches less because the "capability the agent lacks" is fuzzier.

---

## 6. Concrete server design for the "create" half

**File:** `agents/mcp/activities_server.py`
**Stack:** Python + `mcp[cli]` (matches the FastAPI stack already in `agents/`).
**Tools exposed:** `list_activities()`, `get_signups_count(activity: str)`.

### ~30-line code sketch

```python
"""Mergington activities MCP server — exposes the in-memory activities dict
to MCP-aware clients (e.g. GitHub Copilot Agent Mode)."""

from mcp.server.fastmcp import FastMCP

# Reuse the same in-memory data the FastAPI app uses.
# (In a real system this would query the same DB; for the lab,
# we import the dict directly to keep wiring trivial.)
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

### Registration in `.vscode/mcp.json` (additive — keeps the consume server)

```jsonc
{
  "servers": {
    "school-files": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "${workspaceFolder}/agents/sample-data"]
    },
    "mergington-activities": {
      "type": "stdio",
      "command": "${workspaceFolder}/.venv/bin/python",
      "args": ["-m", "agents.mcp_servers.activities_server"]
    }
  },
  "inputs": []
}
```

(Pattern lifted directly from reference README §9.4, with our paths.)

### Sample prompt for the demo
> *"Using the `mergington-activities` MCP server, list every activity and tell me which one is closest to full capacity."*

This forces a chain of tool calls: `list_activities()` → multiple `get_signups_count()` — visible in the Copilot Chat tool-call UI, which is the "aha" moment.

---

## 7. Files Kaylee will need to author or copy

- [ ] `agents/mcp/__init__.py` — empty, makes the package importable.
- [ ] `agents/mcp/activities_server.py` — ~30-line server (§6 above).
- [ ] `agents/sample-data/school-policies.txt` — 5–10 lines of plain text the consume-half prompt will read. (Plus 1 more file so "list directory" is non-trivial.)
- [ ] `.vscode/settings.json` — add `"chat.mcp.discovery.enabled": true` (lift from reference README §9.2).
- [ ] `.vscode/mcp.json` — both server entries (snippet in §6).
- [ ] `agents/requirements.txt` — append `mcp[cli]>=1.0` (verify the exact pin Kaylee/Jayne lock).
- [ ] Lab 3 markdown — 4 prompt examples ready to copy-paste:
  1. (consume) *"Read `school-policies.txt` from the school-files MCP server and summarise the participation rules."*
  2. (create — single tool) *"Use the mergington-activities MCP server to list all activities."*
  3. (create — chained) *"Which activity is closest to full? Use the mergington-activities MCP."*
  4. (negative case) *"Get the signup count for `Knitting Club`."* — demonstrates the `ValueError` path → permission re-prompt + graceful failure.
- [ ] Pre-lab check script (or doc step): `pip install "mcp[cli]"` inside the lab venv, plus `node --version` sanity check for the `npx` consume path.

---

## 8. Open question for Zoe

**Pacing concern:** the asymmetric split (~7 min consume, ~15 min create) assumes learners can `pip install "mcp[cli]"` *and* have Node.js for the `npx` filesystem MCP. If the lab environment doesn't guarantee Node, the consume half collapses to "watch Kaylee's demo" and the block becomes *create-only*, which leaves "MCP marketplace" undertaught. **Decision needed:** does Spine B's 25-min MCP slot assume a Node-capable environment, or do we redesign the consume half around a Python-based / hosted MCP (e.g. Microsoft Learn) to keep dependencies single-stack? This affects the locked plan's "tools required" line and Kaylee's pre-lab setup script.

---

## Sources

- Reference repo: <https://github.com/Geronimo-Basso/github-copilot-workshops-labs-python/tree/main/lab-06-mcp> (accessed 2026-04-20)
- Reference README (raw): <https://raw.githubusercontent.com/Geronimo-Basso/github-copilot-workshops-labs-python/main/lab-06-mcp/README.md> (accessed 2026-04-20)
- MCP registry / catalogue: <https://github.com/mcp> (per reference README Part 2 §A "Explore MCP offering")
- Filesystem MCP server package: `@modelcontextprotocol/server-filesystem` (npm)
- Prior Book inventory: `.squad/decisions/inbox/book-agent-mode-inventory.md` (MCP servers section, 2026-04-20)


### 2026-04-20T13:54: User directive — Lab folder convention
**By:** Geronimo Basso (via Copilot)
**What:** Each lab's README lives INSIDE its working-code folder, never in a sibling folder. Lab 1 = `copilot-chat/README.md`, Lab 2 = `customize-copilot/README.md`, Lab 3 = `agents/README.md` (NOT `agent-mode/README.md`). The folder name IS the lab name.
**Why:** User correction — captured for team memory so future labs follow the same pattern.


### 2026-04-20T10:28:09Z: User directive — Lab 3 spine selected
**By:** Geronimo Basso (via Copilot)
**What:** Lab 3 will follow Spine B (Book's recommendation): Agent loop in practice (multi-file edit + terminal + test iteration) → Permission levels (Default / Bypass / Autopilot) → MCP server integration → Custom agents (`.github/agents/*.agent.md`). Cloud Coding Agent is explicitly deferred to a future lab. River's "ship the half-finished app" exercises remain the hands-on substrate where they fit Spine B.
**Why:** User decision after reviewing Zoe / Book / River planning docs.


# Copilot Directive — Lab 3 Block 3 (MCP) revision

**From:** Geronimo Basso · **Date:** 2026-04-20

**Decisions locked:**

1. **Adopt Book's consume+create structure** for Block 3 (proposal in `book-mcp-block-proposal.md`). Supersedes the consume-only Block 3 in `zoe-lab3-locked-plan.md` §3 Exercise C.
2. **Consume half = OPTIONAL.** Use filesystem MCP via `npx`. Marked with a "⚠️ Optional — skip if Node.js is not available" callout. Learners without Node skip straight to the create half.
3. **Create half = REQUIRED.** Author `agents/mcp/activities_server.py` (~30-line Python `FastMCP` server, lifted from reference repo `lab-06-mcp` README §3–§4, §9.4). Register in `.vscode/mcp.json`. Drive from Agent.
4. **Reference repo:** Geronimo's `github-copilot-workshops-labs-python/lab-06-mcp` is the inspiration; lift snippets where Book flagged them as reusable.
5. **Pre-lab:** add `node --version` to the optional checklist; `pip install "mcp[cli]"` to the required checklist.

**Action:** Zoe to amend the locked plan; Kaylee writes against the amended version.


# Lab 3 — QA Walkthrough Report
**Verdict:** APPROVE WITH MINOR FIXES
**Reviewer:** Jayne
**Date:** 2026-04-20

## Summary
Lab 3 hits the locked plan on the nose: spine, exercises, frontmatter,
cuts, and format all line up with `zoe-lab3-locked-plan.md` and Book's
MCP proposal. One genuine blocker for Windows learners (the hard-coded
POSIX venv path in `.vscode/mcp.json`), but the fix is a 3-line callout
in Step 4 Activity C.2 — patchable in seconds, hence "MINOR FIXES" not
"REJECT". A handful of cross-platform friction items and a model-pin
risk to flag with Zoe round out the list.

## 🛑 Blockers (must fix before ship)

1. **Windows venv path in `.vscode/mcp.json` (file `.vscode/mcp.json:13`
   + `agent-mode/README.md:395–407`).** The registration hard-codes
   `${workspaceFolder}/.venv/bin/python`. On Windows that path doesn't
   exist — it's `${workspaceFolder}/.venv/Scripts/python.exe`. The lab
   never tells Windows learners to swap it. Result: `mergington-activities`
   silently fails to start and the load-bearing create half is dead.
   **Fix:** Add a one-line callout under Activity C.2 step 4 along the
   lines of:
   > 🪟 **Windows:** edit the snippet above to
   > `"command": "${workspaceFolder}/.venv/Scripts/python.exe"`. The
   > rest is identical.
   That's the entire patch. No code change required.

## ⚠️ Friction (fix soon, doesn't block)

1. **`rm -rf agents/tests` in the Step 2 mid-exercise revert
   (`agent-mode/README.md:191`).** Works in Git Bash / WSL / macOS /
   Linux. Fails in cmd.exe and PowerShell (where the equivalent is
   `Remove-Item -Recurse -Force agents/tests`). Add a parenthetical
   "(PowerShell: `Remove-Item -Recurse -Force agents/tests`)".

2. **`python3 -m venv .venv` in pre-lab (`agent-mode/README.md:54`).**
   Windows ships `python`, not `python3`. The activation line below it
   is correctly platform-split, but the venv-creation line isn't.
   Mirror the same pattern: show `python3` for macOS/Linux and
   `python` (or `py -3`) for Windows.

3. **Step 2 mid-exercise revert reverts `agents/requirements.txt`
   (`agent-mode/README.md:191`).** Wipes the `pytest` and `mcp[cli]`
   lines from the working tree — they remain in the venv so `pytest`
   keeps running, but a learner who later runs `pip install -r
   agents/requirements.txt` (e.g. on a fresh machine, in CI) will be
   missing those deps. Per Kaylee's flagged item #2, drop
   `agents/requirements.txt` from the `git checkout` so the revert is
   `git checkout agents/backend/app.py && rm -rf agents/tests`.

4. **Time arithmetic drifts ~10 min (`agent-mode/README.md:5,
   §2 of locked plan`).** Per-step badges sum to ~91 min of activity
   plus an unbudgeted "Congratulations" wrap, putting the wall clock
   at ~100 min vs the advertised 90. The locked plan's wrap allotment
   (9 min) isn't visibly broken out per-step. Either trim Step 4 to
   25 min (5+20) or be honest in the header that the lab is 90–100
   min. Doesn't break the lab; does set false expectations.

5. **`npx` first-run delay on the consume half
   (`agent-mode/README.md:333`).** Per Kaylee's flagged item #4 — the
   first `npx -y @modelcontextprotocol/server-filesystem` invocation
   downloads the package and can stall 5–15 s with no UI feedback.
   One-line "this may pause briefly the first time" calms learners
   who'd otherwise hit Stop.

## 💡 Suggestions (nice to have)

1. **`agents/__init__.py` and `agents/backend/__init__.py` don't
   exist.** The MCP server's `from agents.backend.app import
   activities` works today via PEP 420 implicit namespace packages,
   but it's fragile to future tooling assumptions. Consider shipping
   empty `__init__.py` files at both levels for belt-and-braces. Not
   required — current state passes.

2. **MCP server cwd assumption isn't called out.** `python -m
   agents.mcp_servers.activities_server` only resolves when the launcher's
   cwd is the workspace root. VS Code does this by default for
   stdio MCP servers, but if a learner ever runs the command
   directly from a different shell they'll get an
   `ImportError: No module named agents`. One sentence in the
   "Confirm the package skeleton exists" callout would inoculate
   them.

3. **`.gitignore` doesn't exclude `.venv/`.** Out of scope for this
   lab, but the pre-lab will have learners create `.venv/` at the
   workspace root and a stray `git add .` will hoover it in. Worth
   a fast follow-up.

## Kaylee's flagged items — verdict on each

1. **Workspace-root venv assumption is unambiguous.** **Confirmed
   non-issue** — pre-lab step 2 says "at the workspace root" plainly.

2. **Step 2 revert nukes `agents/requirements.txt` working-tree
   additions.** **Escalated to FRICTION** (item ⚠️ 3 above). Adopt
   her suggested fix: drop `agents/requirements.txt` from the
   `git checkout`.

3. **Windows venv path in `.vscode/mcp.json`.** **Escalated to
   BLOCKER** (item 🛑 1 above). The lab's load-bearing exercise
   silently fails on Windows.

4. **`npx` first-run delay.** **Confirmed FRICTION** (item ⚠️ 5).
   Add the one-line note.

5. **`model: gpt-5` pin.** **Escalated to Zoe.** Not Jayne's call —
   this is a seat-availability question. If `gpt-5` isn't on the
   default learner seat, Step 5 errors out the moment they invoke
   the custom agent. Zoe needs to confirm before shipping or
   downgrade to a model that's guaranteed available (e.g.
   `gpt-4.1`).

6. **Handoff button only renders when Plan considers its response
   "complete".** **Confirmed non-issue** — the prompt at line 517 is
   tight and unambiguous; in practice Plan produces a structured
   plan, not a clarifying question. Worth a sanity run on lab day,
   not a doc change.

7. **`.vscode/` now version-controlled, not git-ignored.**
   **Confirmed non-issue.** Locked plan §3 explicitly ships these
   files; Kaylee's reading is correct.

## If REJECT: who should revise?

N/A — this is APPROVE WITH MINOR FIXES. **Kaylee** can apply the
1 blocker patch (one-line Windows callout in Activity C.2 step 4)
and the four friction fixes herself; none of them require
re-architecting anything. If Zoe's resolution on item 5 (the
`model: gpt-5` pin) requires changing the model, that's a Zoe
decision Kaylee then implements — not a revision.


# Lab 3 D.4 Playwright MCP Addition

**Date:** 2026-04-20T22:00Z  
**Author:** Kaylee (lab content writer)  
**Status:** Shipped to `agents/README.md`

## Summary

Added **D.4 — Browser automation with the Playwright MCP (OPTIONAL)** to `agents/README.md` as a new sub-section under Exercise D, positioned between D.3 (Microsoft Learn MCP, ends at line 668) and the "Wrap: What we skipped" section (previously line 670, now line 777).

## What Was Added

### New Content (D.4 Section)

1. **Framing paragraph** — Contrasts D.4 with D.1/D.2/D.3 by highlighting Playwright MCP as a completely different MCP shape: **stateful browser automation** (not file access, not docs research). Lists concrete use-cases:
   - Scaffolding end-to-end tests
   - Scraping dynamic JavaScript-rendered sites
   - Generating screenshots for documentation/PRs
   - Reproducing UI bugs with exact browser state
   - Automating repetitive web flows

2. **Install step** — Points to `https://github.com/mcp/microsoft/playwright-mcp` and shows `.vscode/mcp.json` snippet:
   ```json
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
   Includes note about browser binary download delay (~200MB, 30–60 seconds first-run).

3. **Verification step** — Command Palette → MCP: List Servers → confirm `playwright` is started (mirrors D.3 pattern).

4. **Screenshot goal** — `<details>` prompt block asking Agent to:
   - Navigate to `https://www.nba.com/standings` using Microsoft Edge (headed)
   - Handle consent banners
   - Scroll full page
   - Save full-page PNG to `./artifacts/01_open_standings.png`
   - Return status JSON with page title, URL, table count, screenshot path

5. **Data extraction goal** — `<details>` prompt block asking Agent to:
   - Extract NBA standings table to JSON array
   - Normalize team names
   - Parse numbers as numbers
   - Save to `./data/standings_raw.json`

6. **Optional multi-page enrichment** — Brief mention of Goal 3 (visit top-N team pages, extract arena/coach, merge) with a one-liner prompt suggestion. Does not paste full prompt; points readers at the pattern.

7. **Tips table** (3 rows):
   | Goal | Add These Phrases |
   |------|-------------------|
   | Reliability | `wait for network idle`, `wait for selector`, `accept any cookie banner` |
   | Reproducibility | `headed`, `Microsoft Edge`, `maximize window`, `save screenshot to ./artifacts/` |
   | Structured output | `return JSON with fields...`, `parse numbers as numbers`, `normalize team names` |

8. **Closing callout** — ✅ pattern mirroring D.3: "the Playwright MCP tool calls render inline (navigate → screenshot → evaluate), an actual PNG file lands in `./artifacts/`, and structured JSON in `./data/`. You just gave Agent a real browser."

### Updates to Existing Sections

- **TOC (line 26):** Added entry after D.3:
  ```markdown
  - [D.4 — Browser automation with the Playwright MCP (OPTIONAL)](#d4--browser-automation-with-the-playwright-mcp-optional)
  ```

- **Congratulations Step 5 (line 795):** Updated to mention D.4:
  > (Optionally) consumed the filesystem MCP server (D.1), **built** your own `mergington-activities` MCP server in ~30 lines of Python and watched Agent chain `list_activities()` → `get_signups_count(...)` calls (D.2), installed the Microsoft Learn MCP from a registry to research official Microsoft documentation with grounded citations (D.3), **and pointed Agent at a real Chromium browser via the Playwright MCP for screenshots and structured scraping (D.4)**.

- **Wrap "What we skipped" (line 780):** Removed `Playwright` from the parenthetical list:
  > explore [`https://github.com/mcp`](https://github.com/mcp) for hundreds of community servers (GitHub, Sentry, Postgres, ...).
  
  Previously: `(GitHub, Sentry, Postgres, Playwright, ...)`

## Source Material

Adapted from `extra/github-copilot-workshops-labs-python/lab-06-mcp/README.md` lines 289–404 (Lab 06 Part A — Playwright MCP, Goals 1–3).

## Key Choices

### Screenshot Target URL

**Choice:** Kept `https://www.nba.com/standings` from the source material.

**Rationale:** 
- Stable, public, JavaScript-heavy page ideal for demonstrating Playwright's value over `curl`
- The structured-data-extraction narrative (NBA standings table → JSON) is concrete and relatable
- Alternative considered: `https://github.com/features/copilot` (more GitHub-adjacent) but loses the table-scraping angle

### Prompt Block Style

Used `<details><summary>Show Prompt</summary>` blocks (matching D.3) instead of the badge-style `> ![Static Badge]...` used in D.2. This keeps consistency within Exercise D's registry-MCP sections (D.3 and D.4 both consume external MCPs; both use collapsible prompts).

## Constraints Met

✅ NO time estimates anywhere (no `~Xmin`, no `(N minutes)`)  
✅ Matches OPTIONAL/REQUIRED tag style of D.1 and D.3  
✅ Heading level: `#### D.4 — ...`  
✅ Preserves repo conventions (badge URLs, no time estimates, theory-first structure)  
✅ All D.1/D.2/D.3 sections untouched  
✅ TOC updated  
✅ Congratulations table updated  
✅ Wrap "What we skipped" updated (Playwright removed from skip list)

## Verification

```bash
# Confirm D.4 anchor exists
grep -n "d4--browser-automation" agents/README.md
# Result: line 26 (TOC)

# Confirm D.4 section added
grep -n "D.4.*Browser automation" agents/README.md
# Result: line 26 (TOC), line 671 (section heading)

# Confirm Playwright removed from Wrap skip list
grep -n "Playwright" agents/README.md | grep -i "skip\|wrap"
# Result: no matches (Playwright no longer in "what we skipped")
```

## Handoff Notes

- D.4 is OPTIONAL (requires Node.js / npx, like D.1)
- Section lands at line 671, right after D.3's closing callout (line 668)
- No dependencies on other sections — can be skipped independently
- All existing sections (A, B, C, D.1, D.2, D.3) intact


# Kaylee → Jayne · Lab 3 Handoff

**Date:** 2026-04-20
**Author:** Kaylee (Lab Builder)
**Status:** Lab 3 fully authored, ready for QA walkthrough.

## Files created

**Lab document:**
- `agent-mode/README.md` — full Lab 3 markdown, mirrors `customize-copilot/README.md` structure (TOC, `## Step N`, `### 📖 Theory` / `### Activity`, prompt badges, "Congratulations 🎉" + "What's Next?" close).

**Supporting code/config:**
- `agents/mcp/__init__.py` — empty (makes `agents/mcp/` an importable package).
- `agents/mcp/activities_server.py` — ~30-line `FastMCP` server, **verbatim** from Book §6 code sketch.
- `agents/sample-data/school-policies.txt` — 7 plain-text participation rules for the optional consume half.
- `.vscode/settings.json` — created (did not previously exist); single key `"chat.mcp.discovery.enabled": true`.
- `.vscode/mcp.json` — created (did not previously exist); both `school-files` and `mergington-activities` server entries per Book §6 snippet.
- `agents/requirements.txt` — appended `mcp[cli]>=1.0` and `pytest` (existing 4 lines preserved).

## Things Jayne should pay extra attention to during walkthrough QA

1. **Step 2 / Exercise A — terminal + pytest loop.**
   The lab assumes `python3 -m venv .venv` at the **workspace root** (not inside `agents/`). The MCP server registration in `.vscode/mcp.json` hard-codes `${workspaceFolder}/.venv/bin/python`. If you create the venv anywhere else, Step 4 silently breaks. Verify the README pre-lab step is unambiguous on this.

2. **Step 2 mid-exercise revert command.**
   The plan-first re-prompt callout instructs `git checkout agents/backend/app.py agents/requirements.txt && rm -rf agents/tests`. **`agents/requirements.txt` is now versioned with `mcp[cli]>=1.0` and `pytest` already added by this lab branch.** Reverting it during Exercise A will *remove* the deps the learner just installed — but only in the working tree, not in the venv, so `pytest` still runs. Confirm this doesn't trip up learners; if it does, change the revert to `git checkout agents/backend/app.py && rm -rf agents/tests` only.

3. **Step 4 — Windows venv path.**
   `.vscode/mcp.json` uses `${workspaceFolder}/.venv/bin/python` (POSIX). Windows learners need `${workspaceFolder}/.venv/Scripts/python.exe`. **The lab does not currently call this out.** Either add a one-line Windows note in Activity C.2 step 4, or rely on Jayne flagging it during platform sweeps.

4. **Step 4 consume half — `npx` first-run delay.**
   First invocation of `@modelcontextprotocol/server-filesystem` via `npx -y` downloads the package (~5–15 s, depending on network). Worth a "this may take a moment the first time" note if you hit a long pause during walkthrough.

5. **Step 5 frontmatter — `model: gpt-5`.**
   Pinned per the locked plan. If the lab environment doesn't have `gpt-5` enabled for the learner, the custom agent will error or fall back. Confirm the pinned model is available in the standard lab seat; if not, escalate to Zoe before changing.

6. **Step 5 handoff button rendering.**
   The "Implement this plan" handoff button only appears after a Plan response that the model considers "complete". If Plan asks a clarifying question instead of producing a plan, the button won't render. The prompt is written to be unambiguous, but worth a sanity run.

7. **`.vscode/settings.json` is now version-controlled.**
   Previously the repo had no `.vscode/` folder. New file. `.gitignore` does not currently exclude `.vscode/` — confirm with the team that committing both files is intended (it is, per the locked plan §3).

## Open questions for Zoe

None. The locked plan was internally consistent and I implemented it as written. No deviations, no contradictions found between the locked plan, Book's MCP proposal, and Book's Agent Mode inventory (the latter referenced via `.squad/decisions.md` since the standalone `book-agent-mode-inventory.md` file does not exist in `.squad/decisions/inbox/` — content is in `.squad/decisions.md` under "## Lab 3 Planning (2026-04-20)" §2–§6, which I treated as authoritative).

## Cuts honored (per locked plan §4)

- Cloud Coding Agent → mentioned only as one-line "Lab 4" teaser in What's Next.
- CLI background agents → not mentioned.
- MCP resources → mentioned in Step 4 wrap as "what we skipped" + as a What's Next teaser.
- MCP host/client authoring → mentioned in Step 4 wrap as one line.
- Subagents, hooks, BYOK, third-party agents → not mentioned.
- Edit mode → single retraction line in Step 1 + one row in the "naming has shifted" table at the top.
- AGENTS.md deep-dive → one disambiguation line in Step 5 theory.

## Voice / format checks

- All prompts are copy-pasteable, fenced as `prompt`, prefixed with the standard `Static Badge` shields.io image URL lifted from Lab 2.
- Every Activity ends with a "✅ You should now see..." checkpoint.
- Time estimates per step come from locked plan §2.
- Pre-lab section splits Required vs Optional, with `node --version` clearly gated as Optional.


# Lab 3 — Microsoft Learn MCP Addition + Time Estimate Removal

**Date:** 2026-04-20  
**Agent:** Kaylee  
**Requester:** Geronimo

## What Changed

Two independent changes to `agents/README.md`:

### Change 1: Added D.3 — Microsoft Learn MCP

**What was added:**

- New sub-section **D.3 — Use an off-the-shelf MCP from a registry (Microsoft Learn MCP)** inserted between current D.2 (build your own) and the "Wrap: What we skipped" section.
- D.3 is marked `(OPTIONAL)` since it requires installing an external MCP from a registry.
- TOC updated with new D.3 entry.
- Congratulations Step 5 expanded to reference all three D sub-activities (D.1 filesystem, D.2 build, D.3 registry).

**Content structure:**

1. **Framing opener** — explains this is the third MCP pattern (consume local → build → use registry), emphasizes real-world relevance, notes Microsoft Learn MCP grounds answers in official docs with citations instead of training data alone.
2. **Install step** — points to `https://github.com/mcp/microsoftdocs/mcp#-installation--getting-started` for IDE-specific install. Notes that for VS Code users, it's typically one-click from registry.
3. **Verify step** — Command Palette → MCP: List Servers → confirm `microsoft-learn` appears and is started.
4. **Research prompt** — one verbatim prompt from source material: *"I need to understand MCP in GitHub Copilot end-to-end (agent mode, registries, server setup). Search Microsoft docs."* Wrapped in the lab's standard `> ![Static Badge](...)` + ```prompt``` fence pattern.
5. **Follow-up citation prompt** — *"Cite the exact Microsoft Docs URLs you used."* Demonstrates the grounded-research angle.
6. **Tip table** — 3-row table of phrases that improve responses (Force official sources, Depth, Validation). Adapted from source material's "Tips for Higher-Quality Responses" table.
7. **✅ callout** — learners should see MCP tool calls inline, answer grounded in fetched docs, and (after follow-up) actual `learn.microsoft.com` URLs cited.

**Source material:** `extra/github-copilot-workshops-labs-python/lab-06-mcp/README.md` lines 408–477 (Part B "Using the Microsoft Learn MCP").

**Why D.3 is OPTIONAL:**

- Requires installing an external MCP from a registry (extra step).
- Different shape from D.1/D.2 — not about building or configuring local servers, but about using a maintained third-party one.
- D.1 and D.2 already cover the core MCP concepts (consume + create). D.3 shows the most common production pattern but isn't load-bearing for the lab's learning objectives.

---

### Change 2: Removed ALL Time Estimates

**What was stripped:**

- Every `(≈XX min)`, `(~XX min)`, `(REQUIRED, ~15 min)`, `(OPTIONAL, ~7 min)` annotation throughout the README.
- Specific locations:
  - TOC: Part 1, Exercises A/B/C/D entries
  - Headings: `## Part 1 — Theory (≈18 min)` → `## Part 1 — Theory`
  - Headings: `### Exercise A — Agent loop in practice (≈20 min)` → `### Exercise A — Agent loop in practice`
  - Headings: `### Exercise B — Permission levels (≈8 min)` → `### Exercise B — Permission levels`
  - Headings: `### Exercise C — Build a custom-agent toolbox (≈30 min)` → `### Exercise C — Build a custom-agent toolbox`
  - Headings: `### Exercise D — Consume + create an MCP server (≈25 min)` → `### Exercise D — Consume + create an MCP server`
  - Headings: `#### D.1 — Consume the filesystem MCP server (OPTIONAL, ~7 min)` → `#### D.1 — Consume the filesystem MCP server (OPTIONAL)`
  - Headings: `#### D.2 — Build your own MCP server (REQUIRED, ~15 min)` → `#### D.2 — Build your own MCP server (REQUIRED)`
  - Internal link: Exercise D reference in Pre-Lab Setup step 6
  - Any other time mentions in prose (verified via grep — none found)

**What was preserved:**

- `OPTIONAL` and `REQUIRED` tags in D.1, D.2, and D.3 headings — only the `~XX min` portion was removed.
- Non-time uses of `~`:
  - `~30-line server` (line count, appears in §What You'll Learn, §1.5 Theory, D.2 heading prose, D.2 code snippet description, Congratulations Step 5)
  - `~5–15 seconds` (download duration in D.1 npx delay note)

**Rationale:**

Geronimo's instruction: *"if the lab takes more than 90 minutes it's okay"* → interpretation: remove the time budget entirely, not try to keep it at 90. The lab is now time-agnostic — learners work at their own pace.

**Verification:**

- Grepped for `min)`, `≈`, `~[0-9]` patterns — zero time-estimate hits remain.
- Verified `~30-line` and `~5–15 seconds` still present (correct — they're not lab-time estimates).

---

## Judgment Calls

1. **D.3 marked OPTIONAL** — aligns with D.1 (also OPTIONAL, also about consuming). D.2 remains REQUIRED as the load-bearing create half.
2. **D.3 framing** — explicitly called out as "different shape from D.1/D.2" in the opener to manage learner expectations.
3. **Tip table condensed to 3 rows** — source material had 4 rows; I kept the 3 most actionable (Force official sources, Depth, Validation) per the brief's "3 rows max" instruction.
4. **Congratulations Step 5 expanded** — now explicitly calls out D.1, D.2, and D.3 by name to reinforce the three-pattern framing.

---

## Preservation Verified

- ✅ Theory-first structure (§1.1–1.5) intact
- ✅ Custom Agents → MCP order intact in Theory and Hands-on
- ✅ Existing 3 custom agents (C.1/C.2/C.3) untouched
- ✅ Existing D.1 (filesystem MCP, OPTIONAL) and D.2 (build your own, REQUIRED) untouched — only D.3 added after D.2
- ✅ All 5 prior Jayne QA fixes intact (Windows venv path, PowerShell `rm -rf`, python3/python pre-lab split, revert command, npx delay note)
- ✅ `model: gpt-5` in custom agent frontmatter preserved (not touched by this pass)
- ✅ OPTIONAL/REQUIRED tags in D.1/D.2/D.3 preserved — only `~XX min` stripped

---

## Files Modified

- `agents/README.md` — added D.3 section, updated TOC, updated Congratulations Step 5, stripped all time estimates
- `.squad/agents/kaylee/history.md` — appended entry under "## Learnings"
- `.squad/decisions/inbox/kaylee-lab3-ms-learn-mcp-and-time-removal.md` — this document


# Lab 3 — Jayne's QA Fixes Applied

**From:** Kaylee
**To:** Zoe (final review)
**Date:** 2026-04-20
**Status:** ✅ Ready for final review

All 5 in-scope fixes from `jayne-lab3-qa.md` landed in
`agent-mode/README.md`. No support files touched. No structural changes
to the locked plan. Step 5 `model: gpt-5` pin left as-is per Geronimo's
explicit confirmation.

## Fixes applied

| # | Severity | File:line (post-patch) | What changed |
|---|----------|------------------------|--------------|
| 1 | 🛑 BLOCKER | `agent-mode/README.md:412` | Added Windows callout under Step 4 Activity C.2 step 4 telling learners to swap `command` to `${workspaceFolder}/.venv/Scripts/python.exe`. |
| 2 | ⚠️ Friction | `agent-mode/README.md:192` | Added PowerShell variant to the Step 2 mid-exercise revert (`Remove-Item -Recurse -Force agents/tests`). |
| 3 | ⚠️ Friction | `agent-mode/README.md:54–55` | Split the venv-creation line in pre-lab into macOS/Linux (`python3 -m venv .venv`) and Windows (`python -m venv .venv` / `py -3 -m venv .venv`), mirroring the activation block below it. |
| 4 | ⚠️ Friction | `agent-mode/README.md:192` | Dropped `agents/requirements.txt` from the Step 2 revert's `git checkout`. Now `git checkout agents/backend/app.py && rm -rf agents/tests` (PowerShell variant included per fix #2). |
| 5 | ⚠️ Friction | `agent-mode/README.md:340` | Added one-line `npx` first-run delay note before the consume-half prompt block in Step 4. |

## Skipped (per task brief)

- **Jayne friction #4 (time arithmetic, ~100 min vs 90 min header).**
  Per-step badges I authored are descriptive; locked plan §2 budget
  governs. Not changing without Zoe's call. Flagging here for visibility
  but I don't think it's worth a re-cut — the wrap is genuinely short
  and learners overshoot lab budgets routinely.
- **All 💡 SUGGESTIONS** in Jayne's report (`__init__.py` files, MCP
  cwd callout, `.gitignore .venv/`). Out of scope for this patch round.
- **Step 5 `model: gpt-5` pin.** Geronimo confirmed `gpt-5` is fine on
  the learner seat. Left unchanged.

## Verification

Re-read each patched section after edit:
- Pre-lab venv block reads naturally; matches activation pattern.
- Step 2 revert one-liner is dense but parses; PowerShell variant
  inline-parenthetical, no new line break.
- Step 4 consume `npx` note sits between the "send:" cue and the
  prompt block — learners will see it before they hit submit.
- Step 4 create Windows callout sits directly under the JSON snippet,
  same indent level as the surrounding numbered list — flows.
- No support-file changes (`.vscode/mcp.json`, `activities_server.py`,
  `requirements.txt` all untouched).

Lab is ready for Zoe's final review.


# Lab 3 — Relocated to `agents/README.md`

**From:** Kaylee
**To:** Zoe (final review)
**Date:** 2026-04-20
**Status:** ✅ Move complete · all 5 QA patches present · ready for Zoe final review

## Move

- Source: `agent-mode/README.md` (561 lines, untracked)
- Destination: `agents/README.md`
- Method: plain `mv` (file was not under version control, so `git mv`
  failed with "not under version control"); then `rmdir agent-mode/`.
- Pre-move clobber check: `agents/README.md` did **not** exist. The
  pre-existing `agents/README-agents.md` is a different filename
  (single-line URL stub, untracked) — left untouched, no collision.
- `agent-mode/` directory removed.

## Path-reference fixes inside the moved README

Per Geronimo's directive, kept workspace-rooted paths in prose and in
all shell commands the learner runs from the workspace root
(`pip install -r agents/requirements.txt`,
`python -m agents.mcp_servers.activities_server`, `pytest agents/tests/ -v`,
`git checkout agents/backend/app.py`, etc.). Only the two markdown
hyperlink targets that used `../agents/...` (which assumed the README
was a sibling of `agents/`) were rewritten to resolve from the new
location:

| Line | Before | After |
|------|--------|-------|
| 139  | `[`signup_for_activity`](../agents/backend/app.py)` | `[`signup_for_activity`](./backend/app.py)` |
| 363  | `[`agents/mcp/activities_server.py`](../agents/mcp/activities_server.py)` | `[`agents/mcp/activities_server.py`](./mcp/activities_server.py)` |

Display text on link 363 deliberately keeps the workspace-rooted
`agents/mcp/activities_server.py` label so the learner sees the
"real" path; only the link target is relativised so the click works.

No other path strings touched. No code or support files modified.

## Jayne's 5 QA patches — verification post-move

All present and unchanged by the relocation:

| # | Severity | Location in `agents/README.md` | Verified |
|---|----------|-------------------------------|----------|
| 1 | 🛑 BLOCKER | line 412 — Windows callout under Step 4 Activity C.2 step 4 (`${workspaceFolder}/.venv/Scripts/python.exe`) | ✅ |
| 2 | ⚠️ Friction | line 192 — PowerShell variant on Step 2 revert (`Remove-Item -Recurse -Force agents/tests`) | ✅ |
| 3 | ⚠️ Friction | lines 54–55 — pre-lab venv split into `python3` (macOS/Linux) and `python` / `py -3` (Windows) | ✅ |
| 4 | ⚠️ Friction | line 192 — Step 2 revert no longer touches `agents/requirements.txt`; now `git checkout agents/backend/app.py && rm -rf agents/tests` | ✅ |
| 5 | ⚠️ Friction | line 340 — `npx` first-run delay note (`~5–15 seconds`) above the consume-half prompt | ✅ |

Step 5 `model: gpt-5` pin: **left as-is per Geronimo's explicit
confirmation.**

## Ready for Zoe final review

Lab 3 lives at `agents/README.md`, conforms to the
"README-inside-working-code-folder" convention (matches
`copilot-chat/README.md`, `customize-copilot/README.md`), and carries
all approved QA fixes. Handing back to Zoe for final sign-off.


# Lab 3 restructure — status note

**From:** Kaylee
**Date:** 2026-04-20T17:30Z
**Scope:** `agents/README.md` only. Lab 1 (`copilot-chat/README.md`) and Lab 2 (`customize-copilot/README.md`) untouched.

## What changed

Restructured Lab 3 from interleaved (Step 1 theory + activity, Step 2 theory + activity, …) to theory-first:

- **Part 1 — Theory (≈18 min)** — sections 1.1–1.5 hold every theory block, in original order.
- **Part 2 — Hands-on** — Exercises A–D map 1:1 to the activity bodies of former Steps 2–5.
- TOC rewritten to match.
- Top time-budget line updated: `📚 Theory: ~18 min upfront · 🧪 Hands-on: ~68 min`.
- The tiny "Find the three pickers" click-through from former Step 1 lives at the end of section 1.1 as `Quick orientation` (no Exercise 0 invented — it's a 30-second visual check that pairs with the picker theory).

## Content preservation

- All theory bodies copied verbatim; only the `### 📖 Theory: …` sub-headings were dropped (now numbered subsections of Part 1).
- All activity bodies copied verbatim — prompts, code blocks, callouts, ✅ checkpoints, tables, all intact.
- All 5 Jayne fixes verified post-move (grep-confirmed): Windows venv callout in C.2 step 4, PowerShell `Remove-Item` variant in Exercise A mid-callout, `python3` vs `python` split in pre-lab step 2, dropped `agents/requirements.txt` from the revert command (still absent), `npx` first-run delay note in C.1 step 3.
- "Congratulations" recap table kept as-is per the task brief, even though it still references "Step 1–5" — that's the recap, not a navigation aid.

## Cross-references rewritten

| Where | Old | New |
| --- | --- | --- |
| Pre-Lab step 6 | `[Step 4](#step-4-mcp--consume-one-then-build-one)` | `[Exercise C](#exercise-c--consume--create-an-mcp-server-25-min)` |
| §1.1 closing paragraph | "Steps 2–4 … Step 5 … Step 3" | "Exercises A–C … Exercise D … Exercise B" |
| Exercise A mid-callout | "(Step 5 will show the alternative…)" | "(Exercise D will show the alternative…)" |
| Exercise B final ✅ | "so `app.py` is clean for Step 4" | "so `app.py` is clean for Exercise C" |
| Exercise C.2 step 1 | "added to `agents/requirements.txt` in Step 2" | "added to `agents/requirements.txt` in Exercise A" |

No other intra-document `Step N` references remain in the body.

## Time budget

Theory ≈18 min + Exercises A(20) + B(8) + C(25) + D(15) = 68 min hands-on + ~4 min intro/wrap ≈ **90 min**. Top header reflects this.

## Files touched

- `agents/README.md` — full structural rewrite (no content rewrites).


# Lab 3 — Swap (Custom Agents ⇄ MCP) + Decision-table trim

**Date:** 2026-04-20T18:15Z
**Author:** Kaylee
**Requested by:** Geronimo

## Change 1 — Custom Agents now precede MCP

### Sections moved (verbatim, only headings renumbered)

| Was | Now | Content |
| --- | --- | --- |
| `### 1.4 Model Context Protocol (MCP)` | `### 1.5 Model Context Protocol (MCP)` | unchanged body |
| `### 1.5 Custom agents` | `### 1.4 Custom agents` | unchanged body |
| `### Exercise C — Consume + create an MCP server (≈25 min)` | `### Exercise D — Consume + create an MCP server (≈25 min)` | unchanged body; sub-headings `#### C.1` → `#### D.1`, `#### C.2` → `#### D.2`; one in-prose ref `Activity C.2` → `Activity D.2` |
| `### Exercise D — Custom agent with Plan → Implementation handoff (≈15 min)` | `### Exercise C — Custom agent with Plan → Implementation handoff (≈15 min)` | unchanged body |

Time estimates per exercise unchanged (Custom agent ≈15 min, MCP ≈25 min). Total still ~90 min.

### Cross-references updated

| Location | Before | After |
| --- | --- | --- |
| Top intro (line 3) | "...extend the agent with an MCP server you build yourself, and ship a custom agent..." | "...ship a custom agent that hands a plan off to Agent for execution, and extend the agent with an MCP server..." |
| What You'll Learn bullets | MCP bullet before custom-agent bullet | Custom-agent bullet before MCP bullet |
| TOC (lines 17–18) | 1.4 MCP / 1.5 Custom agents | 1.4 Custom agents / 1.5 MCP |
| TOC (lines 22–23) | Exercise C MCP / Exercise D Custom | Exercise C Custom / Exercise D MCP (anchor slugs updated to match) |
| Pre-lab Node.js step | `[Exercise C](#exercise-c--consume--create-an-mcp-server-25-min)` | `[Exercise D](#exercise-d--consume--create-an-mcp-server-25-min)` |
| §1.1 picker line | "built-in Agent in Exercises A–C, ... custom agent in Exercise D" | "built-in Agent in Exercises A, B, and D, ... custom agent in Exercise C" |
| Part 2 framing intro | "Exercise B leaves `app.py` reverted for Exercise C; Exercise D handed off to Agent reuses the test file from Exercise A" | "Exercise B leaves `app.py` reverted for Exercise C; Exercise C's handoff to Agent reuses the test file from Exercise A; Exercise D's MCP server imports from the `app.py` Exercise A fixed" |
| Exercise A mid-callout | "(Exercise D will show the alternative: switching to the dedicated Plan built-in agent.)" | "(Exercise C will show the alternative...)" |
| Exercise A sub-step | "It was added to `agents/requirements.txt` in Exercise A." | unchanged (still correct) |
| Recap table | Step 4 = MCP, Step 5 = Custom agent | Step 4 = Custom agent, Step 5 = MCP (rows swapped, content unchanged) |
| Exercise B closing callout | "...clean for Exercise C." | unchanged — the "next exercise" is still Exercise C, which (now) is the custom-agent task that scaffolds into `app.py`, so the clean state still matters |

## Change 2 — Removed "Fill in the decision table" from Exercise B

- Deleted the `#### Fill in the decision table` heading, its intro line ("After the three runs, complete this table from your own experience:"), and the 3-row table.
- Updated the "✅ **You should now see:**" callout immediately after to drop the "filled-in decision table" phrase. New text:
  > ✅ **You should now see:** three working `/healthz` endpoints (one per run, reverted between) and a working mental model for when each tier is appropriate. (Final state: revert one more time so `app.py` is clean for Exercise C.)

## Verification

- `grep` confirms zero remaining references to `Exercise C` for MCP or `Exercise D` for custom agent, no `1.4 MCP` / `1.5 Custom`, no `C.1` / `C.2` headings, no `fill in.*decision table` strings.
- Section separators (`---`) intact between Exercise C ↔ Exercise D and Exercise D ↔ Congratulations.
- No content rewrites — only header renumbering, anchor updates, ref rewrites, and the decision-table excision.


# Lab 3 Exercise C Expansion — Three Custom Agents

**Author:** Kaylee  
**Date:** 2026-04-20  
**Status:** Shipped

## What Changed

Expanded **Exercise C** in `agents/README.md` from creating ONE custom agent to creating THREE custom agents:

1. **C.1 — `endpoint-scaffolder`** (existing, kept as-is) — demonstrates **handoffs** / workflow chaining (planner → Agent executor).
2. **C.2 — `code-quality-reviewer`** (NEW) — demonstrates **least-privilege** via tool whitelist (`[codebase, findTestFiles, search]` only — NO `editFiles`, NO `runCommands`).
3. **C.3 — `test-author`** (NEW) — demonstrates **scope-locking** via system-prompt enforcement (has `editFiles` but only allowed to touch `agents/tests/`).

### Section-Level Changes

- **Exercise C heading:** Changed from "Custom agent with Plan → Implementation handoff (≈15 min)" to **"Build a custom-agent toolbox (≈30 min)"**.
- **Structure:** Restructured into **three sub-sections** (C.1, C.2, C.3), each following the same shape: pattern framing → frontmatter → system prompt → invocation step → ✅ callout.
- **Opener paragraph:** Added one-paragraph opener explaining the three patterns and how they form a mini code-review pipeline.
- **Closer paragraph:** Added one-paragraph closer noting the pattern scales and that custom agents are "the cheapest way to encode 'how this team works'."

### Downstream Updates

All required downstream updates applied:

1. **Table of Contents** (line 5–20): replaced single Exercise C entry with parent + three sub-entries (C.1, C.2, C.3).
2. **§1.4 Custom agents theory** (line 119–129): added forward reference: "In Exercise C you'll build three of them — a planner, a reviewer, and a test author — to see the surface in three different shapes."
3. **Part 2 intro paragraph** (line 154): updated "they build on each other" parenthetical to reflect three custom agents forming a pipeline.
4. **What You'll Learn bullet** (line 26): pluralized and rephrased to mention three patterns (handoffs, least-privilege, scope-locking).
5. **Lab subtitle / opening paragraph** (line 3): updated to mention "a small toolbox of custom agents" instead of "a custom agent".
6. **Congratulations section** (line 490–508): updated Step 4 recap to list all three agents and the mini pipeline flow. Updated "Key Takeaways" to mention tool whitelists enforce least-privilege and system prompts enforce scope.

### Time Budget Math

| Exercise | Old Time | New Time | Delta |
| -------- | -------- | -------- | ----- |
| A — Agent loop | 20 min | 20 min | — |
| B — Permission levels | 8 min | 8 min | — |
| C — Custom agents | **15 min** | **30 min** | **+15 min** |
| D — MCP consume + create | 25 min | 25 min | — |
| **Total hands-on** | **68 min** | **83 min** | **+15 min** |

Adding theory transitions (~7 min) + Part 1 theory (18 min) keeps the total around **90 min** as designed.

## Why

**User request:** Geronimo asked to expand Exercise C to demonstrate breadth of the custom-agent surface and show different patterns (handoffs, narrow tool whitelists, read-only personas). Goal was to add ~15–20 minutes of meaningful content.

**Pedagogical rationale:** A single custom agent shows "the surface exists." Three agents show "here's how you'd actually use it in a team." The patterns are orthogonal:
- **Handoffs** — workflow chaining, demonstrated by endpoint-scaffolder → Agent.
- **Least-privilege** — security boundary via tool whitelist, demonstrated by code-quality-reviewer (read-only).
- **Scope-locking** — edit boundaries via system-prompt enforcement, demonstrated by test-author (only touches `agents/tests/`).

Together they form a coherent mini pipeline (plan → implement → review → test), which is more memorable than three disconnected examples.

## Judgment Calls

### C.2 — code-quality-reviewer Tool Whitelist

**Decision:** `[codebase, findTestFiles, search]` — NO `editFiles`, NO `runCommands`.

**Rationale:** The load-bearing demo is "this agent CANNOT edit" — the tool whitelist is the security boundary. Omitted MCP tools to keep the surface small (MCP is Exercise D's focus).

### C.2 — System Prompt Rules

**Decision:** Five rules, emphasizing structured report format (Blocking / Suggestions / Nits), file:line anchors, and "no code rewrites."

**Rationale:** The most common learner mistake with review agents is letting them paste giant diffs as "fixes" — defeats the read-only boundary. Rule 4 ("describe the fix in prose") addresses that directly.

### C.3 — test-author Scope Enforcement

**Decision:** Enforce scope via system prompt ("you may only create or modify files under `agents/tests/`"), NOT via tool whitelist.

**Rationale:** The agent needs `editFiles` to write tests. The lesson is "system prompts can constrain a broad tool" — complementary to C.2's "tool whitelist can enforce a hard boundary." Both are useful patterns.

### C.3 — Handoff Back to Agent

**Decision:** Added one handoff (`label: Fix the bug this test caught`) to show bidirectional workflow.

**Rationale:** C.1 shows forward handoff (planner → executor). C.3 shows backward handoff (test author → bug fixer). Together they demonstrate handoffs aren't just linear.

### C.3 — Edge-Case Test Prompt

**Decision:** Three edge cases: (1) zero signups, (2) max_participants=0, (3) URL-encoded activity name.

**Rationale:** All three are realistic corner cases for the spots-left endpoint from C.1. The URL-encoding case (Dungeons & Dragons → `%26`) is the most subtle — it tests learners' understanding that FastAPI path params require encoding.

### Model Pin: gpt-5

**Decision:** All three agents use `model: gpt-5`.

**Rationale:** User-confirmed in prior sessions (Jayne QA). Kept consistent across all three for reproducibility.

### Frontmatter Keys

**Decision:** All three agents use `user-invocable: true` + `disable-model-invocation: true`. No `infer:`.

**Rationale:** Per Book's Agent Mode inventory, `infer:` is deprecated. The replacement is the pair above. Kept consistent across all three agents.

## Preserved

- **All 5 prior Jayne QA fixes** (Windows venv path, PowerShell `rm -rf`, python3/python pre-lab split, revert command, npx delay note) — intact.
- **Custom Agents BEFORE MCP** in both theory and hands-on order — unchanged.
- **Theory-first structure** (§1.1–1.5 intact) — unchanged.
- **No decision table sub-section** (previously removed) — stayed removed.

## Artifacts Created

1. Updated `agents/README.md` with three-agent Exercise C and all downstream updates.
2. This decision document (`.squad/decisions/inbox/kaylee-lab3-three-custom-agents.md`).
3. Appended to `.squad/agents/kaylee/history.md` under "## Learnings".


# Decision: Rename agents/mcp/ → agents/mcp_servers/

**Date:** 2026-04-21T08:55Z  
**Agent:** Kaylee (Lab Builder)  
**Status:** Implemented

## Problem

Lab 3 Exercise D had a Python module shadowing bug. The directory `agents/mcp/` shared its name with the installed `mcp` PyPI package (version 1.27.0). When users ran Python from inside the `agents/` directory:

```bash
cd agents
python -c "import mcp.server.fastmcp"  # ❌ ModuleNotFoundError: No module named 'mcp.server'
```

Python's CWD-on-sys.path behavior resolved `import mcp` to the local `agents/mcp/` folder instead of the installed package in `.venv/lib/python3.x/site-packages/mcp/`. The local `agents/mcp/` only contained `__init__.py` and `activities_server.py` — it had no `server/` submodule, causing the import to fail.

**Crucially:** The import worked fine from the repo root because the CWD was `/repo`, not `/repo/agents`, so Python didn't encounter a local `mcp/` directory to shadow the installed package.

## Decision

Rename `agents/mcp/` to `agents/mcp_servers/` to eliminate the name collision.

## Implementation

1. `git mv agents/mcp agents/mcp_servers` — preserves Git history
2. `rm -rf agents/mcp_servers/__pycache__` — clean up gitignored cache
3. Updated all references:
   - `.vscode/mcp.json` line 15: `agents.mcp.activities_server` → `agents.mcp_servers.activities_server`
   - `agents/README.md`: 3 locations (Exercise D step 2, step 3, JSON snippet line 572)
   - `.squad/` decision logs: 5 historical files for consistency
4. Verified fix:
   - `cd agents && python -c "from mcp.server.fastmcp import FastMCP"` ✅
   - `python -m agents.mcp_servers.activities_server` ✅ (starts successfully)
5. Committed with `Co-authored-by: Copilot` trailer, pushed to origin/main

## Rationale

- Descriptive name: `mcp_servers/` clarifies that this directory contains MCP server implementations, not the `mcp` package itself
- Collision eliminated: No more shadowing — `import mcp` always resolves to the installed PyPI package
- History preserved: `git mv` maintains blame/log for both files
- Consistency: All references updated in one atomic commit

## Alternatives Considered

1. **Move venv to repo root** (`.venv` instead of `agents/.venv`):
   - Would fix the immediate bug by changing import resolution order
   - BUT `.vscode/mcp.json` hardcodes `${workspaceFolder}/.venv/bin/python`, suggesting the venv is intended at repo root, not in `agents/`
   - This is a SEPARATE pre-existing issue (venv location mismatch) — flagged for Geronimo but NOT fixed in this pass

2. **Add `agents/` to `.vscode/mcp.json` command CWD override**:
   - Would avoid shadowing by ensuring Python runs from repo root
   - BUT doesn't prevent users from running `cd agents && python -m agents.mcp.activities_server` directly in their terminal
   - Rename is the safer, more robust fix

## Impact

- ✅ Exercise D now works regardless of which directory the user is in
- ✅ No test breakage (pytest found no tests to run, as expected)
- ✅ Zero API changes — the module path is an implementation detail to learners following the lab
- ⚠️ Future: if venv location is moved from `agents/.venv` to `.venv` at repo root (to match `.vscode/mcp.json` assumption), that will be a separate decision

## Learning Extracted

Captured in `.squad/skills/python-package-shadow/SKILL.md` — reusable pattern for avoiding PyPI package name collisions in Python projects.


# Lab 3 — Agent Mode in GitHub Copilot · LOCKED PLAN

**Owner:** Zoe (Lead) · **Status:** LOCKED — Kaylee to author · **Duration:** 90 min
**Supersedes:** `.squad/decisions/inbox/zoe-lab3-plan.md` (draft)
**Spine chosen:** Spine B (Book's recommendation) — cloud Coding Agent deferred to a future Lab 4.

---

## 1. Learning objective (one sentence)

> By the end of Lab 3, the learner can drive VS Code's **Agent** built-in agent through a real multi-file change with terminal + tests, choose the correct **Permission level** for the risk at hand, extend the agent with one **MCP server**, and author a workspace-scoped **custom agent** (`.github/agents/*.agent.md`) that hands off to Agent.

No cloud. No CLI background agents. No subagents. No hooks. Local Agent only.

---

## 2. 90-minute budget (locked)

| Segment | Minutes | Notes |
|---|---:|---|
| Intro + picker correction (Target × Agent × Permission, "Plan ≠ renamed Edit") | 8 | One slide, one diagram |
| Block 1 theory: the agent loop | 5 | Whiteboard the loop: plan → edit → run → observe → iterate |
| **Block 1 hands-on: agent loop in practice** | **20** | Exercise A (River #1) |
| Block 2 theory: permission levels & security trade-offs | 5 | Default / Bypass / Autopilot |
| **Block 2 hands-on: permission levels** | **8** | Exercise B (NEW, mini) |
| Block 3 theory: what MCP is | 5 | One slide, picker hierarchy + trust prompt |
| **Block 3 hands-on: consume + create an MCP server** | **25** | Exercise C (NEW — consume optional, create required) |
| Block 4 theory: custom agents — frontmatter + handoffs | — | folded into the exercise intro (≤2 min) |
| **Block 4 hands-on: custom agent + Plan→Implementation handoff** | **15** | Exercise D (River #3, corrected) |

**Totals:** Theory 15 min · Hands-on 68 min · Intro+wrap 17 min (8 intro + 9 wrap/Q&A/key takeaways). Within charter (theory ≤15, hands-on ≥55, intro+wrap ≤20). ✅

> **River's Exercise 2 (plan-first unregister): CUT.** It overlaps Block 1 in capability surface (multi-file edit + terminal + tests) and consumes 20 min we don't have once Permission levels and MCP are in. The **plan-first prompting pattern** River wanted to teach is preserved as a **callout inside Exercise A** ("now re-prompt with a plan-first gate and watch the difference") and demonstrated again in Exercise D where the custom agent enforces it via system prompt.

---

## 3. Final exercise list

All exercises run against the existing `agents/` app. Do not reorganize folders. Match Lab 2's format: `## Step N` → `### 📖 Theory` → `### Activity` → fenced prompt blocks with the Copilot prompt badge.

### Exercise A — Agent loop in practice (Block 1, ~22 min)
- **Capability:** multi-file edit + terminal execution + test iteration + edit-review overlay + stop button.
- **Source:** River's Exercise 1, kept verbatim in shape.
- **Task:** Fix two bugs in `agents/backend/app.py` (`signup_for_activity`: no duplicate-email guard, no capacity check). Add `pytest` to `agents/requirements.txt`. Create `agents/tests/__init__.py` and `agents/tests/test_app.py` with 4 cases (happy path, duplicate, capacity, 404). Run `pip install` and `pytest -v` in the integrated terminal until green.
- **Files touched:** `agents/backend/app.py`, `agents/requirements.txt`, `agents/tests/__init__.py` (new), `agents/tests/test_app.py` (new).
- **Visible checkpoint:** `pytest -v` shows 4 passing tests in the terminal; manual `curl` POST of the same email twice returns `400 Already signed up`.
- **Mid-exercise callout (preserves River's #2 idea):** after first run, learner re-prompts with the **plan-first** pattern (P1) and observes the diff in agent behavior. No new feature, just a re-run with a tighter prompt.

### Exercise B — Permission levels, three tiers, same task (Block 2, ~10 min)
- **Capability:** Default Approvals → Bypass Approvals → Autopilot (Preview); approval flow; security trade-off.
- **Source:** NEW (per Zoe).
- **Task:** Same trivial prompt run three times with the permission selector changed each time:
  > *"Add a `GET /healthz` endpoint to `agents/backend/app.py` that returns `{\"status\": \"ok\"}`, then `curl localhost:8000/healthz` from the terminal to verify."*
  - Run 1 — **Default Approvals.** Count the dialogs. Discuss what each one is asking.
  - Run 2 — **Bypass Approvals.** Revert the change first (`git checkout`). Re-run. Note: zero dialogs, agent auto-retries on errors.
  - Run 3 — **Autopilot (Preview).** Revert. Re-run with a deliberately ambiguous prompt: *"Add a health check"* — observe the agent answers its own clarifying question.
- **Files touched:** `agents/backend/app.py` (added + reverted between runs).
- **Visible checkpoint:** Learner can articulate, in their own words, when each tier is appropriate and what the security cost of Bypass/Autopilot is. Lab page includes a 3-row decision table they fill in.

### Exercise C — Consume one MCP server, then build one (Block 3, ~25 min)
- **Capability:** MCP server install via `.vscode/mcp.json`, tool surface in **Configure Tools**, MCP trust prompt, agent invoking an MCP tool — **and** authoring a minimal `FastMCP` Python server that exposes app data the agent cannot otherwise see.
- **Source:** NEW (per Zoe + Geronimo's directive 2026-04-20). Structure adopted wholesale from Book's proposal (`book-mcp-block-proposal.md`); inspired by the user's `github-copilot-workshops-labs-python/lab-06-mcp` README §3–§4 + §9.4.
- **Block layout (~25 min):**
  - **~3 min — Frame.** 60-sec MCP elevator pitch ("USB-C for AI tools"). Two-sided picture: clients (Copilot) ↔ servers (capabilities). State today's split: we'll *use* one (optional), then *build* one (required).
  - **~7 min — Consume half (OPTIONAL).** See callout below.
  - **~12 min — Create half (REQUIRED).** See below — this is the load-bearing exercise.
  - **~3 min — Wrap.** Callouts: tools vs. resources (we only did tools), MCP runs as a separate process (security boundary), permission re-prompts per MCP tool by default. Pointer to `https://github.com/mcp`.

- **Consume half — Filesystem MCP (~7 min, OPTIONAL):**
  > **⚠️ Optional — skip if you don't have Node.js.** Run `node --version` in the integrated terminal. If it errors, jump straight to the Create half; the rest of the lab does not depend on this step.

  1. Create `agents/sample-data/school-policies.txt` (5–10 lines of plain-text "policy" rules — pre-created in the pre-lab; learner just verifies it exists).
  2. Create `.vscode/mcp.json` with the filesystem server entry:
     ```jsonc
     {
       "servers": {
         "school-files": {
           "type": "stdio",
           "command": "npx",
           "args": ["-y", "@modelcontextprotocol/server-filesystem", "${workspaceFolder}/agents/sample-data"]
         }
       }
     }
     ```
  3. Run **MCP: List Servers** → start `school-files` → accept the trust prompt.
  4. Single demo prompt to Agent:
     > *"Read `school-policies.txt` from the school-files MCP server and summarise the participation rules."*

- **Create half — `mergington-activities` server (~12 min, REQUIRED):**
  1. Append `mcp[cli]>=1.0` to `agents/requirements.txt` and `pip install -r agents/requirements.txt` in the integrated terminal (the dependency is pre-installed in the lab venv per §7, but learners run the install to see it resolve).
  2. Create `agents/mcp/__init__.py` (empty) and `agents/mcp/activities_server.py` per Book's §6 code sketch:
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
  3. Register the server in `.vscode/mcp.json` **additively** — keep the `school-files` entry if Node was present, otherwise this is the only entry:
     ```jsonc
     {
       "servers": {
         "mergington-activities": {
           "type": "stdio",
           "command": "${workspaceFolder}/.venv/bin/python",
           "args": ["-m", "agents.mcp_servers.activities_server"]
         }
       }
     }
     ```
  4. Run **MCP: List Servers** → start `mergington-activities` → accept the trust prompt. Open **Configure Tools** and verify `list_activities` and `get_signups_count` appear.
  5. Demo prompt to Agent:
     > *"Which activity is closest to full? Use the mergington-activities MCP."*

- **Files touched:** `agents/mcp/__init__.py` (new), `agents/mcp/activities_server.py` (new), `agents/sample-data/school-policies.txt` (new — optional, only relevant if Node is present), `.vscode/settings.json` (`"chat.mcp.discovery.enabled": true`), `.vscode/mcp.json` (new — both server entries when Node is present, just `mergington-activities` otherwise), `agents/requirements.txt` (append `mcp[cli]>=1.0`).
- **Visible checkpoint:** Copilot Chat tool-call UI shows `mergington-activities` tool calls; the chained sequence `list_activities()` → multiple `get_signups_count(...)` calls is visible inline in the transcript before the agent's final answer. (If Node was available, the consume-half prompt earlier shows a `school-files` `read_file` call against `school-policies.txt`.)
- **Reference:** code sketch and `.vscode/mcp.json` patterns lifted from Geronimo's `lab-06-mcp` README §3–§4 + §9.4 — credit it inline in Kaylee's prose as the inspiration repo.

### Exercise D — Custom agent with Plan → Implementation handoff (Block 4, ~15 min)
- **Capability:** custom agent file format, frontmatter (`description`, `tools`, `model`, `agents`, `handoffs`, `target`), tool whitelist, handoff button, the **Plan** built-in agent as a separate persona.
- **Source:** River's Exercise 3, **corrected** per Book.
- **File path (corrected):** `.github/agents/endpoint-scaffolder.agent.md` — **NOT** `.github/chatmodes/endpoint-scaffolder.chatmode.md`.
- **Frontmatter (corrected):** uses `description`, `tools`, `model`, `handoffs`. **Drop `infer:`** (deprecated). Use `user-invocable: true` and `disable-model-invocation: true` so it shows in the picker but won't be auto-invoked by other agents.
- **Task:**
  1. Run **Chat: New Custom Agent**, name `endpoint-scaffolder`, accept `.github/agents/` as the location.
  2. Edit the generated file to:
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
     Plus the system-prompt body River drafted (the 5 numbered house-rules block — keep verbatim, just swap the path note).
  3. Switch the chat picker to the **Plan** built-in agent (NOT Agent). Prompt: *"Scaffold a `GET /activities/{name}/spots-left` endpoint using the endpoint-scaffolder conventions."* Plan produces a structured plan.
  4. Click the **Implement this plan** handoff button → control transfers to Agent which executes.
- **Files touched:** `.github/agents/endpoint-scaffolder.agent.md` (new), `agents/backend/app.py`, `agents/tests/test_app.py`.
- **Visible checkpoint:** Custom agent appears in the agent picker with the description string visible; handoff button renders after Plan's response; final endpoint exists and tests pass.

---

## 4. What is NOT in this lab (explicit cuts)

- **Cloud Coding Agent** — deferred to Lab 4. Do not mention beyond a one-line "next lab" teaser at the wrap.
- **Copilot CLI background agents** — same.
- **Authoring MCP resources (the second primitive) and the MCP client side** — we only build a tools-only server. Resources (`greeting://{name}`-style URIs from the reference repo) and writing a custom MCP host/client are explicitly out; mention in the Block 3 wrap as "what we skipped" and in What's Next.
- **Subagents** (`agents:` frontmatter pointing at other custom agents). Confusing next to handoffs; cut.
- **Hooks** (`hooks:` frontmatter). Preview, unstable. Cut.
- **BYOK models** — out of scope; the lab uses whatever model the learner has.
- **Third-party agents** (Anthropic/OpenAI harnesses, `target:` other than local). Cut.
- **Edit mode.** Mentioned once in the intro correction, then never again. Do not have learners enable `chat.editMode.hidden`.
- **River's Exercise 2 (unregister feature).** Cut for time. The plan-first pattern it taught is preserved as a callout in Exercise A and a structural feature of Exercise D.
- **AGENTS.md / `copilot-instructions.md` deep-dive** — already covered in Lab 2. One sentence in Block 4 disambiguating "custom agent ≠ AGENTS.md", no more.

---

## 5. Resolutions to River's open questions

| # | River's Q | Resolution |
|---|---|---|
| 1 | Chatmode file location & naming | **Resolved by Book.** It's `.github/agents/<name>.agent.md`. `tools:` frontmatter is honored. Lab uses corrected path everywhere. |
| 2 | Terminal/run-command access enabled by default in lab env? | **Defer to Kaylee.** Pre-lab checklist must verify Default Approvals is selected and `chat.tools.terminal.enabled` is on. If the lab env disables it, Block 1 and 2 break. |
| 3 | MCP availability | **Resolved.** Two servers, both wired during the lab (not preinstalled): (a) **`mergington-activities`** — the Python `FastMCP` server learners author in the create half (REQUIRED); (b) **filesystem MCP** (`@modelcontextprotocol/server-filesystem`) via `npx` for the consume half (OPTIONAL — gated on Node.js). **Not GitHub MCP** (dropped per Geronimo's directive 2026-04-20). Kaylee to script both `.vscode/mcp.json` snippets so learners paste, not type. |
| 4 | Built-in plan/approve UX vs prompted pause? | **Both exist now.** Plan is a separate built-in agent (use it in Exercise D). The prompted pause pattern is also taught (Exercise A callout) for use inside Agent itself when you don't want to switch personas. |
| 5 | Auto-approve default for `runCommands`/`editFiles`? | **Default Approvals = confirmation dialogs.** That's exactly why Exercise B exists — make the default visible before showing how to bypass. |
| 6 | Lab 2 overlap (skills vs custom agents) | **Resolved.** One sentence in Block 4: "skills add capabilities to *any* agent; a custom agent is a *new persona* with its own tool whitelist, model pin, and handoffs." Move on. |

---

## 6. Book's corrections — applied everywhere

- ✅ Custom agent files: `.github/agents/*.agent.md` (Exercise D).
- ✅ **Plan is a separate built-in agent**, not a renamed Edit. Stated in intro correction; demonstrated in Exercise D step 3.
- ✅ **Edit mode is deprecated** — single mention in intro, never used.
- ✅ Frontmatter keys: `description`, `tools`, `model`, `handoffs`, `target` (omitted — defaults to local), `user-invocable`, `disable-model-invocation`. **`infer:` removed.**
- ✅ Picker hierarchy taught up front: **Target × Agent × Permission**.
- ✅ Permission levels are 3 tiers (Default / Bypass / Autopilot-Preview) — that *is* Block 2.
- ✅ MCP install via `.vscode/mcp.json`; tools appear in Configure Tools; trust prompt called out.
- ✅ MCP block now teaches **consume + create** per user directive 2026-04-20; the create half (`agents/mcp/activities_server.py`) is the load-bearing exercise, the consume half (filesystem MCP via `npx`) is optional and gated on Node.js.

---

## 7. Format & deliverables Kaylee inherits

- Match `customize-copilot/README.md` and `README-lab2.md` exactly: TOC, `## Step N`, `### 📖 Theory`, `### Activity`, fenced prompts with the Copilot prompt badge, "Congratulations! 🎉" close, "What's Next?" pointing at Lab 4 (cloud), writing your own MCP server, Copilot Extensions, evals.
- Reuse `agents/` app **as-is**. No folder reorg. No file renames.
- Pre-lab steps Kaylee must script:
  1. Confirm `chat.agent.enabled` is on at org level.
  2. **REQUIRED:** `pip install "mcp[cli]>=1.0"` inside the lab venv (Block 3 create half depends on it).
  3. **OPTIONAL:** `node --version` sanity check — gates the Block 3 consume half. If Node is absent, learners skip straight to the create half; the rest of the lab is unaffected.
  4. Pre-create `agents/sample-data/school-policies.txt` with 5–10 lines of plain-text policy rules. Only relevant if Node is present, but cheap to ship regardless so the optional path "just works".
  5. Confirm both `.vscode/mcp.json` snippets (filesystem MCP + `mergington-activities`) are current as of authoring date.
- Lab opener slide: the Target × Agent × Permission diagram + the "Plan ≠ renamed Edit" retraction.

---

## 8. Handoff to Kaylee

**Kaylee — go write Lab 3.** Spine is locked: 4 steps mapping 1:1 to the 4 blocks above (Agent loop / Permission levels / MCP consume + create / Custom agent with handoff). Use Lab 2's structure verbatim — TOC, badged prompt blocks, theory→activity rhythm, "Congratulations 🎉" + "What's Next?" close. The four exercises in §3 are the spine, including all file paths, prompts, and visible checkpoints; treat those as fixed and only adapt voice and framing. Apply every correction in §6 — especially `.github/agents/*.agent.md`, no `infer:` frontmatter, and Plan-as-separate-agent (not a renamed Edit). Cuts in §4 are non-negotiable: no cloud agent, no MCP resources/client authoring, no subagents/hooks. **Block 3's fixed contract per Geronimo's 2026-04-20 directive: consume = OPTIONAL (filesystem MCP, gated on Node.js with the ⚠️ callout); create = REQUIRED (`agents/mcp/activities_server.py` is the load-bearing exercise and must ship even if every other Block 3 minute gets squeezed).** If something doesn't fit in 90 min, cut depth from Block 4 first, then trim the consume half of Block 3 to a Kaylee-led 90-sec demo — never trim the create half. Ping Book if any VS Code surface name has shifted between his 2026-04-20 capture and your authoring date; ping Zoe only if you want to alter the spine or the consume/create split.



---

## 2026-04-21: Lab-building conventions canonized post-Lab 3

**By:** Geronimo (via Copilot, distilled from Lab 3 conversation arc)

**Decision:**

Twelve lab-building conventions have been extracted from the Lab 3 build cycle and canonized to prevent re-litigation in Lab 4+:

1. **Custom-agent frontmatter format:** Every `.agent.md` file MUST use YAML frontmatter with required `name` field per GitHub's official docs. Body follows frontmatter with system-prompt content.

2. **Simple agents in intro labs:** No agent handoffs or multi-agent orchestration in intro/agent-mode labs (Lab 3 is intro). Each custom agent does ONE thing well. Save orchestration for advanced labs.

3. **Divide features across prompts:** When teaching feature work, split into separate prompts (e.g., Lab 3 Exercise A.1/A.2). Reinforces "small, scoped prompt" pattern.

4. **Manual file creation > Command Palette:** Have students create files manually with editor, not via Cmd+Shift+P flows (less reproducible cross-platform). Applies to agent files, plugin files, MCP configs.

5. **Read-through for friction-heavy content:** When features are preview-flagged, fiddly to install, or org-managed (e.g., `chat.plugins.enabled`), use "📖 read this" sections instead of forcing hands-on. See Lab 3 Exercise B (permissions), E.3 (plugin install).

6. **Flexible time budget:** Old default was 90 min hard cap; Geronimo overrode for Lab 3. Build the lab the right size; longer is fine if content earns it. Still sequence by time complexity.

7. **Tight continuity across exercises:** Reuse what was built earlier (Lab 3 Exercise E reused C's agent + D's MCP). Reuse beats fresh examples — students see payoff.

8. **Don't re-teach prior labs:** Lab 3 skipped custom instructions, prompt files, skills (covered in Lab 2). Check what prior labs cover before scoping new labs. Cite "previously taught in Lab N."

9. **Stack consistency:** All labs use `agents/` FastAPI + vanilla JS app. Don't introduce new stacks per lab — students learn Copilot patterns, not frameworks.

10. **Repo hygiene rules:**
    - `.vscode/` tracked (users get working configs)
    - `.squad/` gitignored (never pushed)
    - Module-shadow gotcha: never name local Python package same as PyPI dep (see `python-package-shadow` skill)
    - READMEs include both install AND run commands

11. **Process: plan before building:** Coordinator proposes structure, gets approval, then spawns builder. Prevents rework.

12. **Author's-note style:** Friendly, concrete, allergic to jargon. "You should now see..." checkpoints. Emoji legend: 🛠️ (hands-on), 📖 (read), ✅ (checkpoint), 📌 (sidebar), 🪧 (reminder).

**Applies to:**

- **Kaylee (primary):** Encode into spawn prompt so all future labs follow these patterns automatically
- **Zoe:** Scope decisions must check prior labs (convention 8) and respect simple-agent rule for intro labs (2)
- **Book + River:** When they verify Copilot facts in lab content, these formatting/structural conventions apply (e.g., frontmatter format in 1, emoji legend in 12)
- **Jayne:** QA walkthroughs should verify compliance (e.g., manual creation steps in 4, checkpoints in 12)

---

## 2026-04-21: Kaylee charter additions applied (coordinator action)

**By:** Coordinator (applying Kaylee's self-proposed update)

**What:**

Kaylee proposed eight conventions from the canonized list (1, 2, 4, 5, 6, 7, 8, 3 above) be added to `.squad/agents/kaylee/charter.md` under the "How I Work" section to ensure they auto-flow into future spawn prompts. Coordinator reviewed and applied on 2026-04-21.

**Status:** Applied to `.squad/agents/kaylee/charter.md`

---

## Active Decisions

No formal decisions recorded yet. Lab 3 scope decisions land here once
Kaylee + Jayne lock the draft.

## Governance

- All meaningful changes require team consensus
- Document architectural decisions here
- Keep history focused on work, decisions focused on direction

---

## 2026-04-21: Lab 4 — GitHub Copilot CLI (Agenda → README, under review)

**Proposer/Coordinator:** Zoe (proposal 2026-04-20) → Coordinator (agenda lock 2026-04-21)

**Status:** README authored (Kaylee) → under review (Zoe, in progress)

### Agenda v3 (Book-verified, locked)

**Lab Duration:** 90 min  
**Theory:** 15 min | **Hands-on:** 50 min | **Programmatic:** 20 min | **Wrap:** 5 min

**Learning Objective:**  
Use GitHub Copilot CLI to ask context-aware questions, execute autonomous tasks, review code from terminal, configure CLI-specific agents, and script workflows for automation — all without an IDE.

**Differentiation from Labs 1–3:**
- Lab 1: Chat UI in VS Code (interactive Ask/Plan/Agent)
- Lab 2: Custom instructions, skills, AGENTS.md (workspace-level)
- Lab 3: Agent Mode, MCP, VS Code plugins, custom agents (workspace agents in `.github/agents/`)
- **Lab 4: Terminal-native CLI with headless scripting, user-level agent config (`~/.copilot/agents/`), no IDE**

**Part 1 — Theory (~15 min):**
1. What Copilot CLI is (terminal-native, device-flow auth, 3 modes)
2. When to use CLI vs VS Code (SSH, CI/CD, headless)
3. Interactive vs programmatic modes
4. Slash commands overview

**Part 2 — Core CLI Usage (~50 min, Exercises A–E):**
- **A:** Install + auth (multi-platform, device flow)
- **B:** Context management (`@`, `/context`, `/compact`)
- **C:** Slash commands (`/plan`, `/fleet`, `/research`, `/chronicle` EXPERIMENTAL, `/skills`)
- **D:** Permission flags & patterns
- **E:** Multi-turn autonomous task (waitlist feature in autopilot mode)

**Part 3 — Customization (~30 min, read-throughs + 1 hands-on):**
- Custom instructions (user + repo paths)
- Custom agents (user-level only: `~/.copilot/agents/*.agent.md`)
- Hooks (read-through, config skeleton)
- Skills (CLI invocation, cite Lab 2)
- `/chronicle` (EXPERIMENTAL, requires `/experimental on`)
- CLI plugins (`/plugin` system, separate from VS Code)
- MCP (read-through, cite Lab 3)

**Part 4 — Programmatic & Automation (~20 min, Exercise F hands-on + Exercise G read-through):**
- **F:** Headless invocation (`-p` flag, `--output-format json`, scripting example)
- **G:** CI/CD integration (GitHub Actions, PR reviews, pre-commit)

### Book's CLI Verification (12 ✅ / 8 ⚠️ / 6 ❌ / 2 ❓)

**12 facts confirmed:**
- Install commands (brew, npm, winget)
- Device-flow auth via `/login`
- Trust folder prompt
- Slash commands: `/plan`, `/research`, `/fleet`, `/skills`
- Custom agents real, live in `~/.copilot/agents/`
- Modes affect behavior (interactive/plan/autopilot)
- Hooks exist (real feature)
- MCP integration supported
- CLI plugins system (`/plugin`)
- Programmatic mode flags

**8 facts partially correct:**
- npm package is `@github/copilot` (not `@github/copilot-cli`)
- `/chronicle` exists but EXPERIMENTAL (requires `/experimental on`)
- `/delegate` exists but creates PR, not local sub-agents
- Custom instructions use `.github/copilot-instructions.md` (not `.copilot/`)

**6 facts corrected:**
- Modes ARE `interactive`/`plan`/`autopilot` (NOT `ask`/`task`/`develop`)
- One-shot syntax is `copilot -p "..."` (NOT `copilot ask`)
- JSON output flag: `--output-format json` (NOT `--output json`)
- Custom-agent extension: `*.agent.md` (the `.agent` infix required)
- MCP paths: `~/.copilot/mcp-config.json` (user) + `.github/mcp.json` (repo)
- No `/stop` or `/reset` commands; use `/clear`, `/undo`, `/compact`

**2 facts unresolved:**
- Prompt composition internals (how CLI merges context + instructions + agents)
- Programmatic API surface (if exists beyond CLI flags)

### Kaylee's README Implementation

**File:** `copilot-cli/README.md` (~31 KB, 977 lines)

**Structure:**
- Pre-lab checklist (install verification, device flow auth, `agents/` app reuse)
- Part 1 — Theory 6 sections (5–2 min each)
- Part 2 — Exercises A–E (hands-on, ~50 min total)
- Part 3 — Customization (5 read-throughs, 1 hands-on, ~30 min)
- Part 4 — Exercises F–G (programmatic, ~20 min)
- Learning objectives, "What's Next" capstone

**Correctness rules applied (all 14 from Book's verification):**
1. ✅ Modes: `interactive`/`plan`/`autopilot`
2. ✅ One-shot: `copilot -p "..."`
3. ✅ JSON flag: `--output-format json`
4. ✅ Install: `brew install copilot-cli`, `npm install -g @github/copilot`, `winget install GitHub.Copilot`
5. ✅ Custom-agent extension: `*.agent.md`
6. ✅ Custom-instructions repo path: `.github/copilot-instructions.md`
7. ✅ MCP paths: `~/.copilot/mcp-config.json` + `.github/mcp.json`
8. ✅ `/delegate` clarified (GitHub cloud agent, not local sub-agents)
9. ✅ No `/stop` or `/reset`
10. ✅ `/chronicle` marked EXPERIMENTAL (`/experimental on` required)
11. ✅ Skills invocation: `@skill:skill-name`
12. ✅ Permission patterns (real syntax only)
13. ✅ Hooks: real, read-through with config skeleton
14. ✅ Plugins: CLI system (`/plugin`), separate from VS Code

**Continuity with Labs 1–3:**
- `agents/` app reused (first query in Ex A, context management in Ex B, waitlist feature in Ex E)
- Cross-references: Lab 2 for skills authoring, Lab 3 for MCP server creation

### Zoe's Review Status (in progress at scribe spawn)

**Checklist:**
- Verify all 28 CLI facts from Book's verification are accurate
- Confirm theory ≤25 min, hands-on ≤55 min, total pacing ~90 min
- Validate exercises run in target environment
- Confirm no overlap with Labs 1–3
- Audit clarity, jargon index, step-by-step clarity
- Check links and references (docs, CLI docs, official sources)
- Verify template compliance (badge, pre-lab checklist, learning objectives, "What's Next")

**Output:** `.squad/decisions/inbox/zoe-lab4-review.md` (pending)

**Handoff:** Upon approval, Lab 4 ready for Geronimo final review + merge.

---

## Copilot Directive: 2026-04-21 — No Overexplain

**Issuer:** Geronimo Basso  
**Context:** Lab 4 authoring (Kaylee)

**Directive:**  
Keep Lab 4 README at same word count ≈ Labs 1–3 (no bloat). If space is tight, drop examples rather than add explanatory paragraphs. When writing code examples, show the command and the output; don't explain the output.

**Rationale:** Students learn by doing, not reading. Kaylee's draft already had strong examples; overexplaining pushes toward reference-doc tone rather than lab tone.

**Application:** Already encoded in Kaylee's README authoring.

---

## Lab 4 Q&A Section Pattern (2026-04-21)

**Author:** Book (Copilot Expert)  
**Context:** First Q&A entry for Lab 4 (Plan mode vs `/plan` command distinction)

### Decision

Lab 4's Q&A section follows this structure:

#### Section Placement
- Top-level `## Q&A` section
- Positioned after all exercises/content but before "What's Next?"
- Added to TOC under main sections

#### Per-Question Format
```markdown
### **Q: [Question text]?**

**Short answer:** [1-2 sentence direct answer]

**[Term 1] ([qualifier]):**
- Bullet point details
- More specifics
- Technical notes

**[Term 2] ([qualifier]):**
- Bullet point details
- More specifics
- Technical notes

**📌 When to use which:**
- Use **[option 1]** when [scenario]
- Use **[option 2]** when [scenario]

**Sources:**
- [Link text](URL)
- [Link text](URL)
```

### Rationale

This format:
1. **Front-loads the answer** — learners get value immediately
2. **Structures comparisons** — bold terms + bullets create scannable contrast
3. **Guides application** — the "📌 When to use which" closer ties concepts to practice
4. **Cites sources** — builds trust, enables verification, matches "Book" charter (reference-grade)

### Example

First Q&A entry (Plan mode vs `/plan` command) in `copilot-cli/README.md` lines 879–904.

### Open Questions

- Should Q&A have its own file (like Labs 1–2) or stay in main README?
- If we add 5+ questions, should they be grouped by category (e.g., "Core Usage", "Customization", "Automation")?

### Related Conventions

See Lab 3 conventions #7 (structure TOC updates) and Lab 4 decision (no bloat — learners learn by doing).

---

## Lab 4 README Review (2026-04-21)

**Reviewed by:** Zoe (Lead/Curriculum Designer)  
**Artifact:** `copilot-cli/README.md` (~977 lines)  
**Reviewed against:** AGENDA.md v3, Book's verification report, Lab 3 exemplar, no-overexplain directive

### VERDICT: ✅ **Ship-ready with minor polish**

Kaylee delivered excellent work. The lab is accurate, complete, well-structured, and honors the "code + checkpoints > prose" style directive.

### Correctness (vs Book's verification)

Spot-checked 15 critical facts — all correct:

1. ✅ **Modes** (lines 84-86): `interactive`, `plan`, `autopilot` 
2. ✅ **One-shot syntax** (line 119): `copilot -p "..."`
3. ✅ **JSON flag** (line 122): `--output-format json`
4. ✅ **Install commands** (lines 174-177): brew, npm, winget
5. ✅ **Custom agents extension** (line 532): `*.agent.md`
6. ✅ **Custom instructions repo path** (line 493): `.github/copilot-instructions.md`
7. ✅ **MCP config paths** (lines 813-814): `~/.copilot/mcp-config.json` + `.github/mcp.json`
8. ✅ **`/delegate` behavior** (lines 146, 313): Cloud agent, not local sub-agents
9. ✅ **`/chronicle` experimental** (lines 147, 681): Requires `/experimental on`
10. ✅ **Skills invocation** (lines 314, 642): `@skill:skill-name`
11. ✅ **No `/reset`/`/stop`** (line 156, 277): Uses `/clear`/`/undo`/`/compact`
12. ✅ **Permission patterns** (lines 363-371): Real syntax only
13. ✅ **Hooks** (lines 601-629): Real, read-through with config
14. ✅ **CLI plugins** (lines 741-800): Separate from VS Code
15. ✅ **Context commands** (lines 151-154, 254-287): No fictional commands

**No correctness issues. All Book's corrections faithfully applied.**

### Completeness (vs AGENDA v3)

- ✅ All 7 exercises present (A-G)
- ✅ All 4 parts present (Theory, Core CLI, Customization, Programmatic)
- ✅ All 7 locked decisions Q1–Q7 honored
- ✅ "What We Skip" section complete (Labs 2-3 cites)

### Minor Polish Issues (3)

**Issue 1: Lines 88-93 — bulleted list duplicates what sections teach**
- Feature list appears before code blocks that teach the same concepts
- Recommended fix: Delete lines 88-93

**Issue 2: Line 225-226 — explains context before code shows it**
- Explanation precedes the code block demonstrating `@` mentions
- Recommended fix: Replace with concise statement: "Use `@` mentions and slash commands to control context."

**Issue 3: Lines 258-260, 269-270, 275-276, 287 — explains outputs when checkpoint already covers it**
- Prose explanations of slash command results immediately followed by verifying checkpoint
- Recommended fix: Delete explanatory sentences; keep code + checkpoint only

### Voice/Tone

- ✅ Friendly, hands-on tone matching Lab 3
- ✅ Concrete code-first structure
- ✅ Specific, testable checkpoints
- ✅ Direct imperative language

### Continuity (Labs 1–3)

- ✅ Uses `agents/` app throughout
- ✅ Cites Lab 2 for skills, Lab 3 for MCP
- ✅ No re-teaching of VS Code workflows

### Final Assessment

**Kaylee's execution: A-**  
Accurate, complete, strong. The 3 polish issues are minor and don't confuse learners — just add sentences that could be tightened. 

**Recommendation:** Apply the 3 minor fixes (≈5 min edit), then ship. No second review cycle needed.


---

## Lab 4 Friction Resolution (2026-04-27)

### User Directive: Lab 4 Inherits Knowledge, Not Code

**Date:** 2026-04-27  
**Source:** Geronimo Basso  
**Status:** Guiding principle for Lab 4 updates

**Principle:** Lab 4's reference to Lab 3 is intentional and stays. Learners bring *knowledge* from Lab 3 (what agents are, how they work) but NOT evolved *code* — the `copilot-cli/` workspace is self-contained code. Where README references Lab 3 features in code, rewording applies: concept is reusable, code isn't pre-built here.

---

### Decision: Lab 4 Inherits Knowledge, Not Code

**Date:** 2026-04-27  
**Author:** Kaylee (Lab Builder)  
**Status:** Applied

**Principle:** Lab 4 intentionally builds on Lab 3 *knowledge* (conceptual understanding of agents, Copilot, MCP) but NOT on evolved Lab 3 *code*.

The `copilot-cli/` application directory is a **fresh-start, code-self-contained** FastAPI app (Mergington High School activity signup system). It is *not* an evolution of the Lab 3 codebase.

**Rule:** README expected outputs must describe the actual local codebase running in the learner's workspace, never features from prior labs' evolved code.

**Why:** Learners verify lab outcomes by querying the local app with Copilot CLI (`@backend/app.py`). If expected output describes a different app (Lab 3's evolved version), the learner's verification will fail silently, breaking trust.

**When This Applies:**
- Any README line describing app features, endpoints, or behavior
- Any checkpoint or expected output that names specific functions, endpoints, or validation logic
- Any parenthetical referencing "features added in Lab X" — remove unless code actually has them

**Applied Fixes:**
- Lab 4 Exercise A, Step 4: Expected output rewritten to describe actual Mergington High School app (`GET /activities`, `POST /activities/{activity_name}/signup`). Removed references to Lab 3 endpoints (`/api/v1/register`) and validation logic (duplicate emails, capacity checks).
- Line 176: Softened "Labs 1–3" to "this lab's workspace" for independence clarity.

**References:**
- `copilot-cli/README.md` (lines 176, 198 updated)
- `copilot-cli/app/backend/app.py` (reference implementation)

---

### Decision: Lab 4 Friction Round 1 — 7 Surgical Fixes

**Date:** 2026-04-27  
**Author:** Kaylee (Lab Builder)  
**Source:** Simon's Lab 4 friction log (7 non-blocker issues)  
**Status:** Applied

**Summary:** Applied 7 surgical fixes to `copilot-cli/README.md` addressing clarity gaps flagged by first-time reader. All changes preserve tone, emoji style, and lab structure. No scope rewrite — only targeted rewording to eliminate ambiguity at interaction points (slash commands vs literal text, device-flow vs `/login`, path clarity).

**Fixes Applied:**
1. Full path in pre-lab navigation (`cd github-copilot-101/copilot-cli/app/`)
2. Plan mode vs `/plan` distinction in theory (Part 1.4)
3. Device-flow / `/login` parity in Exercise A Step 3
4. `@.` note repositioned before prompts in Exercise B Step 2
5. `go` literal vs slash command clarity in Exercise C Step 1
6. Exercise D Step 2 expected output (deny prompt visibility)
7. `/agents` plural consistency (line 582)

**Principle:** Clarity over assumption at interaction boundaries. First-timers should never guess whether input is a command, literal text, or browser action.

**References:**
- `copilot-cli/README.md` (all 7 fixes integrated)

---

### 2026-05-04T10:32:27+02:00: River merged into Book
**By:** Geronimo Basso (via Copilot)
**What:** Retired River (Copilot Expert — Patterns & Prompting). Merged role and knowledge into Book, who is now the unified Copilot Expert covering platform, surfaces, patterns, and prompting.
**Why:** User identified the two agents as redundant — overlapping Copilot expertise. Consolidation simplifies routing and removes the Book/River pairing step in the lab pipeline.
**Effects:**
- `.squad/agents/river/` → moved to `.squad/agents/_alumni/river/` (knowledge preserved).
- `book/charter.md` expanded: identity, expertise, what-I-own, how-I-work, boundaries now cover both domains.
- `book/history.md` appended with River's Lab 3 hands-on design notes and the five canonical agent-mode prompting patterns (plan-first, verify-by-running, constrain-blast-radius, checklist, diff-before-commit).
- `team.md` roster: River row removed; Book role title updated.
- `routing.md`: River entries folded into Book; lab pipeline simplified to Zoe → Book + Kaylee parallel → Jayne → Zoe.
- `casting/registry.json`: River status set to `retired` (name reserved, not reused).

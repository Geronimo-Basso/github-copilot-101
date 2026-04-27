---
name: "lab-exercise-structure"
description: "Patterns for structuring hands-on exercises in GitHub Copilot 101 labs"
domain: "technical-writing, pedagogy, workshop-design"
confidence: "high"
source: "earned — distilled from Lab 1, Lab 2, and Lab 3 implementations"
---

## Context

The GitHub Copilot 101 repo teaches Copilot through 90-minute hands-on labs. Each lab follows a consistent structure that balances theory, practice, and verification. This skill captures the structural patterns that make exercises effective.

**Key principle:** Every exercise must be *verifiable* — students know they succeeded before moving on.

## Patterns

### 1. Theory-First Structure (Lab 3 Model)

Lab 3 introduced a **theory-first** structure where all conceptual content appears upfront in Part 1, followed by hands-on exercises in Part 2.

**Structure:**
```markdown
# Lab Title

## Part 1: Theory (20-30% of lab time)
### 1.1 Concept Overview
### 1.2 Mental Model
### 1.3 Key Terms
### 1.4 Preview of What You'll Build

## Part 2: Hands-On Exercises (60-70% of lab time)
### Exercise A: [First hands-on task]
### Exercise B: [Second hands-on task]
...

## What's Next? (5-10% of lab time)
- Recap
- Extensions
- Further reading
```

**When to use:** Intro-level labs where students need a solid mental model before touching code. Lab 3 (Agent Mode intro) used this because "agent" is abstract — students needed the loop diagram and permission model first.

**When NOT to use:** Labs 1 and 2 use interleaved theory/practice (theory → practice → theory → practice). This works when concepts are concrete (e.g., "write a prompt file") and don't require heavy upfront framing.

### 2. Emoji-Based Visual Hierarchy

Use emojis to signal the **type** of activity:

| Emoji | Meaning | When to Use |
|-------|---------|-------------|
| 🛠️ | **Hands-on** — student does it | Any section where students type commands, create files, or modify code |
| 📖 | **Read-through** — student reads, doesn't do | Preview features, friction-heavy installs, org-managed settings (e.g., Lab 3 Exercise B permissions, E.3 plugin install) |
| ✅ | **Checkpoint** — verify before proceeding | After every hands-on step. Format: "✅ You should now see..." |
| 📌 | **Sidebar/callout** — tip or warning | Pro tips, gotchas, Windows-specific notes |
| 🪧 | **Mid-exercise reminder** — nudge | E.g., "🪧 Remember to activate your venv before running this command" |

**Example from Lab 3 Exercise D.2:**
```markdown
### D.2 — Build your own MCP server from scratch (🛠️ hands-on)

1. Create `agents/mcp_servers/activities_server.py`...
   
   📌 **Tip:** The `mcp[cli]` package provides the FastMCP decorator...

2. Run the server:
   ```bash
   python -m agents.mcp_servers.activities_server
   ```

   ✅ You should now see:
   ```
   MCP Server running on stdio
   ```
```

**Why it works:** Students scan for 🛠️ sections when they want hands-on work, 📖 sections when they're exploring, and ✅ checkpoints to verify progress.

### 3. Checkpoint Pattern (Verification)

Every hands-on step ends with a **checkpoint** — concrete output the student should see.

**Format:**
```markdown
✅ You should now see [SPECIFIC OUTPUT]:
```

**Examples:**

**Terminal output:**
```markdown
✅ You should now see:
```
Server running on http://127.0.0.1:8000
```
```

**File content:**
```markdown
✅ Open `.github/agents/test-author.agent.md` — you should see the YAML frontmatter with `name: test-author` at the top.
```

**UI state:**
```markdown
✅ Open the agent picker in Copilot Chat (top-left). You should see three new agents: `code-quality-reviewer`, `test-author`, and `endpoint-scaffolder`.
```

**Why it works:** Students know *immediately* if they succeeded. No guessing. If they don't see the expected output, they stop and debug before proceeding.

### 4. Hands-On vs. Read-Through Split

Not every feature needs hands-on practice. Use **read-through sections** (📖) for:

1. **Preview features** — e.g., Lab 3 Exercise E.3 (plugin install) because `chat.plugins.enabled` is often org-locked
2. **Friction-heavy installs** — e.g., Playwright MCP downloading browser binaries (~150MB)
3. **Org-managed settings** — e.g., Lab 3 Exercise B (permission picker) when students can't control the setting

**Example from Lab 3 Exercise E.3:**
```markdown
### E.3 — Install & verify (📖 read-through)

**Note:** Plugin installation requires the `chat.plugins.enabled` setting, which may be **org-managed**. If it's grayed out in your settings, contact your admin. This section shows what *would* happen when you install the plugin.

**What you'd see after installation:**
1. Agent appears in the picker: `my-mergington-plugin/test-author`
2. MCP server shows in **MCP: List Servers**: `my-mergington-plugin activities-mcp`
3. Tools available when you invoke the agent: `get_activities`, `search_policies`

**Troubleshooting common issues:**
- Invalid `name` field (slashes, colons) → silent failure
- Agent name mismatch between `plugin.json` and `.agent.md` → agent doesn't load
- MCP server not starting → check Python path in `.mcp.json`
```

**Why it works:** Students learn the *concept* without debugging org policies. They understand the structure (plugin.json, agent file, MCP config) even if they can't test it locally.

### 5. Prompt-Splitting for Feature Work

When teaching students to build features with Copilot, split the work into **multiple small prompts** instead of one large prompt.

**Example from Lab 3 Exercise A:**

**Instead of:**
```markdown
### Exercise A — Add two features (30 min)
Prompt: "Add a duplicate-email guard and a capacity check to the registration endpoint."
```

**Do this:**
```markdown
### Exercise A — Add features with scoped prompts

#### A.1 — Duplicate email guard (15 min)
Prompt: "Modify the `/api/v1/register` endpoint to reject duplicate emails. Return 409 Conflict if the email already exists."

✅ Run `pytest agents/tests/test_app.py -v` — the `test_duplicate_email` test should pass.

#### A.2 — Capacity check (15 min)
Prompt: "Add a capacity check to the registration endpoint. Reject registration if the cohort is full (30 students max). Return 400 Bad Request with message 'Cohort full'."

✅ Run `pytest agents/tests/test_app.py::test_capacity` — should pass.
```

**Why it works:**
1. Students internalize the "small, scoped prompt" pattern (convention C from Lab 3)
2. Each prompt has a clear verification step
3. If one prompt fails, students don't lose progress on the other
4. Mirrors real-world Copilot usage (iterative, not monolithic)

### 6. Continuity via Artifact Reuse

Within a single lab, **reuse artifacts** from earlier exercises instead of creating new examples.

**Example from Lab 3:**

- **Exercise C.3:** Students create `test-author.agent.md` custom agent
- **Exercise D.2:** Students create `activities_server.py` MCP server
- **Exercise E.2:** Students package *the same* `test-author` agent and `activities_server` into a plugin

**Why it works:**
- Students see the payoff of modular pieces
- Reduces cognitive load (don't learn a new example)
- Creates a narrative arc: build → use → bundle

### 7. Optional vs. Required Sub-Exercises

When an exercise has multiple parts, label them **REQUIRED** or **OPTIONAL**.

**Example from Lab 3 Exercise D:**
```markdown
### Exercise D — Model Context Protocol (MCP)

#### D.1 — Consume an existing MCP server (REQUIRED)
...

#### D.2 — Build your own MCP server from scratch (REQUIRED)
...

#### D.3 — Use an off-the-shelf MCP from a registry (OPTIONAL)
...

#### D.4 — Browser automation with the Playwright MCP (OPTIONAL)
...
```

**Why it works:**
- Students on a tight schedule skip optional sections
- Students with extra time explore deeper
- Clear signaling: "D.1 and D.2 are core, D.3 and D.4 are enrichment"

### 8. Code Blocks Are Copy-Paste-Ready

Every code block must be **runnable as-is**. No placeholders like `<your-name>`, no pseudocode, no "adapt this for your setup."

**Bad example:**
```bash
# Install dependencies
pip install -r <path-to-requirements>
```

**Good example:**
```bash
# Install dependencies
pip install -r agents/requirements.txt
```

**Why it works:**
- Students copy/paste without thinking
- Reduces friction — no "what do I replace?" questions
- Respects students' time — they're here to learn Copilot, not debug shell commands

### 9. Cross-Platform Callouts (Windows/macOS/Linux)

When commands differ across platforms, provide **variants inline** with 📌 callouts.

**Example from Lab 3 (venv activation):**
```markdown
2. Activate the virtual environment:

   **macOS/Linux:**
   ```bash
   source .venv/bin/activate
   ```

   **Windows (PowerShell):**
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   📌 **Windows note:** If you see a "script execution disabled" error, run:
   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   ```
```

**Why it works:**
- Windows users don't hit silent failures
- macOS/Linux users don't waste time reading Windows instructions (separate blocks)
- 📌 callout for the common Windows gotcha (execution policy)

### 10. Manual File Creation Over Command Palette

Direct students to **create files manually** (type the path, paste the content) instead of using VS Code's Command Palette (Cmd+Shift+P).

**Bad example:**
```markdown
1. Press Cmd+Shift+P (Ctrl+Shift+P on Windows)
2. Type "Create: New File"
3. Enter path `.github/agents/test-author.agent.md`
4. Paste the following content...
```

**Good example:**
```markdown
1. In VS Code, create a new file at `.github/agents/test-author.agent.md`
2. Paste the following content:
   ```markdown
   ---
   name: test-author
   description: Writes unit tests for existing Python code
   ---
   
   You are a test-writing specialist...
   ```
```

**Why it works:**
- Command Palette workflows vary across VS Code versions and extensions
- Manual creation works identically on Windows/macOS/Linux
- Simpler to write, simpler to follow

## Anti-Patterns

### ❌ No Checkpoints

```markdown
### Exercise B — Add a feature

1. Open `app.py`
2. Modify the `/register` endpoint
3. Run the tests

Move on to Exercise C.
```

**Problem:** Students don't know if they succeeded. What should the tests show?

**Fix:** Add `✅ You should now see: All 12 tests passed.`

### ❌ Ambiguous Instructions

```markdown
Run the app and check that it works.
```

**Problem:** "Works" is vague. What does success look like?

**Fix:**
```markdown
Run the app:
```bash
uvicorn agents.backend.app:app --reload
```

✅ Open http://127.0.0.1:8000/docs — you should see the FastAPI interactive docs with 5 endpoints listed.
```

### ❌ Re-Teaching Prior Labs

```markdown
### Exercise A — Create a custom instruction file

Custom instructions let you shape Copilot's behavior... [3 paragraphs explaining what Lab 2 already taught]
```

**Problem:** Wastes time, adds clutter.

**Fix:**
```markdown
### Exercise A — Create a custom instruction file

(Custom instructions were covered in Lab 2. We'll use them here for...)
```

### ❌ Introducing New Stacks Per Lab

```markdown
Lab 1: FastAPI app in `copilot-chat/agents/`
Lab 2: Express.js app in `customize-copilot/api/`
Lab 3: Django app in `agent-mode/backend/`
```

**Problem:** Students learn three frameworks, not Copilot patterns.

**Fix:** All labs use the same `agents/` FastAPI + vanilla JS app. Each lab adds to it.

## Examples

### Lab 3 Exercise C.2 (Read-Only Agent)

**Structure:**
- **C.2 heading** — clear title, 🛠️ emoji
- **Step 1:** Create file manually (convention D)
- **Frontmatter block:** Copy-paste-ready YAML (convention A)
- **System prompt block:** Copy-paste-ready content
- **Checkpoint 1:** File exists, frontmatter is valid
- **Step 2:** Invoke agent via chat
- **Prompt block:** Copy-paste-ready prompt
- **Checkpoint 2:** Agent responds, *doesn't* edit files
- **Sidebar:** 📌 explaining why `tools: ['read', 'search']` matters

### Lab 3 Exercise E.2 (Plugin Scaffolding)

**Structure:**
- **E.2 heading** — clear title, 🛠️ emoji
- **Step 1:** Create directory structure manually
- **Step 2:** Create `plugin.json` (copy-paste-ready)
- **Step 3:** Copy existing `test-author.agent.md` (reuse from C.3)
- **Step 4:** Create `.mcp.json` (copy-paste-ready)
- **Checkpoint:** Directory tree shown, students verify their structure matches
- **Sidebar:** 📌 noting production plugins would bundle runtime or document Python requirement

### Lab 1 Exercise (Interleaved Theory/Practice)

**Structure:**
- **Mini theory block** — "Agent Mode lets you delegate tasks. Here's the Plan Agent."
- **Hands-on step** — "Invoke Plan Agent with prompt X"
- **Checkpoint** — "You should see a 5-step plan in the chat"
- **Mini theory block** — "Agents loop until they solve the task. Here's the Stop button."
- **Hands-on step** — "Click Generate and watch the agent execute the plan"
- **Checkpoint** — "You should see 3 new commits in Git History"

**When to use:** When concepts are concrete and students benefit from immediate practice after each bite-sized theory chunk.

## Related Skills

- **Custom Agent Frontmatter Format** (`.squad/skills/custom-agent-frontmatter-format/`) — specific to agent files
- **Python Package Shadow** (`.squad/skills/python-package-shadow/`) — one of the repo hygiene rules applied in labs

## References

- Lab 1: `copilot-chat/README.md` (interleaved theory/practice model)
- Lab 2: `customize-copilot/README.md` (interleaved theory/practice model)
- Lab 3: `agents/README.md` (theory-first model, emoji legend, checkpoint pattern, reuse via continuity)
- Kaylee's history.md: conventions A-L (2026-04-21)

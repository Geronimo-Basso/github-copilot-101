# Lab 4 — Copilot CLI · Agenda v3 (Book-verified)

> Status: v3 — Book verified all CLI surface against shipping CLI v1.0.32 + official docs. Ready for Kaylee to build.
> Last updated: 2026-04-21
> Stack: existing `agents/` FastAPI + vanilla JS app (continuity with Labs 1–3)

---

## 1. Learning Objective

By the end of Lab 4, the learner will be able to:
- Use GitHub Copilot CLI interactively and programmatically
- Master slash commands, context management, and permission patterns
- Customize the CLI with custom agents, hooks, skills, and plugins
- Script headless workflows for automation and CI/CD

**Core differentiation:** Terminal-native AI assistant with scripting + plugin capabilities VS Code cannot provide.

---

## 2. Differentiation from Labs 1–3

| Lab | Topic | What Lab 4 does NOT re-teach |
|-----|-------|------------------------------|
| 1 | Copilot Chat in VS Code | Chat UI workflows, inline suggestions |
| 2 | Customization (instructions, skills, AGENTS.md) | Skill authoring (cite Lab 2), `.github/prompts/`, AGENTS.md syntax |
| 3 | Agent mode + custom agents + MCP + plugins (VS Code) | `.github/agents/` workspace agents, MCP server creation (cite Lab 3) |
| **4** | **CLI — terminal AI + scripting + customization** | VS Code-specific UI, inline completions |

---

## 3. Structure (Total: ~2.5 hours)

### Part 1 — Theory & Foundations (~15 min)
- What CLI is (terminal-native, device-flow auth)
- When to use CLI vs VS Code
- Interactive vs programmatic
- Slash commands overview

### Part 2 — Core CLI Usage (~50 min)
- Install + auth (multi-platform)
- Modes: `interactive` / `plan` / `autopilot`
- Context management (`@` syntax, `/context`, `/compact`, `/clear`)
- Slash commands deep dive (`/plan`, `/fleet`, `/research`, `/delegate`, `/chronicle`, `/skills`, `/yolo`)
- Permission flags + patterns

### Part 3 — Customization (~50 min)
- Custom instructions (CLI-side paths)
- Custom agents (`.agent.md` format)
- Hooks (📖 read-through — config skeleton + docs)
- Skills (CLI invocation — cite Lab 2 for authoring)
- Copilot memory via `/chronicle` (EXPERIMENTAL)
- CLI plugins (`/plugin` + marketplaces)
- MCP read-through (CLI config paths only)

### Part 4 — Programmatic & Automation (~20 min)
- Headless invocation (`copilot -p`)
- Scripting with `--output-format json`
- CI/CD use case (GitHub Actions snippet)

---

## 4. Part 1 — Theory & Foundations (~15 min)

### What Copilot CLI is (3 min)

Terminal-native AI assistant. Runs in bash/zsh/PowerShell. Device-flow auth on first run. Three modes: `interactive` (default REPL), `plan` (plan-only), `autopilot` (autonomous multi-turn).

### When to use CLI vs VS Code (5 min)

**Reach for CLI when:**
- SSH'd into a server, no IDE available
- CI/CD pipelines (GitHub Actions, Jenkins)
- Repo-wide refactors driven from shell
- Quick one-off tasks already in terminal
- Headless code review on PRs (scripted)

**Reach for VS Code when:**
- Multi-file inline editing with visual feedback
- Deep debugging with integrated tools
- Workspace agents tied to `.github/agents/`
- Real-time inline completions

### Interactive vs Programmatic (4 min)

```bash
# Interactive REPL
copilot

# Programmatic (one-shot, exits when done)
copilot -p "Generate tests for @agents/backend/app.py"

# JSON output for parsing in scripts
copilot -p "Summarize @agents/backend/" --output-format json
```

### Slash commands overview (3 min)

Short list, deep dive in Part 2:
- `/plan`, `/yolo`, `/fleet`, `/research`, `/delegate`, `/chronicle`, `/skills`, `/clear`, `/context`, `/compact`, `/undo`

---

## 5. Part 2 — Core CLI Usage (~50 min)

### Exercise A — Install + Auth + Hello World (🛠️ ~12 min)

**Multi-platform install:**

| Platform | Command |
|---|---|
| macOS (Homebrew) | `brew install copilot-cli` |
| macOS / Linux (npm) | `npm install -g @github/copilot` |
| Windows (winget) | `winget install GitHub.Copilot` |
| Windows (npm) | `npm install -g @github/copilot` |

**First run:**
```bash
cd agents/
copilot
```
- Trust folder prompt (managed via `trustedFolders` config)
- `/login` → device-flow auth (opens browser)
- First query: `What does @agents/backend/app.py do?`

✅ **Checkpoint:** CLI returns FastAPI app summary

### Exercise B — Context Management (🛠️ ~12 min)

**Add context with `@` mentions:**
```bash
> Explain @agents/backend/app.py             # single file
> What endpoints are in @agents/backend/?   # folder
> Review @. for security issues              # current directory
```

**Manage the context window:**
```bash
> /context        # show token usage and visualization
> /compact        # summarize history to free context
> /clear          # start new conversation (alias: /new)
> /undo           # rewind last turn (revert file changes)
```

> Note: There is **no** `/reset`, `/stop`, or natural-language "remove context" command. Manage scope via `@` mentions per message and use `/compact` or `/clear` to reduce window pressure.

✅ **Checkpoint:** Use `@` mentions across multiple turns and run `/context` to inspect usage.

### Exercise C — Slash Commands Deep Dive (🛠️ ~15 min)

| Command | Purpose | Example |
|---------|---------|---------|
| `/plan` | Create implementation plan | `/plan Build waitlist feature` |
| `/yolo` | Allow all tools, paths, URLs | `/yolo Refactor auth and run tests` |
| `/fleet` | Parallel subagent execution | `/fleet Review backend, frontend, tests` |
| `/research` | Deep investigation (GitHub + web) | `/research Best rate limiting approaches` |
| `/delegate` | Send session to GitHub → creates a PR | `/delegate Refactor auth and open PR` |
| `/chronicle` | Session insights (**EXPERIMENTAL**) | `/chronicle standup` |
| `/skills` | List/info/add/remove/reload skills | `/skills list` |

**Notes:**
- `/delegate` does **not** invoke local sub-agents. It hands the session to GitHub's cloud agent which opens a PR. For local parallel work use `/fleet`.
- Skills are **invoked** via `@skill:skill-name` mentions in prompts, not via a `/skills` subcommand.
- `/chronicle` requires enabling experimental features first: `/experimental on` (covered in Part 3).

**Practice task:**
Use `/plan` → review → execute → `/research` to investigate a tricky design choice.

✅ **Checkpoint:** Successfully chain at least three slash commands for a real task.

### Exercise D — Permission Flags & Patterns (🛠️ ~8 min)

The CLI uses **permission patterns** of the form `tool` or `tool(arg)`:
- `bash`, `write`, `view`, `edit`, `web_fetch` — bare tool names
- `shell(git push)` — specific shell command
- `shell(git:*)` — all git subcommands
- `MyMCP(tool_name)` — specific MCP server tool
- `url(github.com)` — URL access by domain

**Examples:**
```bash
# Allow all tools (no prompts)
copilot --allow-all-tools

# Deny destructive git operations
copilot --deny-tool='shell(git push)' --deny-tool='shell(git reset --hard)'

# Allowlist read-only operations
copilot --allow-tool=view --allow-tool='shell(git:*)' --deny-tool=write

# Allow a specific MCP tool
copilot --allow-tool='github-mcp-server(create_issue)'
```

✅ **Checkpoint:** Run a task with a deny-list that blocks `shell(git push)` and observe the prompt.

### Exercise E — Multi-Turn Autonomous Task (🛠️ ~3 min)

Build the waitlist feature (waitlist endpoint + frontend "Join Waitlist" button when full).

```bash
copilot --mode autopilot -i "Build a waitlist feature in @agents/. Add backend endpoint and frontend button when activity is full."
```

Use `/undo` (or `/rewind`) if the agent drifts and you want to revert the last turn.

✅ **Checkpoint:** Waitlist feature works (31st student sees "Join Waitlist").

---

## 6. Part 3 — Customization (~50 min)

### Custom Instructions — CLI paths (🛠️ ~5 min)

| Scope | Path |
|---|---|
| User | `~/.copilot/copilot-instructions.md` |
| Repo | `.github/copilot-instructions.md` |

> Both paths use `.github/` at the repo level — **not** `.copilot/`. Cite Lab 2 for authoring patterns.

✅ **Checkpoint:** Add a one-liner to `~/.copilot/copilot-instructions.md` and observe it in the next CLI response.

### Custom Agents (🛠️ ~15 min)

**Location:** `~/.copilot/agents/` (user-level only, per locked decision Q3)
**File extension:** `*.agent.md` (the `.agent` infix is required — files without it are ignored)

**Format:**
```yaml
---
name: fastapi-code-reviewer
description: "Specialized code review agent for FastAPI codebases. Use when reviewing backend Python code for security, validation, and FastAPI best practices."
---

You are a code review specialist focusing on:
- FastAPI best practices
- Input validation and Pydantic models
- Security vulnerabilities (auth, injection, secrets)
- Test coverage gaps

Always provide specific file paths and line numbers, plus an actionable fix per finding.
```

> The `tools` field is not required by the CLI — agents inherit available tools from the session. Only `name` and `description` are confirmed required.

**Create the file manually:**
```bash
mkdir -p ~/.copilot/agents
# Open ~/.copilot/agents/fastapi-code-reviewer.agent.md in your editor and paste the above.
```

**Invoke:**
```bash
copilot
> @fastapi-code-reviewer Review @agents/backend/app.py
```

You can also browse agents with `/agent`.

✅ **Checkpoint:** Custom agent applies the FastAPI lens and identifies at least one specific issue.

### Hooks (📖 ~5 min — read-through)

Hooks are a real CLI feature. Configuration locations:

| Scope | Location |
|---|---|
| User | `hooks` key in `~/.copilot/config.json` |
| Repo | `.github/hooks/*.json` |

**Skeleton (event types are under-documented at time of writing — refer to current docs):**
```json
{
  "hooks": {
    "event-name": {
      "command": "/path/to/script.sh",
      "description": "What this hook does"
    }
  }
}
```

**Disable globally:** `"disableAllHooks": true` in config.

> Lab 4 keeps hooks as read-through. Once you've identified an event type in your version of the CLI, the syntax above plugs in directly.

### Skills — CLI Invocation (🛠️ ~5 min)

```bash
> /skills list                               # see available skills
> /skills info <skill-name>                  # details
> @skill:fastapi-best-practices Review this endpoint
```

Cite Lab 2 for skill authoring. Lab 4 covers invocation only.

✅ **Checkpoint:** Invoke at least one skill via `@skill:` syntax.

### Copilot Memory via `/chronicle` (🛠️ ~7 min — EXPERIMENTAL)

`/chronicle` is **experimental** — enable it first:

```bash
> /experimental on
```

**Subcommands:**
| Command | Purpose |
|---|---|
| `/chronicle standup` | Generate a standup report from recent sessions |
| `/chronicle tips` | Personalized CLI usage tips based on your history |
| `/chronicle improve` | Analyze session history → propose custom-instructions improvements |
| `/chronicle reindex` | Rebuild session store from history |

**Storage:** `~/.copilot/session-state/` (JSONL) + `~/.copilot/session-store.db` (SQLite). All local.

**Practice:**
```bash
> /experimental on
> /chronicle standup
> /chronicle improve
```

✅ **Checkpoint:** `/chronicle improve` proposes at least one custom-instructions edit you find useful.

### CLI Plugins (🛠️ ~7 min)

The CLI has its **own** plugin system (separate from VS Code's). Plugins can bundle custom agents (`*.agent.md`), skills (`SKILL.md`), hooks, MCP configs, and LSP configs.

**Default marketplaces:**
- `github/copilot-plugins`
- `github/awesome-copilot`

**Management commands:**
```bash
> /plugin list                               # show installed
> /plugin marketplace                        # browse marketplaces
> /plugin install <name>                     # install
> /plugin uninstall <name>                   # remove
> /plugin update                             # update all
```

Or from outside a session: `copilot plugin <subcommand>`.

✅ **Checkpoint:** List installed plugins and inspect at least one marketplace entry.

### MCP — CLI config paths (📖 ~5 min — read-through)

| Scope | Path |
|---|---|
| User | `~/.copilot/mcp-config.json` |
| Repo | `.github/mcp.json` |

> Different from VS Code (`.vscode/mcp.json`) and different from what you might expect. Note `mcp-config.json` for user, plain `mcp.json` for repo.

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"]
    }
  }
}
```

Cite Lab 3 for MCP server authoring.

✅ **Checkpoint:** Locate `~/.copilot/mcp-config.json` and identify one configured server.

---

## 7. Part 4 — Programmatic & Automation (~20 min)

### Exercise F — Headless Invocation (🛠️ ~8 min)

```bash
# One-shot, exits when done
copilot -p "Generate tests for @agents/backend/app.py"

# JSON output (one JSON object per line — JSONL)
copilot -p "Summarize @agents/backend/" --output-format json

# Combine with permission patterns for safety in scripts
copilot -p "Review @agents/backend/ for security issues. Write to review.md" \
  --allow-tool=write --deny-tool='shell(git push)'
```

**Scripting pattern:**
```bash
#!/bin/bash
copilot -p "Review @agents/backend/ for security. Write report to review-report.md" \
  --allow-all-tools
cat review-report.md
```

✅ **Checkpoint:** Script generates `review-report.md` autonomously.

### Exercise G — CI/CD Integration (🛠️ ~12 min)

GitHub Actions snippet (read-through, not deployed):

```yaml
name: Copilot Code Review
on: [pull_request]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Copilot CLI
        run: npm install -g @github/copilot
      - name: Review PR
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          copilot -p "Review the diff in this PR for security and best practices. Write to review.md" \
            --allow-all-tools \
            --output-format json
          cat review.md >> $GITHUB_STEP_SUMMARY
```

**Use cases:**
- PR reviews
- Pre-commit checks
- Scheduled codebase audits
- Test generation in CI

✅ **Checkpoint:** Learner can describe how to authenticate the CLI in a workflow and how `--output-format json` enables downstream parsing.

---

## 8. What We Skip (and where it's covered)

| Topic | Where it was taught |
|-------|---------------------|
| Custom instructions (theory + authoring) | Lab 2 |
| Prompt files (`.github/prompts/`) | Lab 2 |
| Skills (authoring) | Lab 2 |
| `AGENTS.md` | Lab 2 |
| MCP server creation | Lab 3 |
| VS Code custom agents (`.github/agents/`) | Lab 3 |
| VS Code agent plugins | Lab 3 |

---

## 9. Risks Tracked

1. **Install friction** — fallback: Codespace
2. **Auth blocked by org SSO** — pre-lab check, allow personal account
3. **Terminal differences** (bash/zsh/PowerShell) — platform callouts
4. **`/chronicle` requires `/experimental on`** — call it out explicitly in Part 3
5. **Hook event types under-documented** — kept as read-through with skeleton
6. **Permission patterns are unfamiliar** — provide the table in Ex D

---

## 10. Open Questions Decided (LOCKED — preserve through edits)

| # | Question | Decision |
|---|----------|----------|
| 1 | Sample app | Keep `agents/` (continuity) |
| 2 | Install scope | Multi-platform (macOS + Linux + Windows) in Ex A |
| 3 | Custom agent paths | User-level only (`~/.copilot/agents/`) |
| 4 | Exercise F (scripting) | **Core**, not optional — CLI's killer feature |
| 5 | MCP coverage | Brief 📖 read-through showing config-path difference, no hands-on |
| 6 | `/chronicle` coverage | Keep in lab — show `/experimental on` flow + 1–2 chronicle commands |
| 7 | Hooks coverage | Read-through only — config skeleton + docs cite, no hands-on |

---

## 11. Next Steps

1. ✅ **Book:** verification complete (see `.squad/decisions/inbox/book-lab4-cli-verification.md`)
2. **Kaylee:** write full lab to `copilot-cli/README.md` following this v3 structure
3. **Zoe:** review Kaylee's draft → Geronimo final approval → ship

---

## Appendix — v3 Revision Notes (2026-04-21, post-Book)

Corrections applied from Book's verification report:

1. Modes: `ask`/`task`/`develop` → **`interactive`/`plan`/`autopilot`**
2. One-shot syntax: `copilot ask`/`copilot task` → **`copilot -p`** (and `-i` for interactive with prompt)
3. Install: brew formula `copilot-cli`, npm package `@github/copilot`, winget `GitHub.Copilot`
4. JSON flag: `--output json` → **`--output-format json`**
5. Custom agents: file extension is **`.agent.md`**, not `.md`
6. Custom-instructions repo path: **`.github/copilot-instructions.md`** (not `.copilot/`)
7. MCP paths: **`~/.copilot/mcp-config.json`** (user) + **`.github/mcp.json`** (repo)
8. `/delegate` clarified: creates a PR via GitHub cloud agent (not local sub-agent)
9. `/stop` and `/reset` removed (don't exist); added `/clear`, `/undo`, `/compact`, `/context`
10. `/chronicle` marked EXPERIMENTAL with `/experimental on` requirement; added subcommand table
11. Skills invocation: **`@skill:name`** in prompts (not `/skills invoke`)
12. Permission patterns: replaced fictional `runCommands`/`editFiles` examples with real patterns (`shell(...)`, `write`, `view`, `MyMCP(tool)`, `url(...)`)
13. Hooks: confirmed real, kept as read-through per locked decision Q7
14. Plugins: documented CLI's own plugin system (`/plugin` + marketplaces), separate from VS Code

Style maintained from v2: code + checkpoints over prose, no overexplanation.

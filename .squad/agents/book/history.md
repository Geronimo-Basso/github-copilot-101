# Project Context

- **Owner:** Geronimo Basso
- **Project:** github-copilot-101 — a repository of hands-on labs (90 min each, theory + practice) teaching GitHub Copilot. Existing lab examples live in `customize-copilot/` and `copilot-chat/`.
- **Stack:** Markdown labs, sample code in various languages, repo-as-curriculum
- **Created:** 2026-04-20T09:46:24Z

## Learnings

<!-- Append new learnings below. Each entry is something lasting about the project. -->

## Core Context: Platform Facts & References (Canonical as of 2026-04-21)

### VS Code Copilot Chat modes
- The three modes are: **Ask**, **Plan**, and **Agent**.
- "Edit mode" was renamed to **Plan mode**. Never refer to it as Edit again.

### Custom agents (VS Code Copilot Chat)
- File location: `.github/chatmodes/{name}.chatmode.md` (project-scoped) or per-user.
- Required YAML frontmatter format (per official GitHub docs):
  ```
  ---
  name: kebab-case-name
  description: One-sentence purpose
  tools: ['read', 'search', 'edit']
  ---
  ```
- The `name` field is REQUIRED. Lab content that omits it is wrong.

### Copilot CLI permission management
- `/yolo` slash command grants full permissions in CLI agent mode (skip per-action prompts).
- The in-editor permission picker (dropdown UI in Agent Mode) is the GUI equivalent for VS Code.

### VS Code agent plugins (Preview)
- Gated by setting: `chat.plugins.enabled` (often org-managed).
- A plugin can bundle: custom agents (chatmode.md files) + MCP servers + tools.

### MCP servers in VS Code
- Configured via `.vscode/mcp.json`.
- `workspaceFolder` resolves to the repo root, not the script's parent directory — watch for path resolution gotchas.
- Use stdio transport for local Python MCP servers built with `mcp[cli]`.

### Python package shadow gotcha
- Never name a local Python package the same as a PyPI dependency (e.g., a folder named `mcp/` shadows the installed `mcp` package).
- See .squad/skills/python-package-shadow/SKILL.md for recovery pattern.

### GitHub Copilot CLI (v1.0.32 reference)

**CLI file structure:**
```
~/.copilot/
├── config.json                    # user-level config, hooks inline
├── copilot-instructions.md        # user-level custom instructions
├── mcp-config.json                # user-level MCP servers
├── agents/*.agent.md              # user-level custom agents
├── session-state/                 # session JSONL files
└── session-store.db               # SQLite session index

.github/                           # repo-level
├── copilot-instructions.md        # repo-level custom instructions
├── mcp.json                       # repo-level MCP servers
└── hooks/*.json                   # repo-level hook definitions
```

**Verified facts:**
- Modes: `interactive` / `plan` / `autopilot` (NOT ask/task/develop)
- One-shot syntax: `copilot -p "prompt"` (programmatic) or `copilot -i "prompt"` (interactive start)
- Context: managed via `/context` (view), `/compact` (reduce), `/clear` (reset). Add via `@file` mentions.
- Install: Homebrew `copilot-cli`, npm `@github/copilot`
- Auth: device-flow via `/login`
- Slash commands confirmed: `/plan`, `/yolo`, `/fleet`, `/research`, `/skills`, `/chronicle` (experimental)
- Context syntax: `@file`, `@folder/`, `@.`
- Permission flags: `--allow-all-tools`, `--deny-tool`, `--allow-tool`
- Hooks are real: configured in `config.json` or `.github/hooks/*.json`
- Plugins have full surface: `/plugin` commands, marketplaces, can bundle agents + skills + hooks + MCP

---

### 2026-04-21 — Lab 4 Q&A section: Plan mode vs /plan command distinction

- **Task:** Add Q&A section to Lab 4 README distinguishing CLI's Plan mode from the `/plan` slash command.
- **Research sources:** GitHub Copilot CLI docs, local CLI help
- **Key distinction confirmed:**
  - **Plan mode** = persistent interactive state, toggled with `Shift+Tab` or started with `copilot --plan`. All prompts in this mode generate structured plans before execution.
  - **`/plan` slash command** = one-off request within any mode (interactive/autopilot). Creates a single plan without changing the session mode.
- **Output:** Added Q&A section to `copilot-cli/README.md` (after Part 4), updated TOC. Committed in `f1c02da`.

### 2026-04-20 — Agent Mode capability inventory for Lab 3
- Produced authoritative inventory at `.squad/decisions/inbox/book-agent-mode-inventory.md` (sources: code.visualstudio.com/docs/copilot).
- Key corrections: "Plan mode ≠ renamed Edit"; custom agents now in `.github/agents/*.agent.md`; `infer:` frontmatter deprecated.
- Lab 3 scope recommendation ranked: (1) Agent loop with multi-file edit + terminal, (2) Permission levels, (3) MCP integration, (4) Custom agents.

### 2026-04-20 — MCP block proposal for Lab 3 (reference repo lift)
- Studied Geronimo's own `lab-06-mcp/` reference (README-only, learner-authored).
- Reference scope ~75–90 min; Lab 3 budget = 25 min. Recommendation: asymmetric 7/15/3-min split (consume / create / wrap).
- Consume = filesystem MCP via npx. Create = `agents/mcp/activities_server.py` exposing `list_activities` + `get_signups_count`.
- Flagged module-shadow risk (later fixed by Kaylee: renamed to `agents/mcp_servers/`).

### 2026-04-21 — Lab 3 Exercise D MCP server module shadow fix
- Kaylee deployed fix: renamed `agents/mcp/` → `agents/mcp_servers/` (post-QA).
- No action needed; MCP proposal remains sound.

### 2026-04-21 — Lab 3 Exercise E (Plugin Capstone) shipped
- Kaylee added optional Exercise E: Package agents and MCP servers as VS Code plugin.
- Three sub-exercises: E.1 theory, E.2 hands-on scaffold, E.3 discovery/distribution. Committed `1cfde5a`.


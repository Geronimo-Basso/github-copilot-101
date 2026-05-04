# Project Context

- **Owner:** Geronimo Basso
- **Project:** github-copilot-101 — a repository of hands-on labs (90 min each, theory + practice) teaching GitHub Copilot. Existing lab examples live in `customize-copilot/` and `copilot-chat/`.
- **Stack:** Markdown labs, sample code in various languages, repo-as-curriculum
- **Created:** 2026-04-20T09:46:24Z

## Learnings

<!-- Append new learnings below. Each entry is something lasting about the project. -->


## 2026-04-20 — Lab 3 hands-on design

- Read `agents/` codebase (FastAPI + vanilla JS school activities app). Found 10 concrete improvement opportunities; key bugs: no duplicate-signup guard, no capacity check, orphan `activities.json` not read by `app.py`, no tests, signup via query-string instead of body.
- Designed 3 cumulative hands-on exercises (~55 min): (1) multi-file bug fix + pytest scaffold, (2) plan-first end-to-end "unregister" feature across backend + frontend + tests, (3) custom chatmode `endpoint-scaffolder` at `.github/chatmodes/endpoint-scaffolder.chatmode.md` with constrained tool list. Stretch Exercise 4 = MCP, gated on Book confirming environment.
- Wrote 5 agent-mode-specific prompting patterns (plan-first, verify-by-running, constrain-blast-radius, checklist, diff-before-commit) each with before/after examples drawn from this codebase.
- 6 open questions parked for Book — chatmode syntax/path, terminal access default, MCP availability, plan/approve UX, auto-approve defaults, Lab-2-vs-Lab-3 skills/chatmode boundary.
- Output: `.squad/decisions/inbox/river-lab3-handson-design.md`.

### 2026-04-21 — Lab 3 Exercise D MCP server module shadowing resolved

Lab 3 Exercise D went live but discovered a latent bug: `agents/mcp/` shared a name with the installed `mcp` PyPI package; when Python ran from inside `agents/`, CWD on `sys.path` shadowed the installed package. Kaylee fixed by renaming to `agents/mcp_servers/`. **No test path impact** — all your pytest cases remain rooted at the workspace level (`.pytest` discovery finds `agents/tests/`), not affected by the rename. Your handson patterns are all still good.

## Platform facts confirmed during Lab 3 (2026-04-21)

These are facts about Copilot surfaces that came up repeatedly during the Lab 3 build cycle. Use these as the canonical reference until contradicted by official docs.

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
- No additional /permission-style slash commands have been confirmed in stable releases as of this audit.

### VS Code agent plugins
- Status: **Preview** as of Lab 3 build.
- Gated by setting: `chat.plugins.enabled` (often org-managed).
- Plugin manifest field reference: name, displayName, description, version, contributes (chatModes, mcpServers, tools).
- A plugin can bundle: custom agents (chatmode.md files) + MCP servers + tools. This is the "package and ship" story.

### MCP servers in VS Code
- Configured via `.vscode/mcp.json`.
- `workspaceFolder` resolves to the repo root, not the script's parent directory — watch for path resolution gotchas when the script lives in a subfolder.
- Use stdio transport for local Python MCP servers built with `mcp[cli]`.

### Module-shadow gotcha (relevant when MCP code is in lab samples)
- Never name a local Python package the same as a PyPI dependency (e.g., a folder named `mcp/` shadows the installed `mcp` package).
- See .squad/skills/python-package-shadow/SKILL.md for the recovery pattern.

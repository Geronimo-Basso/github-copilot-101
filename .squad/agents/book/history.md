# Project Context

- **Owner:** Geronimo Basso
- **Project:** github-copilot-101 — a repository of hands-on labs (90 min each, theory + practice) teaching GitHub Copilot. Existing lab examples live in `customize-copilot/` and `copilot-chat/`.
- **Stack:** Markdown labs, sample code in various languages, repo-as-curriculum
- **Created:** 2026-04-20T09:46:24Z

## Learnings

<!-- Append new learnings below. Each entry is something lasting about the project. -->

### 2026-04-21 — Lab 4 Q&A section: Plan mode vs /plan command distinction

- **Task:** Add Q&A section to Lab 4 README distinguishing CLI's Plan mode from the `/plan` slash command.
- **Research sources:** 
  - [About GitHub Copilot CLI - Modes of use](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli#modes-of-use)
  - [Use GitHub Copilot CLI - Use plan mode](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli#use-plan-mode)
  - Local CLI help (`copilot --help`)
- **Key distinction confirmed:**
  - **Plan mode** = persistent interactive state, toggled with `Shift+Tab` or started with `copilot --plan`. All prompts in this mode generate structured plans before execution. Asks clarifying questions.
  - **`/plan` slash command** = one-off request within any mode (interactive/autopilot). Creates a single plan without changing the session mode.
- **Output:** Added Q&A section to `copilot-cli/README.md` (after Part 4, before "What's Next?"), updated TOC. Committed in `f1c02da`.
- **Format established:** Q&A section uses: Short answer up front → comparison bullets → "📌 When to use which" closer → cited sources (URLs). Matches Lab 4 voice (concise, learner-friendly, bold/code formatting).


## 2026-04-20 — Agent Mode capability inventory for Lab 3
- Requested by Geronimo Basso. Produced authoritative inventory at `.squad/decisions/inbox/book-agent-mode-inventory.md`.
- Sources: code.visualstudio.com/docs/copilot (agents/overview, agents/local-agents, agents/agent-tools, customization/custom-chat-modes, customization/custom-instructions, customization/mcp-servers, chat/chat-agent-mode), all accessed 2026-04-20.
- Key corrections flagged for the lab:
  - "Plan mode = renamed Edit" is **wrong**. Edit is deprecated (`chat.editMode.hidden`); Plan is a distinct built-in agent.
  - Custom agents now live in `.github/agents/*.agent.md` (not `.github/chatmodes/`); `infer:` frontmatter deprecated → use `user-invocable` / `disable-model-invocation`.
  - Permission levels are 3-tier: Default Approvals / Bypass Approvals / Autopilot (Preview).
- Lab 3 scope recommendation (ranked, non-overlapping with Lab 2): (1) Agent loop with multi-file edit + terminal + test iteration, (2) Permission levels, (3) MCP integration in Agent, (4) Custom agents with Plan→Implementation handoff.
- Deferred to future labs: Cloud/CLI agents, subagents, hooks, third-party agents, BYOK.

## 2026-04-20 — MCP block proposal for Lab 3 (reference repo lift)
- Requested by Geronimo Basso. Studied his own `Geronimo-Basso/github-copilot-workshops-labs-python` → `lab-06-mcp/`.
- Reference lab is README-only (no committed `server.py`/`client.py`/`.vscode` files); learner authors everything inline. Source: <https://github.com/Geronimo-Basso/github-copilot-workshops-labs-python/tree/main/lab-06-mcp>.
- Reference scope = build `FastMCP` server (math tools + greeting resource) + Python stdio client + `.vscode/mcp.json` registration + consume Playwright MCP (NBA scrape) + consume Microsoft Learn MCP. Total ~75–90 min — 3× our 25-min Lab 3 budget.
- Reusable: `FastMCP` skeleton (README §3), `@mcp.tool()` pattern (§4), `.vscode/settings.json` discovery flag (§9.2), `.vscode/mcp.json` stdio block (§9.4), "click ▶ in mcp.json" UX flow (§9.5).
- Dropped: client.py (learners aren't MCP hosts), Playwright NBA exercise (stack/scope mismatch), math tools (don't show MCP's value — agent can already add), `mcp dev` Inspector (extra port/token dance), MS Learn prompt set (off-topic for activities app).
- Recommendation written to `.squad/decisions/inbox/book-mcp-block-proposal.md`: asymmetric 7/15/3-min split (consume / create / wrap). Consume = filesystem MCP via npx scoped to `agents/sample-data/`. Create = `agents/mcp/activities_server.py` exposing `list_activities` + `get_signups_count` against the existing in-memory dict.
- Open Q flagged for Zoe: does Lab 3 env guarantee Node.js for the `npx` consume path, or do we go Python-only (Microsoft Learn MCP) to single-stack the dependencies?

### 2026-04-21 — Lab 3 Exercise D MCP server module shadow fix

Kaylee deployed a post-QA fix: renamed `agents/mcp/` → `agents/mcp_servers/` to fix Python import shadowing where `import mcp` from inside `agents/` resolved to the local directory instead of the installed `mcp` PyPI package. This was a latent bug in the MCP block's proposal (Book had written `agents.mcp.activities_server` in `.vscode/mcp.json` without catching the shadowing risk). **No action needed** — Kaylee owns the fix; your MCP proposal is otherwise solid and the `mcp_servers/` rename fits your asymmetric consume/create design perfectly.

### 2026-04-21 — Lab 3 Exercise E (Plugin Capstone) shipped

Kaylee added Exercise E as the final hands-on capstone for Lab 3: **Package agents and MCP servers as a VS Code plugin**. Three sub-exercises teach students to understand plugin structure (E.1), scaffold a `my-mergington-plugin/` folder with `plugin.json` + agent + MCP reference (E.2), and understand VS Code plugin discovery/distribution (E.3). Exercise E is optional depth (~20 min), positioned after Exercise D. Reuses existing artifacts (agent from C.3, MCP reference from D.2); no new code. Committed in `1cfde5a`. Full decision rationale and preview status gotchas documented in `.squad/decisions.md`. You may want to verify plugin facts align with current VS Code docs when planning Lab 4 or follow-up materials.

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

## 2026-04-21 — Lab 4 CLI verification (28 claims)

Geronimo requested full fact-check of the Lab 4 agenda against shipping GitHub Copilot CLI v1.0.32. The agenda was drafted using the external repo `github/copilot-cli-for-beginners` as reference, which appears to use outdated/incorrect terminology.

**Sources:** Local CLI v1.0.32 (`copilot --help` and all help subcommands), official GitHub docs (install, chronicle, plugins, CLI reference, custom instructions), Homebrew, npm registry.

**Key corrections delivered to `.squad/decisions/inbox/book-lab4-cli-verification.md`:**

### Critical errors found (6 claims wrong)
1. **Modes** — Agenda claims `ask` / `task` / `develop`. WRONG. Actual modes: `interactive` / `plan` / `autopilot`.
2. **One-shot syntax** — Agenda claims `copilot ask "..."` and `copilot task "..."`. WRONG. Actual: `copilot -p "prompt"` (programmatic) or `copilot -i "prompt"` (interactive start).
3. **Context management** — Agenda claims natural language "Add context: @file" commands. WRONG. Context is added via `@file` mentions in prompts; managed via `/context` (view usage), `/compact` (reduce), `/clear` (reset). No explicit add/remove commands.
4. **Custom instructions paths** — Agenda claims project path is `.copilot/copilot-instructions.md`. WRONG. Correct: `.github/copilot-instructions.md`.
5. **MCP paths** — Agenda claims `~/.copilot/mcp.json` and `.copilot/mcp.json`. WRONG. Correct: `~/.copilot/mcp-config.json` (user) + `.github/mcp.json` (repo).
6. **Reset command** — Agenda references `/reset`. WRONG. No `/reset` command exists. Use `/clear` (new conversation), `/undo` or `/rewind` (undo last turn), `/compact` (reduce context).

### Partial corrections (8 claims)
- Install commands: brew is `copilot-cli` (not `github-copilot-cli`), npm is `@github/copilot` (not `@github/copilot-cli`)
- `--output json` should be `--output-format json`
- `/delegate` exists but does NOT invoke sub-agents — it delegates to GitHub cloud agent for PR creation
- `/chronicle` exists but is EXPERIMENTAL (requires `/experimental on` first)
- `/skills` exists with subcommands `list|info|add|remove|reload`, but invocation is via `@skill:name` mentions (not `/skills invoke`)
- Custom agent file extension is `.agent.md` (not `.md`)
- Frontmatter schema: `name` and `description` confirmed; `tools` field unclear/optional
- Tool names: agenda used old names (`runCommands`, `editFiles`, `codebase`); actual names differ (`bash`, `create`, `view`, `grep`, `web_fetch`, etc.)

### Confirmed features (12 claims)
- Device-flow auth via `/login` ✅
- Trust folder prompt ✅
- `/plan`, `/yolo`, `/fleet`, `/research`, `/skills` all exist ✅
- `@file`, `@folder/`, `@.` context syntax ✅
- Permission flags: `--allow-all-tools`, `--deny-tool`, `--allow-tool` ✅
- Custom agents location `~/.copilot/agents/*.agent.md` ✅
- User-level custom instructions `~/.copilot/copilot-instructions.md` ✅

### New discoveries
1. **Hooks are real!** Configured via `hooks` key in `~/.copilot/config.json` (user) or `.github/hooks/*.json` (repo). Event-driven, keyed by event name. Config help confirms: "inline hook definitions, keyed by event name (same schema as .github/hooks/*.json)". Specific event types need further research.
2. **CLI plugins** are a full feature surface with `/plugin` commands, marketplaces (`github/copilot-plugins`, `github/awesome-copilot` added by default), and can bundle agents + skills + hooks + MCP configs + LSP configs. NOT equivalent to VS Code plugins — separate CLI-native architecture.
3. **Chronicle is powerful** — `/chronicle standup`, `/chronicle tips`, `/chronicle improve`, `/chronicle reindex`. All session data stored locally in `~/.copilot/session-state/` (JSONL) + `~/.copilot/session-store.db` (SQLite). Enables questions about coding history. Currently experimental.

### CLI file structure canonical reference (as of v1.0.32)
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

**Recommendation to team:** The external repo `github/copilot-cli-for-beginners` should not be trusted as a reference for current CLI behavior. Always verify against `copilot --help` and official docs.github.com/copilot URLs.

**Lab 4 readiness:** ~60% accurate before corrections. After applying the 28 fixes, lab will be solid. Blocking issues are mode names and paths. Once fixed, the lab structure is excellent and covers the full CLI surface well.

## 2026-04-21 — Lab 4 CLI verification (28 claims, 12✅ 8⚠️ 6❌ 2❓)

Verified all 28 CLI facts from the Lab 4 agenda against GitHub Copilot CLI v1.0.32 (local + official docs). Produced comprehensive report in `.squad/decisions/inbox/book-lab4-cli-verification.md` with:
- **12 facts confirmed ✓** (modes, install, auth, slash commands, hooks, MCP, plugins)
- **8 facts partial ⚠️** (package names, paths, deprecations)
- **6 facts corrected ❌** (mode names are interactive/plan/autopilot not ask/task/develop; one-shot syntax; JSON flag; custom-agent extension; config paths; context commands)
- **2 facts unresolved ❓** (prompt composition, programmatic API)

Key corrections applied to AGENDA.md v3 by Coordinator before Kaylee authoring. Lab 4 README now references verified facts; Lab 4 in final review with Zoe.

**Status:** Verification complete, handoff to Kaylee/Zoe satisfied.

# Project Context

- **Owner:** Geronimo Basso
- **Project:** github-copilot-101 — a repository of hands-on labs (90 min each, theory + practice) teaching GitHub Copilot. Existing lab examples live in `customize-copilot/` and `copilot-chat/`.
- **Stack:** Markdown labs, sample code in various languages, repo-as-curriculum
- **Created:** 2026-04-20T09:46:24Z

## Core Context (Lab 3 & Earlier)

### Lasting Lab 3 Insights (summarized from full history)

**Lab 3 scope:** Agent loop + permission levels + MCP consume+create + custom agents + plugin packaging.

**Key learnings that affect Lab 4 and beyond:**
1. **Lab 1–3 continuity via `agents/` app reuse.** Lab 1 ships a basic endpoints (students + signup). Lab 3 adds MCP integration. Any new lab reusing this app must coexist with existing data model + endpoints.
2. **Custom-agent frontmatter is strict YAML.** Every agent must have: `name` (kebab-case, required), `description`, `tools` list. No optional `infer:` field — use `user-invocable` + `disable-model-invocation` instead.
3. **Intro labs keep agents simple.** Lab 3 avoided multi-agent orchestration (save for advanced lab). Each agent does ONE thing: permission enforcement, test authoring, code review.
4. **Windows blindspot fixed.** Always include platform-specific paths/commands. Lab 3 originally had POSIX venv path in `.vscode/mcp.json` which silently broke on Windows. Now: split `python3`/`python`, add PowerShell equivalents, mark Windows callouts explicitly.
5. **Manual file creation > Command Palette.** Avoid `Cmd+Shift+P` flows — less reproducible. Have students type file paths and paste content in the editor.
6. **Read-through for preview/fiddly features.** Use 📖 (read) vs 🛠️ (hands-on) to distinguish. Lab 3 Exercise B (permissions, often org-managed) and E.3 (plugin install, preview) used read-through to teach concepts without debugging environment policies.
7. **Time budget is flexible (quality over 90 min).** Build the right-sized lab. Lab 3 landed at ~100-110 min with all exercises. Always provide per-exercise time estimates so students know the commitment.
8. **.vscode/ is tracked, .squad/ is gitignored.** Lab 3 added `settings.json` + `mcp.json` to .vscode/ and they now live in the repo. Future labs: merge changes into existing files, never clobber.
9. **No scope re-teaching.** Lab 2 taught custom instructions + skills + AGENTS.md. Lab 3 skipped all of those and cited "previously covered in Lab N." Lab 4 must audit prior labs before scoping.
10. **Theory-first model works.** All theory in Part 1 (~15 min), hands-on in Parts 2–4. Reuse this structure for future labs. Emoji legend: 🛠️ (hands-on), 📖 (read), ✅ (checkpoint), 📌 (sidebar).

### Lab 3 Phases (archived)

- **2026-04-20:** Planning (Zoe proposal + locked spine), MCP design (Book), authoring (Kaylee)
- **2026-04-20 evening:** Patches (Jayne QA), README move to `agents/`, agent examples, MCP server creation, plugin capstone
- **2026-04-21 morning:** Module-shadow fix (mcp/ → mcp_servers/), Exercise E plugin capstone completed

Full Lab 3 decision timeline lives in `.squad/decisions.md` under "## Lab 3 Planning (2026-04-20)".

---

## Learnings (Current Activity)

## 2026-04-21 — Lab 4 README authored & shipped to review

Wrote `copilot-cli/README.md` (~977 lines, 31KB) per verified AGENDA.md v3. Structure: Theory (6 sections, 15 min) → Core Exercises A–E (50 min) → Customization (30 min) → Programmatic & Automation (Ex F–G, 20 min). All 14 correctness rules from Book's verification applied. Pre-lab checklist + learning objectives included. Lab 4 now in review phase with Zoe.

**Charter addendum:** Lab 4 charter conventions + no-overexplain directive applied automatically in spawn prompt. Quality over wordcount maintained.

**Status:** Awaiting Zoe review + Geronimo final approval.

## 2026-04-27 — Lab 4 Q&A section pattern established (cross-agent note)

Book added Lab 4's first Q&A entry (Plan mode vs `/plan` command) and established reusable template for future questions. Format: short answer → detailed terms (bullets) → "📌 When to use which" guidance → source links. Pattern documented in `.squad/decisions.md` § Lab 4 Q&A Section Pattern. Your README (lines 879–904) carries the first exemplar; future questions will follow this structure.

## 2026-04-27 — Simon's Lab 4 friction log shipped; actionable feedback for Lab 4 revisions

Simon (new Learner agent) completed first-time-reader dry-run of Lab 4. Friction log available at `.squad/files/simon-lab4-friction-log.md`. Key findings: 1 blocker (Exercise A Step 4 references Lab 3 features without prerequisite), 5 confusing moments (plan mode placement in theory, interaction prompt clarity), 2 nits. **Action for you:** Exercise A Step 4 fix is critical (Lab 3 context assumption breaks first-timers). Consider Simon's suggested fixes for interaction clarity (`go` vs `/go`, `/agent` vs `/agents` consistency, expected output for Exercise E). Simon's tone is respectful, specific, and includes "what worked well" notes for framing feedback positively.

## 2026-04-27 — Lab 4 expected output fixed (Exercise A, Step 4)

**Issue:** README line 198 described expected CLI output for `@backend/app.py` query with features from Lab 3 (university app with `/api/v1/register`, duplicate-email validation, capacity checks). But `copilot-cli/app/backend/app.py` is a fresh starter — Mergington High School activity signup app with only `GET /activities` and `POST /activities/{activity_name}/signup` endpoints.

**Fix applied:** Rewrote line 198 expected output to match actual local code: "A summary of the FastAPI app — it manages activity signups for Mergington High School, with endpoints like `GET /activities` and `POST /activities/{activity_name}/signup`…"

**Principle:** Lab 4 inherits Lab 3 *knowledge* (conceptual understanding of agents, Copilot capabilities), but NOT code. The `copilot-cli/` app is code-self-contained. Expected outputs in READMEs must describe the actual local codebase, never features from prior labs' evolved code. This prevents first-timers from verifying impossible outputs.

**Also updated:** Line 176 clarified "from this lab's workspace" instead of "from Labs 1–3" to reinforce this is an independent app copy.

## 2026-04-27 — Lab 4 friction round 1: 7 surgical fixes to README

Applied all 7 non-blocker fixes flagged by Simon's friction log:

1. **Fix 1 — Pre-Lab path clarity (line 173):** Changed `cd copilot-cli/app/` to `cd github-copilot-101/copilot-cli/app/` with added note that full path works regardless of repo entry point.
2. **Fix 2 — Plan mode theory (line ~123):** Added inline note distinguishing `/plan` slash command (one-off) from **plan mode** (persistent session state, toggled with `--plan` flag), pointing to Q&A for full explanation.
3. **Fix 3 — Auth flow clarity (line 184-186):** Rewrote device-flow vs `/login` bullets to make clear they're the same thing (CLI version difference), introducing the "either way, authenticate with GitHub" model.
4. **Fix 4 — Exercise B `@.` positioning (line ~220-231):** Moved `@.` explanation note to **before** the prompts using it, and added expected-output hint after prompts (learner should see CLI summarize backend files).
5. **Fix 5 — Exercise C `go` vs `/go` clarity (line 304):** Clarified that `go` is literal text input at plan prompt, not a slash command, with phrasing "(no slash — it's a literal response at the plan prompt)".
6. **Fix 6 — Exercise D Step 2 expected output (line ~378):** Added explicit `✅ You should now see` block describing the deny prompt when permission constraint kicks in.
7. **Fix 7 — `/agent` vs `/agents` consistency (line 582):** Changed `/agent` to `/agents` (plural) to match the actual CLI command.

**Pattern observed:** Most friction stemmed from ambiguous **interaction points** — unclear whether input is a slash command, literal text, or browser action. Precision in formatting (backticks for literals, clear phrasing on "type X") eliminates guesswork for first-timers. All fixes preserved tone, emoji style, and existing structure.

## 2026-05-04 — River retired; merged into Book

River (Copilot Expert — Patterns & Prompting) retired. Role and knowledge consolidated into Book, who is now unified Copilot Expert covering platform, surfaces, AND patterns/prompting. For prompting questions, pattern guidance, or agent-mode review, route to Book.

## Lab Knowledge Base (canonical as of 2026-05-04)

Supersedes earlier ad-hoc Lab 3 notes from 2026-04-20. From this point on, treat the entries below as the source of truth for lab scope, structure, and continuity. Re-read the relevant subsection before authoring/editing a lab; only crack the README open for verbatim text.

### Lab 1 — Copilot Chat (`copilot-chat/`)
- **Teaches:** How to use Copilot Chat's three modes (Ask, Agent, Plan) inside VS Code to onboard, fix bugs, and add features.
- **Audience / prerequisites:** Total Copilot beginner; needs VS Code + GitHub Copilot + Python extensions installed and a working `git`. No prior labs assumed.
- **Time budget:** ~90 min, 6 "Steps" (not Exercises). Step 1 onboard → Step 2 inline + bug fix → Step 3 Agent Mode → Step 4 Plan Agent → Step 5 solo capstone (3 mini-tasks) → Step 6 commit.
- **Stack / sample app:** FastAPI (`backend/app.py`) + vanilla JS/HTML (`frontend/`). Mergington High School activities signup. In-memory `activities` dict with `Chess Club`, `Programming Class`, `Gym Class`. Endpoints: `GET /activities`, `POST /activities/{name}/signup`. Run with `uvicorn backend.app:app --reload` from `copilot-chat/` after `pip install -r requirements.txt`.
- **Lab structure:** Step 1 = open chat, ask for project intro, terminal inline-chat for git branch. Step 2 = fix duplicate-signup bug + generate sample data + describe work. Step 3 = Agent Mode adds participant list + unregister buttons. Step 4 = Plan Agent designs tests for backend. Step 5 = three "fly solo" tasks (extract data to JSON, withdraw feature, Swagger docs). Step 6 = commit.
- **Key files / paths:** `backend/app.py` (the only backend file students edit), `frontend/{app.js,index.html,styles.css}`, `requirements.txt`. There is a `venv/` checked-in artifact that should ideally be gitignored.
- **Copilot features showcased:** Ask Mode, Inline Suggestions, Inline Chat, Terminal Inline Chat (Ctrl/Cmd+I), Agent Mode, Plan Agent. No custom agents, no MCP, no plugins, no CLI.
- **Continuity notes:** Lab 1 introduces the Mergington app; Lab 3 and Lab 4 both fork the same starter into their own folders. Lab 1 → Lab 2 jump is a *different* sample app (SunVoyage), so no code continuity into Lab 2. Lab 1 must NOT assume any prior Copilot knowledge.
- **Style traps to avoid:** Has a "Congratulations!" wrap-up (lines 713–722) that violates current "no wrap-up" rule — and it incorrectly says "Lab 02". Theory is interleaved per-step with `### 📖 Theory:` headings rather than a single Part 1 (legacy pattern). Step numbering restarts at `1.` mid-list. Uses GitHub-only emoji shortcodes (`:bug:`, `:rocket:`).
- **Editing hotspots:** Wrap-up section (delete on next pass); Step 6 title typo ("Finally commit time"); the table at lines 29–35 lists "Plan Agent" as a mode — verify against current docs since Plan moved between mode picker and slash command. Screenshots: none today, but several activities reference the chat side panel and mode picker — UI changes will rot fast.

### Lab 2 — Customizing Copilot (`customize-copilot/`)
- **Teaches:** How to shape Copilot output without re-prompting, via custom instructions (3 scopes), path-specific instructions, prompt files, AGENTS.md, and skills.
- **Audience / prerequisites:** Comfortable with Copilot Chat (Lab 1 level). Needs VS Code + Copilot + Python and a workspace where `.github/` lives at the repo root.
- **Time budget:** ~120 min, 5 Steps. Heavier than 90 min by design.
- **Stack / sample app:** SunVoyage Tours — FastAPI (`main.py`) + Jinja2 templates + static JS/CSS. Activities, flights, accommodations driven by `config.json`. Per-activity markdown lives under `activities/{jet-skiing,kayaking,sightseeing,restaurant-guide}/`. Run `pip install -r requirements.txt` then `uvicorn main:app --reload` from `customize-copilot/`.
- **Lab structure:** Step 1 = repo-level `copilot-instructions.md` (org-level read-through, personal read-through). Step 2 = path-specific `*.instructions.md` for `activities/`, fix kayaking + sightseeing. Step 3 = `AGENTS.md` for agent onboarding. Step 4 = `*.prompt.md` reusable slash commands (new-activity, plus a flights/accommodations DIY). Step 5 = `SKILL.md` web-enhancer skill + a skill that references prompt files.
- **Key files / paths:** `.github/copilot-instructions.md`, `.github/instructions/activities.instructions.md`, `.github/prompts/new-activity.prompt.md`, `.github/skills/web-enhancer/SKILL.md`, `AGENTS.md`, `config.json`, `activities/<id>/`. Strict rule reminded at lines 26–44: `.github/` must be at workspace root.
- **Copilot features showcased:** Repository / personal / organization custom instructions, path-specific instructions, AGENTS.md, prompt files, skills. No agent mode focus, no MCP, no CLI.
- **Continuity notes:** Lab 2 introduces every "customization primitive" (instructions, prompt files, AGENTS.md, skills). Labs 3 and 4 explicitly *don't re-teach* these — they cite "covered in Lab 2." Lab 4's "What we skipped" table points back here.
- **Style traps to avoid:** Big "Congratulations!" + "Key Takeaways" + "What's Next?" block (lines 1164–1192) violates the no-wrap-up rule. Also has a dual-language sibling (`README-es.md`, `README-lab2.md`) that drifts easily.
- **Editing hotspots:** Lines 26–44 .github layout diagram (changes if VS Code moves any path); Step 1 priority-recap table (must stay aligned with whatever GitHub docs currently say about precedence); skills section since SKILL.md schema is still evolving.

### Lab 3 — Custom Agents (`agents/`)
- **Teaches:** Drive Agent Mode through the full plan→edit→run→observe loop, pick the right permission level, build workspace-scoped custom agents, consume + author MCP servers, and package the lot as a plugin.
- **Audience / prerequisites:** Comfortable with Agent Mode (Lab 1) and customization primitives (Lab 2). Needs Python 3 venv + Copilot Agent enabled + `chat.mcp.discovery.enabled`. Node optional for the consume-an-MCP exercise.
- **Time budget:** ~100–110 min, 5 Exercises (A–E) with sub-parts. Theory front-loaded in Part 1.
- **Stack / sample app:** Forked Mergington app — `backend/app.py` (FastAPI, same in-memory `activities` dict as Lab 1), `frontend/`, plus `mcp_servers/activities_server.py` (FastMCP), `tests/` (scaffold only — `__init__.py` present but no real tests committed yet), `sample-data/school-policies.txt`.
- **Lab structure:** Part 1 theory (agent loop, permission levels, custom agents, MCP). Part 2 hands-on: A = run agent loop end-to-end. B = read-through of Default / Bypass / Autopilot permissions. C = three custom agents (`planner` with handoff, read-only `reviewer`, scope-locked `test-author`). D = consume filesystem MCP (optional), build `activities_server.py` (required), Microsoft Learn MCP + Playwright MCP (both optional). E = package agents + MCP into `my-mergington-plugin/` with `plugin.json`, `agents/`, `.mcp.json`.
- **Key files / paths:** `.github/agents/*.agent.md` (3 of them), `.vscode/mcp.json`, `.vscode/settings.json`, `agents/mcp_servers/activities_server.py`, `agents/requirements.txt` (adds `mcp[cli]>=1.0`, `pytest`), `my-mergington-plugin/plugin.json`.
- **Copilot features showcased:** Agent Mode loop, permission levels, custom agents (handoff / least-privilege / scope-locking patterns), MCP consume + author with `FastMCP`, Copilot plugins (preview, gated by `chat.plugins.enabled` + `chat.pluginLocations`).
- **Continuity notes:** Lab 3 reuses Lab 1's Mergington app (same data shape — must coexist with `Chess Club` / `Programming Class` / `Gym Class`). Lab 4 reuses Lab 3's app skeleton at `copilot-cli/app/` (independent copy — Lab 4 README must describe its own local code, never Lab 3's evolved features).
- **Style traps to avoid:** None major today — Lab 3 already follows current conventions (theory-first, no wrap-up, manual file creation, install + run commands, agent frontmatter strict). Watch the Windows callouts in Pre-Lab + the `.vscode/mcp.json` venv path so they stay platform-split.
- **Editing hotspots:** E.1–E.3 plugin section (preview feature, marketplace and settings names churn); the `mcp[cli]` version pin in `requirements.txt`; D.3/D.4 optional MCPs (registry URLs change). Tests folder is empty today — if a future lab actually generates tests, this is where they'd land.

### Lab 4 — Copilot CLI (`copilot-cli/`)
- **Teaches:** Use Copilot CLI interactively and headlessly from any terminal, with permission patterns, custom agents/skills/plugins, MCP, hooks, and `/chronicle` memory.
- **Audience / prerequisites:** Knows VS Code Copilot well (Labs 1–3 worth of vocabulary). Needs a terminal + Homebrew or npm or winget + a GitHub account that can device-flow auth.
- **Time budget:** ~100 min, 6 Exercises (A–F) split across Core (A–E), Customization (read-throughs + drills), Programmatic (F).
- **Stack / sample app:** Self-contained copy of the Mergington app under `copilot-cli/app/{backend,frontend,mcp_servers,tests,sample-data,requirements.txt}`. Identical starter to Lab 3 — `GET /activities`, `POST /activities/{activity_name}/signup`. Lab 4 work happens in the terminal, against this app as a context target.
- **Lab structure:** Part 1 theory (what CLI is, CLI vs VS Code, interactive vs programmatic, slash commands). Part 2 core: A install+auth+hello, B context (`@`, `/context`, `/compact`, `/clear`), C slash commands deep dive, D permission flags + patterns (`shell(git push)`, `MyMCP(tool)`, `url(domain)`), E multi-turn autonomous task. Part 3 customization: CLI custom-instruction paths, custom agents (`.agent.md`), hooks (read-through), skills via `@skill:name`, `/chronicle` memory, plugins, MCP CLI config paths (read-through). Part 4: Exercise F headless `copilot -p` for CI-style automation. Followed by a Q&A section (template established 2026-04-27) and a "What's Next?" section.
- **Key files / paths:** `copilot-cli/app/backend/app.py` (the local code targeted by `@backend/app.py`), CLI config paths under `~/.copilot/` (instructions, agents, MCP), `copilot-cli/app/requirements.txt`. No `.github/` content authored in this lab — Labs 2/3 own those.
- **Copilot features showcased:** CLI interactive + plan + autopilot modes, slash commands, `@`-mention context, permission patterns, CLI-flavored custom agents/skills/plugins/hooks, `/chronicle`, headless `copilot -p`. Explicitly *defers* AGENTS.md / prompt files / VS Code agents+plugins / MCP authoring to Labs 2 and 3.
- **Continuity notes:** Lab 4 inherits Lab 3 *concepts* (agents, MCP, plugins, skills) but NOT code. The `copilot-cli/app/` copy is the canonical source for any expected-output text — never describe Lab 3's evolved app here. Q&A section uses the pattern Book established (short answer → detailed terms → 📌 when to use which → source links).
- **Style traps to avoid:** "What's Next?" + "Lab complete. 🎉" block (lines 913–954) violates current no-wrap-up rule. Pre-Lab is much thinner than Lab 3's (no clone step, no `cd`, no app boot check) — feels uneven across the suite.
- **Editing hotspots:** CLI install commands per platform (Homebrew/npm/winget formulas drift), slash command list (new commands land often), `chat.plugins.enabled` + `/chronicle` (preview features), `copilot -p` flag surface. Simon's friction-log fixes from 2026-04-27 already shipped — keep an eye on the same "interaction-point ambiguity" pattern when adding new exercises.

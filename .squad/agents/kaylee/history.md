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

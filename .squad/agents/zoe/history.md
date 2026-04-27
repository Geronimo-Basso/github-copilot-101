# Project Context

- **Owner:** Geronimo Basso
- **Project:** github-copilot-101 — a repository of hands-on labs (90 min each, theory + practice) teaching GitHub Copilot. Existing lab examples live in `customize-copilot/` and `copilot-chat/`.
- **Stack:** Markdown labs, sample code in various languages, repo-as-curriculum
- **Created:** 2026-04-20T09:46:24Z

## Learnings

<!-- Append new learnings below. Each entry is something lasting about the project. -->


## 2026-04-20 — Lab 3 plan drafted

- Reframed user's "custom agents" idea as a 3-layer arc: custom chat modes → MCP → cloud Coding Agent. Single feature wasn't enough to fill 90 min or justify a third lab.
- Hard rule applied: theory blocks ≤ 12 min each, totalling 19 min; hands-on 58 min; intro+wrap 13 min.
- Non-overlap audit done against Lab 1 (basic Agent Mode, Plan Agent) and Lab 2 (AGENTS.md, prompt files, skills). Custom chat modes ≠ AGENTS.md; MCP tools ≠ skills. Worth documenting this distinction in the lab itself.
- Reusing `agents/` app as-is. Lab 1 already implements "unregister" — flagged to Book to pick a different first feature for Step 2.
- Cloud Coding Agent included despite async risk because it's the payoff that makes the lab feel grown-up; flagged pacing risk to River (Q7, Q8).
- Plan written to `.squad/decisions/inbox/zoe-lab3-plan.md` for Book & River review before Kaylee writes content.

## 2026-04-20 — Lab 3 plan LOCKED (Spine B)

- User chose Spine B (Book's recommendation). Cloud Coding Agent deferred to a future Lab 4. My original draft's 3-layer arc (chatmodes → MCP → cloud) is superseded.
- Locked 4-block structure: Agent loop in practice (22 min) → Permission levels (10 min) → MCP install + drive (20 min) → Custom agent + Plan→Implementation handoff (15 min). Theory 15, hands-on 67, intro+wrap 18. Within charter.
- River's Exercise 2 (plan-first unregister): CUT. Capability overlapped Block 1 and the time wasn't there. Preserved the plan-first pattern as a mid-exercise callout in Exercise A and as a structural feature of Exercise D (Plan agent → handoff to Agent).
- Locked MCP choice: GitHub MCP server. Playwright rejected — can't guarantee browser binary in lab env. GitHub MCP also gives the textbook "open issue, implement it" wow moment.
- Applied Book's corrections globally: `.github/agents/*.agent.md`, `infer:` removed (use `user-invocable` + `disable-model-invocation`), Plan is a separate built-in agent (not a renamed Edit — corrected in intro slide).
- Resolved 5 of River's 6 open questions; Q2 (terminal access in lab env) deferred to Kaylee as pre-lab checklist.
- Locked plan written to `.squad/decisions/inbox/zoe-lab3-locked-plan.md` with explicit handoff brief to Kaylee.

## 2026-04-20 — Lab 3 plan AMENDED (MCP block: consume + create)

- Per Geronimo's directive (`copilot-directive-mcp-block.md`), amended the locked plan in place: replaced Block 3 / Exercise C wholesale with Book's consume+create design (filesystem MCP optional, `agents/mcp/activities_server.py` required). Budget rebalanced: Block 3 hands-on 20→25, Exercise A 22→20, Exercise B 10→8; totals now theory 15 / hands-on 68 / intro+wrap 17 — within charter.
- Dropped GitHub MCP entirely (and the pre-lab GitHub-issue creation step) since the new server set is `mergington-activities` + filesystem MCP. Updated §4 cuts (now: no resources, no MCP client), §5 row 3, §6 corrections, §7 pre-lab (added `mcp[cli]` install + `node --version` + sample-data seed), and §8 handoff (called out consume=optional / create=required as Block 3's fixed contract for Kaylee).
- Spine, Exercises A/B/D, file path conventions, and Book's other corrections all left untouched.

## Lead/scope notes from Lab 3 cycle (2026-04-21)

Geronimo (project owner) directives observed across the Lab 3 build cycle. Use as canon for Lab 4 planning and beyond.

### Scope discipline
- Always check what prior labs covered before scoping a new one. Lab 3 explicitly skipped custom instructions, prompt files, and skills (taught in Lab 2). Cite "previously taught in Lab N" instead of re-explaining.
- Stack is fixed: agents/ FastAPI + vanilla JS app. Don't introduce new stacks per lab — students learn Copilot patterns, not new frameworks.

### Process: plan before building
- Geronimo wants a planning conversation BEFORE Kaylee starts writing.
- Coordinator pattern: propose structure, get explicit approval, then spawn the builder.
- This was demonstrated for Exercise E and confirmed by Geronimo.

## 2026-04-27 — Lab 4 Q&A pattern review approved (cross-agent note)

Book established Lab 4's Q&A section format: short answer → detailed comparison terms → "📌 When to use which" closer → cited sources. First entry distinguishes Plan mode from `/plan` command. Pattern documented, approved, ready for future questions. See `.squad/decisions.md` § Lab 4 Q&A Section Pattern.

### Time budget
- Old default: 90 minutes per lab. **Now flexible** — quality over strict cap. Build the lab the right size.
- Still post per-exercise time estimates so students know what they're committing to.

### Voice preferences for the coordinator (Direct Mode answers)
- Direct, concise. Geronimo dislikes filler.
- Compact tables / bullet summaries for multi-agent work.
- Use ask_user with multi-choice menus for scope decisions — Geronimo appreciates them.
- Respond in English (per global CLI rules) even if Geronimo writes in Spanish.

### Repo facts
- `.squad/` is gitignored — never commit it.
- `.vscode/` IS tracked — users get working configs out of the box.
- Module-shadow gotcha when scaffolding Python lab samples (skill captured).

## 2026-04-20 — Lab 4 planning kickoff

- Analyzed external reference repo `github/copilot-cli-for-beginners` (8 chapters: install → modes → workflows → agents/skills/MCP).
- Key insight: Chapters 00-03 are CLI-foundational (install, ask/task/develop modes, context with `@`, workflows). Chapters 04-07 parallel our Labs 2-3 extensibility (agents, skills, MCP) but with CLI-specific config paths.
- Gold to borrow: install/auth flow, three-mode framing, `@` context syntax, code review + test generation workflows, CLI-specific custom agents (`~/.copilot/agents/` vs VS Code's `.github/agents/`).
- Skip: AGENTS.md, skills, MCP theory (all taught in Labs 2-3).
- Differentiation locked: Lab 4 = terminal-native Copilot with CLI config (`.copilot/config.yaml`), user-level agents, scripting/headless automation. No overlap with VS Code UI workflows.
- Proposal written to `.squad/decisions/inbox/zoe-lab4-agenda-proposal.md` with 5 exercises (A-E: install/auth, ask mode + context, task mode, develop mode, CLI custom agents), optional 6th (scripting). Theory 15 min, hands-on 60-75 min.
- Five open questions for Geronimo (install scope, sample app choice, agent path scope, scripting required vs optional, MCP inclusion).
- Flagged risks: install friction (multi-platform), auth (device flow + org policies), develop mode drift, config file discoverability, overlap fatigue.
- Next steps proposed: spawn Book + River (verify CLI syntax/flows) → lock structure → spawn Kaylee to write.

## 2026-04-21 — Lab 4 v2 complete revision per Geronimo feedback

- v1 agenda was missing 7 major areas: slash commands deep dive, interactive vs programmatic framing, use cases, dedicated customization section, permission flags, context management, hooks, memory, and code-review agent example.
- **New style directive:** trim prose ruthlessly. Code + checkpoints > explanation. Applied globally.
- Restructured from 2-part (theory + exercises) to 4-part: (1) Theory & Foundations, (2) Core CLI Usage, (3) Customization, (4) Programmatic/Automation.
- Part 2 now includes:
  - Expanded context management (add/remove context, limits, reset/clear)
  - **NEW: Slash commands deep dive** — `/fleet`, `/plan`, `/skills`, `/delegate`, `/research`, `/chronicle` (super important per Geronimo), `/yolo`
  - **NEW: Permission flags** — `--allow-all-tools`, `--deny-tool`, `--allow-tool`
- Part 3 (Customization) is now a dedicated ~50 min section covering:
  - Custom instructions (CLI-side)
  - Custom agents (with code-review agent example per Geronimo request)
  - **NEW: Hooks** (mechanism pending Book verification)
  - Skills (CLI invocation — cite Lab 2 for authoring)
  - **NEW: Copilot memory** (relationship to `/chronicle`)
  - Plugins (cite Lab 3, CLI equivalents if any)
  - MCP read-through (config path differences only)
- Part 1 now includes:
  - **NEW: Use cases section** (when to use CLI vs VS Code — SSH, CI/CD, headless review, etc.)
  - **NEW: Interactive vs programmatic** as explicit teaching point
- Total time increased to ~2.5 hours (within flexible-time-budget convention).
- Added 28 verification tags for Book covering: mode names, slash command syntax/behavior, permission flags, hooks mechanism, memory storage, context management commands, MCP paths, headless auth, and more.
- Section 7 (Open Questions Decided) preserved intact per instructions, renumbered to Section 10.
- v2 emphasizes differentiation: CLI = terminal-native + scripting (what VS Code can't do).

## 2026-04-21 — Lab 4 README review phase

Kaylee shipped `copilot-cli/README.md` from verified AGENDA.md v3. Now in Zoe review phase to check correctness, pacing, clarity, and no-overlap with Labs 1–3. Checklist: 28 CLI facts (Book verification), theory ≤25 min, hands-on ≤55 min, exercises A–G run in target env, code examples valid, links accurate, template compliance (badge, objectives, "What's Next"). Output: `.squad/decisions/inbox/zoe-lab4-review.md` (pending).

**Status:** In progress.

## 2026-04-21 — Lab 4 README final review (Kaylee's draft)

- Reviewed Kaylee's `copilot-cli/README.md` (~977 lines) against AGENDA v3, Book's verification report, Lab 3 exemplar, and no-overexplain directive.
- **VERDICT: ✅ Ship-ready with minor polish.** No correctness errors, all 7 exercises complete, all locked decisions honored.
- Spot-checked 15 critical CLI facts vs Book's report — all correct: modes (`interactive`/`plan`/`autopilot`), one-shot syntax (`copilot -p`), JSON flag (`--output-format json`), install commands, `.agent.md` extension, `.github/` repo paths, `/chronicle` experimental gate, hooks read-through, permission patterns.
- **3 minor overexplain instances flagged** (lines 88-93, 225-226, 258-287): bulleted feature list duplicates what code blocks teach, Exercise B intro explains `@` before showing it, slash command explanations duplicate checkpoints. Recommended deleting ~10 lines of prose to tighten "code + checkpoints > explanation" style.
- **No continuity issues:** Uses `agents/` app throughout, cites Labs 2-3 correctly for custom instructions/skills/MCP, "What We Skip" table accurate.
- **Voice/tone matches Lab 3:** Friendly, concrete, hands-on. Checkpoints specific and testable.
- **Kaylee's execution: A-** — high-quality lab, minor polish would make it tighter. Recommended fixes written to `.squad/decisions/inbox/zoe-lab4-review.md` with line numbers for Geronimo or Kaylee to apply (5 min edit).

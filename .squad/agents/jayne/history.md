# Project Context

- **Owner:** Geronimo Basso
- **Project:** github-copilot-101 — a repository of hands-on labs (90 min each, theory + practice) teaching GitHub Copilot. Existing lab examples live in `customize-copilot/` and `copilot-chat/`.
- **Stack:** Markdown labs, sample code in various languages, repo-as-curriculum
- **Created:** 2026-04-20T09:46:24Z

## Learnings

<!-- Append new learnings below. Each entry is something lasting about the project. -->

### 2026-04-20T10:02:26Z — Lab 3 planning staged; review coming

Zoe, Book, and River planned Lab 3 ("GitHub Copilot Agent Mode").
Full plans live in `.squad/decisions.md` under **"## Lab 3 Planning
(2026-04-20)"**. Kaylee will draft the lab next; you will be called
afterwards to review for tone, pacing, and parity with Lab 1/2
structure. Read the three flagged contradictions at the top of that
section before reviewing — they shape what "correct" looks like.

### 2026-04-20 — Lab 3 QA walkthrough → APPROVE WITH MINOR FIXES

Walked Lab 3 (`agent-mode/README.md`, 556 lines) end-to-end against
Zoe's locked plan, Book's MCP proposal, and Kaylee's handoff.
Lessons worth carrying forward for any lab in this format:

- **Cross-platform pass is non-optional.** Two of the seven items
  Kaylee flagged were Windows path issues, and one was an outright
  blocker (`.vscode/mcp.json` hard-coding `.venv/bin/python`).
  Whenever a lab ships a `.vscode/mcp.json`, `python3` command, or
  `rm -rf`, write the Windows variant in the same edit. There is no
  per-OS variable substitution in `mcp.json`, so a callout is the
  only fix.
- **`python -m <pkg>.<sub>` invocations only work when launched
  from the project root and when implicit namespace packages
  resolve.** Worth shipping `__init__.py` at every package level
  even when PEP 420 covers you, because future tooling may not.
- **Model pins (`model: gpt-5`) are seat-availability landmines.**
  Always escalate to whoever owns the lab environment before
  shipping a hard model pin — never assume the latest model is
  enabled on the default learner seat.
- **Time arithmetic drifts.** Per-step "~N min" badges plus an
  unbudgeted wrap routinely add up to 10+ min over the advertised
  total. Sum them yourself; don't trust the header.
- **Reviewer Rejection Lockout heuristic.** A genuine one-line
  callout fix counts as APPROVE WITH MINOR FIXES (no lockout). If
  a reviewer needs to think about *what* the fix should be, that's
  a REJECT and someone other than the original author writes the
  patch.

### 2026-04-21 — Lab 3 Exercise D module shadow fix deployed

Post-QA fix from Kaylee: renamed `agents/mcp/` → `agents/mcp_servers/` to eliminate Python module shadowing bug where `import mcp` from inside `agents/` resolved to the local dir instead of the installed PyPI package. All references updated in `.vscode/mcp.json` and `agents/README.md`. **No action required from QA** — this affects the same Exercise D you reviewed; the fix is orthogonal to your callouts (all your patches remain intact). Verified working.

### 2026-04-21 — Lab 3 Exercise E (Plugin Capstone) shipped

Kaylee added Exercise E as the optional capstone for Lab 3: **Package agents and MCP servers as a VS Code plugin**. Three sub-exercises teach students plugin structure (E.1 theory), scaffold `my-mergington-plugin/` (E.2 hands-on), and understand VS Code discovery/distribution (E.3 theory). Reuses Exercise C + D artifacts. Committed in `1cfde5a`. Exercise E is optional depth (~20 min). Note: E.3 does not require students to actually enable `chat.plugins.enabled` (often org-locked); it explains what would happen if they did. When planning Lab 3 walkthrough/verification, can confirm plugin facts align with current VS Code docs and test the plugin manifest as a bonus if time permits.

### 2026-04-27 — Simon (Learner) joins squad; Lab 4 friction identified

Simon cast as first-time-learner persona. Dry-ran Lab 4 with prerequisites only (no CLI installed). Produced friction log identifying 8 stuck-points: 1 blocker (Exercise A Step 4 assumes Lab 3 knowledge), 5 confusing items (plan mode vs `/plan`, interaction ambiguity), 2 nits (path context, command inconsistency). Key insight: **confusion vs. breakage distinction.** Simon's findings are available at `.squad/files/simon-lab4-friction-log.md`. Lab 4 is logically sound but needs clarity at interaction boundaries before approval. Orchestration log: `.squad/orchestration-log/2026-04-27T12-38-19Z-simon-lab4-dryrun.md`.


### 2026-04-27 — Lab 4 Round 1 polish complete; ready for QA

Simon's Lab 4 dry-run friction log (8 items) fully addressed by Kaylee via blocker fix + round-1 polish. All expected-output and clarity ambiguities resolved. Lab 4 README now ready for QA pass when your schedule allows.

## 2026-05-04 — River retired; merged into Book

River (Copilot Expert — Patterns & Prompting) retired. Role and knowledge consolidated into Book, who is now unified Copilot Expert covering platform, surfaces, AND patterns/prompting. For QA feedback on prompting patterns, agent-mode guidance, or Copilot surface verification, route to Book.

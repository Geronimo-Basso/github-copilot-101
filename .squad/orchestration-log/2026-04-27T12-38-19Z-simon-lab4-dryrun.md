# Orchestration: Simon Lab 4 Dry-Run

**Timestamp:** 2026-04-27T12:38:19Z  
**Agent:** Simon (Learner)  
**Task:** Lab 4 dry-run (first-time learner, no CLI installed, prereqs only)  
**Deliverable:** `.squad/files/simon-lab4-friction-log.md` (12.6 KB)  
**Requested by:** Geronimo Basso  

---

## Friction Summary

**Total stuck-points:** 8  
- **Blockers** (would have given up): 1
  - Exercise A Step 4 assumes Lab 3 knowledge (features not introduced in this lab)
- **Confusing** (had to guess): 5
  - Plan mode vs `/plan` command (explained in Q&A, not in theory section)
  - Exercise A Step 3: `/login` vs device-flow instructions unclear
  - Exercise B Step 2: no expected output; unclear what to validate
  - Exercise C Step 1: unclear if `go` is literal text or `/go` command
  - Exercise E: missing app context (capacity, feature scope, frontend tech)
- **Nits** (mild friction): 2
  - Pre-Lab Setup: unclear if already inside repo folder before Exercise A Step 2
  - Part 3 (line 530 vs 582): `/agents` vs `/agent` command inconsistency

---

## Strengths Noted

- Part 1 theory is clear (three-mode breakdown, CLI vs VS Code distinction)
- Exercise B context management is logical and incremental
- Permission patterns syntax table is unambiguous
- Part 3 file path tables are concrete and beginner-friendly
- Q&A section is honest about limitations
- "What's Next" callouts are actionable

---

## Recommendation

Lab is *logically sound* but requires **Lab 3 completion** as a prerequisite and needs **interaction clarity** at critical moments (e.g., step prompt format). Simon estimates: 90 min if Lab 3 prereq met, ~120 min if backtracking needed.

**Critical fix required:** Exercise A Step 4 must list Lab 3 Exercise A as a prerequisite or rewrite expected output to be app-agnostic.

---

## Files Modified / Created

- `.squad/files/simon-lab4-friction-log.md` — full friction log with 8 stick-points and detailed suggested fixes

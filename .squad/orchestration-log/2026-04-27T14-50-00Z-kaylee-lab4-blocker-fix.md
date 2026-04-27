# Orchestration: Kaylee Lab 4 Blocker Fix

**Timestamp:** 2026-04-27T14:50:00Z  
**Agent:** Kaylee (Lab Builder)  
**Task:** Fix Simon's blocker — Exercise A Step 4 expected output  
**Deliverable:** `copilot-cli/README.md` line 198 rewritten; decision doc added to inbox  
**Requested by:** Geronimo Basso  

---

## Issue

Simon (Learner) found that Lab 4 Exercise A Step 4 expected output described features from Lab 3 evolved code:
- `/api/v1/register` endpoint
- Duplicate email validation
- Capacity checks

These features are **not** in the Lab 4 `copilot-cli/app/` starter code (Mergington High School activities app with only `/activities` and `/activities/{activity_name}/signup`).

---

## Fix Applied

Line 198 expected output rewritten to describe actual Lab 4 app:
- Removed Lab 3 feature references
- Updated to match actual endpoints: `GET /activities`, `POST /activities/{activity_name}/signup`
- Reframed as self-contained app, not evolved from Lab 3 code

---

## Context Decision

Added decision doc `kaylee-lab4-knowledge-not-code.md` to decisions inbox establishing principle: **Lab 4 builds on Lab 3 *knowledge* (conceptual), not evolved Lab 3 *code*.** Expected outputs describe only the local `copilot-cli/app/` starter.

---

## Files Modified / Decision Added

- `copilot-cli/README.md` — line 198 expected output rewritten
- `.squad/decisions/inbox/kaylee-lab4-knowledge-not-code.md` — principle and examples

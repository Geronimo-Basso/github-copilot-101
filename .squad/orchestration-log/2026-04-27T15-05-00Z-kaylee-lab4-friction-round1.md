# Orchestration: Kaylee Lab 4 Friction Round 1

**Timestamp:** 2026-04-27T15:05:00Z  
**Agent:** Kaylee (Lab Builder)  
**Task:** Fix remaining 7 friction items from Simon's lab 4 dry-run  
**Deliverable:** `copilot-cli/README.md` 7 surgical fixes; decision doc added to inbox  
**Requested by:** Geronimo Basso  

---

## Issues Fixed

Simon's non-blocker friction items (5 confusing, 2 nits) addressed with targeted rewording:

1. **Pre-Lab path clarity** — full path added to repo navigation step
2. **Plan mode vs `/plan` distinction** — theory section clarified (line 176)
3. **Device-flow / `/login` parity** — Exercise A Step 3 aligned
4. **`@.` ordering** — repositioned before prompts in Exercise B Step 2
5. **`go` vs `/go` distinction** — literal vs command clarified in Exercise C Step 1
6. **Exercise D Step 2 expected output** — prompt visibility rule documented
7. **`/agents` plural consistency** — unified across file (line 582 fixed)

---

## Context Decision

Added decision doc `kaylee-lab4-friction-round1-fixes.md` to inbox documenting principle: **clarity over assumption at interaction boundaries.** First-timers must never guess whether input is a CLI command, literal text, or browser action.

---

## Strengths Preserved

- Tone, emoji style, and lab structure unchanged
- No scope rewrite — only interaction clarity
- All fixes verified against Simon's detailed suggestions
- Lab 3 knowledge framing consistent with blocker fix decision

---

## Files Modified / Decision Added

- `copilot-cli/README.md` — 7 targeted fixes (lines 176, 198 and others)
- `.squad/decisions/inbox/kaylee-lab4-friction-round1-fixes.md` — summary and principle

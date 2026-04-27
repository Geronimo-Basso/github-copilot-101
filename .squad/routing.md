# Work Routing

How to decide who handles what.

## Routing Table

| Work Type | Route To | Examples |
|-----------|----------|----------|
| Lab scope, structure, learning objectives | Zoe | "What should the next lab cover?", curriculum arc, prerequisites |
| Copilot platform/surface facts | Book | "Does Copilot Chat support X in JetBrains?", MCP, agent mode, custom instructions |
| Prompting patterns, workflows, exercises | River | "Best prompting pattern for refactoring?", hands-on exercise design |
| Lab writing & sample code | Kaylee | Author the README, write sample code, scaffold the lab folder |
| Lab QA / walkthrough testing | Jayne | Run the lab end-to-end, verify timing, reject broken steps |
| Learner walkthrough / confusion report | Simon | Read the lab as a first-timer, surface ambiguity and stuck-points (no veto) |
| Final lab review & approval | Zoe | Sign-off before shipping |
| Session logging | Scribe | Automatic — never needs routing |
| Backlog / work-monitor | Ralph | Issue triage loop, queue keeper |

## Lab Production Pipeline

1. **Zoe** scopes the lab (objective, time budget, audience).
2. **Book** + **River** in parallel — Book validates Copilot feature accuracy; River designs the prompting/exercise patterns.
3. **Kaylee** writes the lab content using inputs from Book + River.
4. **Jayne** walks the lab end-to-end. May reject — revision goes to a different agent.
5. **Zoe** final review and ship.

## Issue Routing

| Label | Action | Who |
|-------|--------|-----|
| `squad` | Triage and assign `squad:{member}` | Zoe |
| `squad:zoe` | Scope/curriculum/review | Zoe |
| `squad:book` | Copilot platform accuracy | Book |
| `squad:river` | Prompting patterns / exercise design | River |
| `squad:kaylee` | Write/edit a lab | Kaylee |
| `squad:jayne` | QA a lab | Jayne |
| `squad:simon` | Learner walkthrough / confusion report | Simon |

## Rules

1. **Eager by default** — for any new lab, spawn Book + River + Kaylee in parallel after Zoe scopes.
2. **Scribe always runs** background after substantial work.
3. **Quick facts → coordinator answers directly.**
4. **"Team, build a lab on X" → fan-out:** Zoe (sync, scope) → Book/River/Kaylee parallel → Jayne → Zoe.
5. **Reviewer rejection lockout** — if Jayne or Zoe rejects, original author cannot revise.

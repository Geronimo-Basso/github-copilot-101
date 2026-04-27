# Simon's Lab 4 Friction Log

**Date:** 2024-01-10  
**Lab:** copilot-cli/README.md  
**Reader posture:** First-time learner, prerequisites only, CLI not installed.

---

## Summary

- **Total stuck-points:** 8
  - 🛑 Blockers (would have given up): 1
  - 😕 Confusing (had to guess): 5
  - 🤏 Nitpicks (mild friction): 2
- **Overall verdict:** The lab is *mostly* well-structured for a first-timer, but lacks clarity in three critical moments: the definition of "plan mode" and when to use it vs `/plan` (explained only in Q&A, not in the theory section where it belongs), Exercise E's autopilot task (which assumes I know what a "waitlist feature" looks like in this specific app), and the `/agent` vs `/agents` command mismatch (line 582 says `/agent`, but line 530 says `/agents`). I would finish the theoretical sections confidently but pause mid-Exercise E.

---

## Stuck-points

### Pre-Lab Setup — line ~54
**Severity:** 🤏  
**What tripped me up:** The prereq says "Open this repository in your terminal" and "All commands assume you're starting from the workspace root (`github-copilot-101/`)". But then Exercise A Step 2 (line 173) says "cd copilot-cli/app/" without reminding me where I am. If I follow the instruction literally and don't cd into the repo first, the next step fails.

**What I would have done:** Assumed I should already be inside the repo folder and tried `cd copilot-cli/app/` from my home directory.

**Suggested fix:** Either (1) restate "Make sure you're in the `github-copilot-101/` folder before proceeding to Exercise A," or (2) say `cd github-copilot-101/copilot-cli/app/` in Exercise A Step 2 to be explicit about the full path from anywhere.

---

### Part 1.4 — Slash commands overview, line ~120-140
**Severity:** 😕  
**What tripped me up:** The overview lists commands but doesn't mention "plan mode" (e.g., `copilot --plan` flag or Shift+Tab toggle) anywhere in Part 1. The Q&A section (line 881) later clarifies that "plan mode" is a persistent session state, distinct from the `/plan` slash command. But I'm reading top-to-bottom as a first-timer — I don't know plan mode exists until the Q&A, which breaks the flow.

**What I would have done:** Assumed `/plan` is the only "planning" mechanism in the CLI and been surprised when I hit the Q&A section or tried to use `--plan` flag and wondered what it does.

**Suggested fix:** Add one sentence to line 124–125 (the slash commands intro): "Note: There is also a persistent **plan mode** (toggled with `--plan` flag or Shift+Tab in a session) that is different from the one-off `/plan` command — see the Q&A section for details."

---

### Exercise A Step 3 — line ~178-188
**Severity:** 😕  
**What tripped me up:** The step says "On first run, you'll see: A **trust folder prompt**..." and "...a `/login` prompt or device-flow instructions...". But I don't have the CLI installed (as per my persona). I'm imagining what I'd see, and the instructions assume I'll recognize these prompts. The `/login` prompt and "device-flow instructions" are mentioned but not explained — are they the same thing? Will I see both or just one?

**What I would have done:** If I were a real learner with the CLI installed, I might type `yes` when asked to trust, but then get confused about what happens next if I see a "device-flow" prompt instead of a `/login` prompt and not know they are related.

**Suggested fix:** Clarify: "You'll see a trust folder prompt (type `yes`). Then, the CLI will ask you to authenticate with GitHub via device-flow: it will provide a code and URL — open the URL in your browser, enter the code, and authenticate. You may see this as a `/login` prompt or as explicit device-flow instructions, depending on your CLI version."

---

### Exercise A Step 4 — line ~195-198
**Severity:** 🛑  
**What tripped me up:** The expected output says I should see "A summary of the FastAPI app — it manages activity signups for a university, has endpoints like `/api/v1/register` and `/activities`, and includes validation for duplicate emails and capacity checks **(features added in Lab 3 Exercise A)**."

This statement **assumes I have done Lab 3 Exercise A**. The lab says to read prerequisites but doesn't list "Lab 3 Exercise A completion" as a prereq. I'm a first-timer. If I haven't done Lab 3, I won't know what those features are or whether the CLI's answer is correct. This breaks my ability to verify success.

**What I would have done:** I'd see the CLI's summary and think, "Um, okay, but is that right? I don't know what the app actually does because I skipped the earlier labs." I'd be stuck and would likely have to go back and skim Lab 3 to validate.

**Suggested fix:** Either (1) add to Pre-Lab Setup: "Prerequisite: Complete Lab 3 Exercise A (or at least review what the app does by reading `copilot-cli/app/backend/app.py` first)," or (2) rewrite the expected output to be app-agnostic: "...A summary of the FastAPI app, mentioning endpoints and validation features specific to your codebase." If you want to be specific, state it as "The app should list endpoints and mention validation features you added in earlier labs."

---

### Exercise B Step 2 — line ~219-231
**Severity:** 🤏  
**What tripped me up:** The step says "Try these prompts one by one:" and then lists three prompts. But it doesn't say what to expect or what to look for. For example, `@backend/` should show "all endpoints in the backend folder" — but I don't know how many there are or what they're called (again, Lab 3 context assumption). And `@.` is explained as "current directory" in a note, but the note appears *after* I'm told to use it.

**What I would have done:** I'd run the prompts, see output, and not know whether the CLI behaved correctly or is missing files.

**Suggested fix:** Reorder: put the note about `@.` *before* the prompts, or add expected-output clarifiers: "Try `Explain @backend/app.py` (you should see a description of the main app logic)," etc.

---

### Exercise C Step 1 — line ~301-304
**Severity:** 😕  
**What tripped me up:** The step says "The CLI generates a numbered plan (files to touch, steps to take) but **doesn't execute** anything. Review the plan, then type `go` to execute, or `exit` to cancel."

I'm told to "type `go`" but not whether `go` is a slash command, a literal prompt, or something else. Is it `/go`? Is it `go`? The step doesn't clarify. This is a critical interaction point where I could get stuck.

**What I would have done:** I'd probably type `/go` first, and if that didn't work, try `go` next. But if I'm reading carefully and see the pattern from earlier (slash commands are explicit), I might assume `go` is just a literal text input at the plan prompt.

**Suggested fix:** Say "...type `go` (without a slash) at the plan prompt to execute" or state it as a literal prompt example: "The CLI shows the plan. At the prompt, type `go` to proceed with execution."

---

### Exercise D Step 2 — line ~366-376
**Severity:** 😕  
**What tripped me up:** The step says "Refactor the registration endpoint and push to a new branch." The CLI is denied `git push` and `git reset --hard`. But the prompt says "push to a new branch" — does the CLI know to create a new branch first, or will it try to push to the current branch and fail? The step doesn't say what to expect when the CLI tries to push and is denied.

**What I would have done:** If I'm running this myself, I'd wait to see the CLI attempt a push, get denied, and then I'd have to decide: did the CLI respect my permission pattern (good) or did it stop mid-task (bad)? Without a clear expected outcome, I can't tell if it worked.

**Suggested fix:** Add expected output: "✅ **You should now see:** The CLI refactors the endpoint and attempts a git push, but is rejected by the permission constraint. You'll see a prompt asking to approve or deny. Type 'deny' to confirm the permission pattern works."

---

### Exercise E — line ~408-414
**Severity:** 😕  
**What tripped me up:** The task says "When an activity is full (31st student tries to sign up), show a 'Join Waitlist' button in the frontend instead of 'Sign Up'."

I don't know: (a) How many spots are in an activity by default? (b) Why 31? (c) Is there already a frontend, or am I building one from scratch? (d) What tech is the frontend written in (HTML, React, Vue)? The lab assumes I either know the app from Lab 3, or I know what "full" means in the context of the app I'm working with.

**What I would have done:** I'd run the autopilot command and watch it make decisions. But if the CLI asks me clarifying questions (e.g., "What is the max capacity?"), I wouldn't know how to answer correctly.

**Suggested fix:** Add a prerequisite note: "Before starting Exercise E, review `copilot-cli/app/backend/app.py` to see the default activity capacity (you'll find it in the model or in earlier exercises). The default is 30 spots per activity, so the 31st signup triggers the waitlist prompt." Or embed it in the task: "...When an activity reaches capacity (currently 30 spots, as defined in the model), show a 'Join Waitlist' button..."

---

### Exercise E Step 2 — line ~419-427
**Severity:** 😕  
**What tripped me up:** The step says "Observe the loop. The CLI will: 1. Read the existing code 2. Plan the changes... 5. Iterate if anything fails."

But there are 5 bullet points of *what the CLI will do*, and no expected output for each. If the CLI does something different, I won't know if it's a success or failure. For instance, what if the CLI edits `frontend/index.html` instead of `frontend/script.js`? Is that okay, or wrong? The step doesn't say.

**What I would have done:** I'd let the autopilot run and hope it's doing the right thing. Without an expected file list or a set of hooks to validate, I'd have to trust the CLI blind.

**Suggested fix:** Add: "✅ **You should see these files change:** (1) `backend/app.py` — adds a `/activities/{name}/waitlist` POST endpoint, (2) `frontend/index.html` or `frontend/script.js` — adds conditionals to show 'Join Waitlist' when capacity is reached. Verify by running the server and testing signup at capacity."

---

### Part 3 Custom agents — line ~582 vs 530
**Severity:** 🤏  
**What tripped me up:** Line 530 says "Inside an interactive `copilot` session, run: `> /agents`" (with an 's'). But line 582 says "You can list all custom agents with: `> /agent`" (no 's'). Are these two different commands, or is one a typo?

**What I would have done:** I'd try `/agents` first, and if that fails, I'd try `/agent`. But if both exist and do different things, I'd be confused about which to use.

**Suggested fix:** Verify which command is correct and use it consistently throughout the section. If both are valid aliases, state that: "The commands `/agent` and `/agents` are aliases — either works."

---

## What worked well

- **Part 1 theory is clear:** The three-mode breakdown (interactive, plan, autopilot), the CLI vs VS Code distinction, and the slash-command overview are all well-written and unambiguous. I understood the vocabulary immediately.
- **Exercise B context management is hands-on and incremental:** The `@` mention examples build logically, and the commands (`/context`, `/compact`, `/clear`, `/undo`) are all clearly explained before use.
- **Permission patterns syntax table is excellent:** The table at line 337–345 is unambiguous. I know exactly what `shell(git:*)` matches and what `url(github.com)` does.
- **Part 3 file path tables are concrete:** Each customization section (custom instructions, agents, MCP) includes a clear path table — user vs repo scope — with examples. This is beginner-friendly.
- **Q&A section is honest:** Admitting that "Hook event types are under-documented" and explaining why it's read-through (line 617) is refreshing. You're not pretending knowledge you don't have.
- **What's Next callouts are actionable:** The "Extensions to try" and "Further reading" sections give me a concrete next step, not vague advice.

---

## Overall

The lab is *logically sound* but assumes **Lab 3 familiarity** without stating it as a prerequisite, and it leaves a few **interaction points ambiguous** (e.g., typing `go` vs `/go`, which command is `/agent` vs `/agents`). If I'm a first-timer with no Lab 3 context, I'd successfully understand and *imagine* doing Exercises A–D, but I'd pause at Exercise E, uncertain about the app's structure and the expected outcomes of autopilot. I'd likely finish the lab in 90 minutes if I've already read Lab 3, or about 120 minutes if I have to double-back to understand what a "waitlist feature" means in this app.

**Critical moment of truth:** Exercise A Step 4 breaks because it references Lab 3 features without stating Lab 3 as a prerequisite. I'd have to make an assumption or backtrack.

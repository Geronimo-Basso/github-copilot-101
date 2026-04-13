# Lab 02 — Copilot Custom Instructions

Teach **GitHub Copilot** to speak your project's language. Custom instructions, path-specific rules, and reusable prompt files turn Copilot from a generic assistant into a domain expert that knows your conventions by heart.

## Table of Contents

- [What You'll Learn](#what-youll-learn)
- [Step 1: Setting Up Custom Instructions](#step-1-setting-up-custom-instructions)
- [Step 2: Path-Specific Custom Instructions — Guided Fix](#step-2-path-specific-custom-instructions--guided-fix)
- [Step 3: Path-Specific Custom Instructions — Your Turn! 🏆](#step-3-path-specific-custom-instructions--your-turn-)
- [Step 4: Agent Instructions](#step-4-agent-instructions)
- [Step 5: Reusable Prompt Files — Guided](#step-5-reusable-prompt-files--guided)
- [Step 6: Reusable Prompt Files — Your Turn! 🏆](#step-6-reusable-prompt-files--your-turn-)
- [Step 7: Skills — Guided](#step-7-skills--guided)
- [Step 8: Skills That Use Prompt Files — Your Turn! 🏆](#step-8-skills-that-use-prompt-files--your-turn-)
- [Congratulations! 🎉](#congratulations-)

## What You'll Learn

Today's goal is to learn how to **customize GitHub Copilot's behavior** so its output consistently matches your project standards — without repeating the same guidance in every prompt.

- **Custom Instructions** — Give Copilot project-wide, personal, and organization-level context
- **Path-Specific Custom Instructions** — Target conventions to specific files or directories
- **Prompt Files** — Build reusable slash commands that automate multi-step workflows
- **Skills** — Package domain expertise so Copilot writes better code in specialized areas

By the end of this lab you will have set up custom instructions at every scope, fixed non-compliant content, built prompt files to automate repetitive tasks, and created a skill that levels up your website's JavaScript and security — all on a FastAPI tourism website served by Uvicorn. 🌊

> ⚠️ **Important:** All customization files created during this lab — `copilot-instructions.md`, instruction files (`*.instructions.md`), prompt files (`*.prompt.md`), and skills (SKILL.md) — must live inside the **`.github`** directory, and this `.github` directory **must be at the root of the workspace** where the GitHub repository was cloned. If the `.github` folder is placed anywhere else, VS Code and Copilot will not detect it and the instructions/prompts will have no effect.
>
> ```
> <repo-root>/          ← workspace root (where you cloned the repo)
> ├── .github/
> │   ├── copilot-instructions.md          ← repository-level instructions
> │   ├── instructions/
> │   │   └── activities.instructions.md   ← path-specific custom instructions
> │   ├── prompts/
> │   │   └── new-activity.prompt.md       ← reusable prompt files
> │   └── skills/
> │       └── web-enhancer/
> │           └── SKILL.md                 ← domain expertise skills
> ├── AGENTS.md                            ← agent instructions
> ├── main.py
> ├── config.json
> ├── README.md
> └── ...
> ```

## Step 1: Setting Up Custom Instructions

Welcome to **SunVoyage Tours** — a tourism portal where visitors browse activities, flights, and accommodations across Mediterranean destinations. ✈️ 🏖️ 🍽️

In this step we'll set up the development environment, explore the website, and configure Copilot custom instructions at **all three scope levels**: organization, repository, and personal.

### 📖 Theory: What are Custom Instructions?

Custom instructions are **natural-language rules** you provide to Copilot. Once configured, they are automatically included in every request, ensuring consistent, context-aware responses across your entire workflow.

Think of them as a cheat-sheet you hand to a new team member on day one — except Copilot reads it every single time, never forgets, and never drifts from the guidelines.

Copilot supports instructions at **three scope levels**. Each one is designed for a different audience.

| Level | Scope | Set by | Where it lives |
| ----- | ----- | ------ | -------------- |
| **🥉 Organization** | All members across all repos | Organization owners | GitHub.com → Org Settings → Copilot → Custom Instructions |
| **🥈 Repository** | Anyone working in this repo | Any contributor | `.github/copilot-instructions.md` in the repo |
| **🥇 Personal** | Your conversations everywhere | You | VS Code `settings.json` or GitHub.com personal settings |

When multiple levels apply, Copilot uses **all of them** but respects this priority (highest first): **Personal > Repository > Organization**. Non-conflicting rules from every level are combined; when they do conflict, the higher-priority level wins.

> 💡 **Tip:** Avoid contradictions between levels. If you are getting unexpected results, review which instructions are active at each scope.

---

### Activity: Explore the project with Copilot 🔍

Before we configure any instructions, let's get the website running and use Copilot to learn about its structure.

1. Clone or open this repository in VS Code.

2. In the left sidebar, click the **Extensions** tab and verify that the **GitHub Copilot** and **Python** extensions are installed and enabled.

3. Open a terminal and create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - **macOS / Linux:**

     ```bash
     source venv/bin/activate
     ```

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the development server:

   ```bash
   python main.py
   ```

7. Open your browser at **http://127.0.0.1:8000** and explore the SunVoyage Tours website.

   > ❕ **Important:** Keep the server running throughout the lab so you can see live changes.

8. Take a moment to look at the website. You should see four activity cards, three flight routes, and three accommodation listings. Notice that some cards look polished while others are clearly missing information — **we will fix that later!**

9. Now let's ask Copilot about the project. Open the **Copilot Chat** panel and make sure you are in **Ask Mode**.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Please briefly explain the structure of this project.
   > What tech stack does it use and how are activities organized?
   > ```

   > 💡 **Tip:** You can drag files (like `main.py` or `config.json`) into the chat panel to give Copilot more context. You can also use `#codebase` to let Copilot search the whole repo.

10. Browse the project files to verify Copilot's explanation:

   | Path | Purpose |
   | ---- | ------- |
   | `main.py` | FastAPI application served with Uvicorn |
   | `config.json` | Central configuration — activities, flights, accommodations |
   | `templates/index.html` | Jinja2 HTML template for the main page |
   | `templates/activity-template.md` | Markdown template every activity README must follow |
   | `activities/` | One subfolder per activity, each with a `README.md` |
   | `static/` | CSS and JavaScript assets |

---

### 📖 Organization-Level Instructions

Organization-level instructions are set by **organization owners** (GitHub Business or Enterprise plans) and apply to **all members** across every repository in the organization. Think of this as the "company policy" that every team member inherits automatically.

**How to configure:**

Since organization instructions require **admin access to a GitHub organization**, this part is a guided review rather than a hands-on exercise.

1. Navigate to your organization's **Settings** on GitHub.com.
2. In the sidebar, click **Copilot → Custom instructions**.
3. Add your natural-language instructions and click **Save changes**. Here is an example of what SunVoyage Tours might set at the organization level:

   ```text
   SunVoyage Tours is a Mediterranean tourism company headquartered in Spain.
   All customer-facing content must be professional and inviting.
   Prices must always be displayed in euros (€).
   All dates should use European format (DD/MM/YYYY).
   Comply with EU GDPR regulations when handling user data.
   Prefer Python for backend services and vanilla JS for frontend code.
   ```

4. **Discussion question:** If this were your organization, what additional company-wide standards would you add?

   <details>
   <summary>Example ideas 💡</summary>

   - _"All API responses must include proper HTTP status codes"_
   - _"Never commit secrets or API keys to the repository"_
   - _"Write documentation in English using a professional tone"_
   - _"Prefer type hints in all Python function signatures"_

   </details>

> 📚 Full documentation: [Adding organization custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-organization-instructions)

> 🪧 **Note:** Organization instructions are currently supported for Copilot Chat on GitHub.com, Copilot code review, and the Copilot coding agent.

---

### 📖 Repository-Level Instructions

Repository custom instructions allow you to give Copilot repo-specific guidance. Copilot supports **three types** of repository custom instructions, each designed for a different use case:

| Type | File(s) | Scope | Use case |
| ---- | ------- | ----- | -------- |
| **Repository-wide** | `.github/copilot-instructions.md` | All requests in the repo | Project conventions, tech stack, coding standards |
| **Path-specific** | `.github/instructions/NAME.instructions.md` | Requests involving files that match a glob pattern | Targeted rules for specific files or directories |
| **Agent instructions** | `AGENTS.md` (anywhere in the repo) | Used by AI agents (Copilot cloud agent, etc.) | Onboarding context for autonomous agents working on your repo |

When multiple types apply to a request, Copilot uses **all of them** — they complement each other. Path-specific instructions combine with repository-wide instructions when both match.

> 💡 **Tip:** You'll explore all three types during this lab. We'll start with repository-wide custom instructions now, then cover path-specific custom instructions in **Step 2**, and agent instructions after **Step 3**.

> 🪧 **Note:** Although we don't recommend it, you can **enable or disable custom instructions** at any time. This only affects your own use of Copilot Chat — not other users.
>
> To toggle them in VS Code:
> 1. Open the Settings editor (`Cmd+,` on Mac / `Ctrl+,` on Linux/Windows).
> 2. Type `instruction file` in the search box.
> 3. Select or clear the checkbox under **Code Generation: Use Instruction Files**.

---

#### Repository-Wide Custom Instructions

Repository-wide instructions live inside the repo in a file called **`.github/copilot-instructions.md`**. They are automatically attached to every Copilot Chat request made in the context of that repository.

**How to configure:**

1. Create a `.github/copilot-instructions.md` file in the root of your repository.
2. Write natural-language instructions describing your project.
3. Save — Copilot picks it up immediately.

> 📚 Full documentation: [Adding repository custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions?tool=vscode)

> 💡 **Tip:** Keep instructions short and focused on the **"how"** of the project: purpose, folder structure, coding standards, key tools, expected formats, etc.

### Activity: Create repository instructions with Copilot 🤖

Right now Copilot doesn't **truly** know our project conventions. If we ask it to create content, it might use the wrong price format, inconsistent durations, or a casual tone. Let's fix that by creating repository-level instructions.

Instead of creating the file manually, let's use **Agent Mode** to do the heavy lifting!

1. Open the **Copilot Chat** panel and switch to **Agent** mode.

2. Ask Copilot to create the instructions file for you. Provide enough context so it understands what the file should contain:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Create a .github/copilot-instructions.md file for this project.
   > It should describe:
   > - The project (a tourism portal built with Python/FastAPI/Uvicorn)
   > - The tech stack (FastAPI, Jinja2, vanilla JS, JSON config)
   > - The project structure (main.py, config.json, templates/, activities/, static/)
   > - Conventions: prices in €XX / person format, locations as City Country,
   >   durations in full words, Title Case categories, activity READMEs must follow
   >   the template in templates/activity-template.md, professional tone.
   > ```

3. Review the file Copilot creates. It should look similar to this:

   <details>
   <summary>Expected content 📄</summary>

   ```markdown
   # SunVoyage Tours — Project Instructions

   ## Project Description

   SunVoyage Tours is a tourism portal built with **Python and FastAPI**, served via **Uvicorn**. Visitors can browse tourist activities, flights, and accommodations across Mediterranean destinations.

   ## Tech Stack

   - **Backend:** Python 3 / FastAPI / Uvicorn
   - **Templating:** Jinja2 (HTML templates in `templates/`)
   - **Frontend:** Vanilla HTML, CSS, and JavaScript (in `static/`)
   - **Data:** JSON-based configuration (`config.json`)

   ## Project Structure

   - [`main.py`](../main.py) — FastAPI application entry point
   - [`config.json`](../config.json) — Central data source for activities, flights, and accommodations
   - [`templates/`](../templates/) — Jinja2 HTML templates and content templates
   - [`activities/`](../activities/) — Each activity has its own subfolder with a `README.md`
   - [`static/`](../static/) — CSS stylesheets and JavaScript files

   ## Conventions

   - All prices must use the euro symbol and include "/ person" or "/ night" suffix (e.g., `€75 / person`)
   - Locations must follow the format `City, Country` (e.g., `Costa del Sol, Spain`)
   - Duration values must use full words (e.g., `2 hours` not `2h`)
   - Activity categories must use Title Case (e.g., `Water Sports` not `water`)
   - Every activity folder must contain a `README.md` following the structure in [`templates/activity-template.md`](../templates/activity-template.md)
   - Keep the website professional and customer-friendly in tone
   ```

   </details>

4. If Copilot's output is missing any conventions, provide follow-up feedback to refine it. Remember — Copilot keeps the conversation history, so you can iterate!

5. **Accept the changes** and save the file.

   > ❕ **Important:** The file must be at exactly `.github/copilot-instructions.md`. If Copilot placed it somewhere else, move it.

### Activity: Test your repository instructions ✅

Now let's verify that Copilot actually uses the instructions you just created.

1. Make sure you are in **Agent** mode in Copilot Chat.

2. Ask Copilot a question that exercises your conventions:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > What conventions does the project have regarding the city, the money and the title of the activity? 
   > ```

3. Copilot should respond with `€50 / person` — following the convention you established.

4. Check the **References** section at the bottom of Copilot's response. You should see `.github/copilot-instructions.md` listed, confirming it was used.

   <details>
   <summary>Don't see the reference? 🔍</summary>

   - Make sure the file is saved at exactly `.github/copilot-instructions.md` (not in a subfolder).
   - Restart VS Code if the file was just created.
   - Verify the setting **"Enable custom instructions"** is checked in VS Code settings (search for `copilot instructions`).

   </details>

5. Try one more test — ask Copilot to describe the project in its own words:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Can you briefly describe the project structure?
   > ```

   Copilot should now mention FastAPI, Uvicorn, activities, flights, and accommodations — language it wouldn't have known without your instructions. That alone is a huge productivity boost for onboarding teammates!

   **🎯 Goal: Copilot references your instruction file and follows the project conventions. ✅**

---

### 📖 Personal-Level Instructions

Personal instructions reflect your **individual role and preferences**. They follow you across all projects and are not committed to any repository. They are configured through **GitHub.com**, not inside the IDE.

**How to configure:**

1. Open [Copilot Chat](https://github.com/copilot).
2. Click your profile picture → **Personal instructions**.
3. Type your preferences and click **Save**.

When multiple levels apply, Copilot uses **all of them** but respects this priority (highest first): **Personal > Repository > Organization**. Non-conflicting rules from every level are combined; when they do conflict, the higher-priority level wins.

> 📚 Full documentation: [Adding personal custom instructions for GitHub Copilot](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-personal-instructions)

---

### Priority Recap

Now that you understand the three instruction levels, let's make sure the priority model is clear:

| Priority | Level | Example |
| -------- | ----- | ------- |
| 🥇 Highest | **Personal** | Your individual role, language preferences, focus areas |
| 🥈 Medium | **Repository** | Project structure, conventions, formatting rules |
| 🥉 Lowest | **Organization** | Company-wide standards (euros, GDPR, professional tone) |

**Discussion question:** What if the organization says "use British English" but your personal instructions say "use European Spanish"?

<details>
<summary>Answer 💡</summary>

All three instruction sets are sent to Copilot, but **personal instructions take highest priority**, followed by repository, then organization. If your personal instruction says "use European Spanish", Copilot will favor that over the org-level "British English" preference. The remaining non-conflicting instructions from all levels still apply.

</details>

---

## Step 2: Path-Specific Custom Instructions — Guided Fix

Great work setting up repository-wide custom instructions! Now let's tackle a more targeted scenario.

🐛 **THERE IS A PROBLEM IN THE ACTIVITY FILES** 🐛

The activity content files in this repository **don't all follow the same standards**. Open `activities/kayaking/README.md` and compare it with `activities/jet-skiing/README.md` — you'll immediately spot the inconsistencies. The kayaking file has wrong formatting, missing sections, and an unprofessional tone.

We need a way to automatically enforce the activity template on every activity markdown file. That's where **path-specific custom instructions** come in.

### 📖 Theory: Path-Specific Custom Instructions

Instruction files (`*.instructions.md`) provide Copilot with targeted guidance for **specific files or directories**. Unlike repository-wide instructions that apply everywhere, these use the `applyTo` field in the [frontmatter](https://jekyllrb.com/docs/front-matter/) with [glob syntax](https://code.visualstudio.com/docs/editor/glob-patterns) to target specific paths.

VS Code looks for `*.instructions.md` files in the `.github/instructions/` directory by default. When Copilot works on a file that matches the glob pattern, the instructions are **automatically attached** — no manual action required.

> 💡 **Tip:** Instructions should focus on **HOW** a task should be done — the guidelines, standards, and conventions for that particular part of the codebase.

### Activity: Identify the problem 🔍

1. Open the file `activities/kayaking/README.md` and review its content.

2. Now open `templates/activity-template.md` to see the expected structure.

3. Compare the two files. Notice the kayaking file has multiple issues:

   | Issue | Kayaking File | Expected |
   | ----- | ------------- | -------- |
   | Title | `# Kayaking in Mallorca` | `# 🛶 Kayaking Adventure` (with emoji) |
   | Overview section | Missing entirely | Required with 1–2 sentences |
   | Details table | Plain text (`Duration: 2h`) | Structured markdown table |
   | Price format | `45 euro` | `€45 / person` |
   | Duration format | `2h` | `2 hours` |
   | Location format | `Mallorca` | `Mallorca, Spain` |
   | What's Included | Missing | Required |
   | Safety Information | Missing | Required |
   | Requirements | Missing | Required (separate from "What to bring") |
   | Booking section | Missing | Required |
   | Tone | Casual (`trust us!`) | Professional and customer-friendly |

4. Also check the kayaking entry in `config.json` — it has matching issues (empty image, plain `"45"` price, lowercase category `"water"`).

### Activity: Create activity-specific instructions with Copilot 🤖

Instead of writing the instruction file from scratch, let's ask **Agent Mode** to create it for us — while also teaching it what the file needs to contain.

1. Open **Copilot Chat** and switch to **Agent** mode.

2. Drag the `templates/activity-template.md` file into the chat as context, then ask Copilot to generate the instruction file:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Create a file at .github/instructions/activities.instructions.md
   > It should have an applyTo frontmatter targeting "activities/**/*.md"
   > and contain rules for activity markdown files:
   > - Must follow the structure in templates/activity-template.md
   > - Each activity must be a README.md in its own subfolder
   > - Section headers must include the correct emoji icons
   > - Prices: €XX / person format
   > - Durations: full words (2 hours not 2h)
   > - Locations: City, Country format
   > - Categories: Title Case
   > - Tone: professional and inviting, no slang
   > ```

3. Review the file Copilot creates. It should have a YAML frontmatter block with `applyTo: "activities/**/*.md"` and a set of clear markdown rules.

   <details>
   <summary>Expected structure 📄</summary>

   The file should look similar to:

   ```markdown
   ---
   applyTo: "activities/**/*.md"
   ---

   # Activity Markdown Structure Guidelines

   All activity markdown files must follow these guidelines:

   ## 1. Template Usage

   - Activity markdown files must follow the structure in [`templates/activity-template.md`](../../templates/activity-template.md).
   - Each activity must be a `README.md` file inside its own subfolder of `activities/`.
   - Do not skip or remove required sections from the template.

   ## 2. Section Guidance

   The section headers must match the template structure exactly, including the emoji icons:

   - **Title**: Use a relevant emoji followed by the activity name (e.g., `# 🛶 Kayaking Adventure`).
   - **📋 Overview**: Write 1–2 sentences describing the experience. Use professional, customer-friendly language.
   - **📍 Details**: Present details as a markdown table with fields: Category, Location, Duration, Price, Difficulty, Min. Age.
   - **✅ What's Included**: Bullet list of what the customer gets.
   - **📝 Requirements**: Bullet list of prerequisites or things to bring.
   - **⚠️ Safety Information**: Bullet list of safety warnings.
   - **📞 Booking**: Contact information for reservations.

   ## 3. Formatting Rules

   - **Prices**: Always use the format `€XX / person` (euro symbol, space, slash, space, "person").
   - **Durations**: Use full words (e.g., `2 hours` not `2h`).
   - **Locations**: Use `City, Country` format (e.g., `Mallorca, Spain`).
   - **Categories**: Use Title Case (e.g., `Water Sports` not `water`).
   - **Tone**: Professional and inviting. Avoid slang or overly casual phrasing.
   ```

   </details>

4. **Accept the changes** and save the file.

### Activity: Fix the kayaking activity with Copilot 🛶

Now the instruction file exists and automatically applies to any file under `activities/**/*.md`. Let's put it to the test.

1. Open `activities/kayaking/README.md` in VS Code.

2. Open **Copilot Chat** and make sure you are in **Agent** mode.

3. With the kayaking file open, ask Copilot to fix it:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Update this activity file to follow the project standards and template structure
   > ```

4. Observe how Copilot references the activity-specific instructions (`.github/instructions/activities.instructions.md`) in its response references.

5. Review the proposed changes:
   - The title should now have an emoji
   - An Overview section should be added
   - Details should be in a proper markdown table
   - Prices, durations, and locations should follow the correct format
   - Missing sections (What's Included, Safety, Requirements, Booking) should be added
   - The tone should be professional

6. **Accept the changes** and save the file.

### Activity: Fix the kayaking config entry 🔧

The README is fixed, but the `config.json` entry for kayaking is still non-compliant. Let's fix that too.

1. Open `config.json` and find the `kayaking` entry.

2. In **Agent** mode, ask Copilot:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > The kayaking entry in config.json doesn't follow our conventions.
   > Fix the category, price, duration, location, and image fields
   > to match the format used by the other activities.
   > ```

3. Verify the updated entry looks similar to:

   ```json
   {
     "id": "kayaking",
     "name": "Kayaking Adventure",
     "category": "Water Sports",
     "price": "€45 / person",
     "duration": "2 hours",
     "location": "Mallorca, Spain",
     "image": "🛶",
     "folder": "activities/kayaking"
   }
   ```

4. **Restart the server** (`Ctrl+C` then `python main.py`) and refresh the browser to verify the kayaking card now looks correct on the website.

   **🎯 Goal: The kayaking card on the website displays a proper emoji, formatted price, full duration, and correct location. ✅**

<details>
<summary>Having trouble? 🤷</summary>

- Make sure the instruction file is at `.github/instructions/activities.instructions.md`.
- The `applyTo` field must be `"activities/**/*.md"` — check for typos.
- Restart VS Code if the instructions don't seem to apply.
- If the website doesn't update, make sure you saved `config.json` and restarted the server.

</details>

---

## Step 3: Path-Specific Custom Instructions — Your Turn! 🏆

You've successfully fixed the kayaking activity with Copilot's help. Now it's time to take the training wheels off and apply what you've learned on your own!

### The Scenario

Open `activities/sightseeing/README.md`. This file has a **different set of problems** from the kayaking file:

- The title is missing its emoji icon
- Section names don't match the template (`"About this tour"` instead of `"📋 Overview"`, `"Extras"` instead of `"✅ What's Included"`)
- Details are in a bullet list instead of a markdown table
- The `"⚠️ Safety Information"` and `"📝 Requirements"` sections are completely missing
- The `"📞 Booking"` section uses a different email and is missing the phone number

### Your Task

1. Use Copilot in **Agent** mode to **update the sightseeing activity** so it matches the activity template structure — just like you did with the kayaking file.

2. Think about whether the existing `.github/instructions/activities.instructions.md` file already covers this case, or if you need to adjust it.

3. Don't forget to verify the result matches the template by comparing it with `activities/jet-skiing/README.md` (a properly formatted example).

4. **Bonus:** Check if the sightseeing entry in `config.json` also needs corrections. Does the pricing format, category casing, or any other field need updating?

<details>
<summary>Hints 💡</summary>

- The instruction file you created in Step 2 uses `applyTo: "activities/**/*.md"` — it already applies to the sightseeing file too! You can reuse the same Copilot prompt.
- Open the sightseeing file first, then ask Copilot in **Agent** mode:

  > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
  >
  > ```prompt
  > Update this activity file to follow the project standards and template structure
  > ```

- After fixing the README, ask Copilot to also review and fix the sightseeing entry in `config.json`.

</details>

<details>
<summary>Expected result ✅</summary>

After fixing, the sightseeing `README.md` should have:
- A title with an emoji: `# 🏛️ City Sightseeing Tour`
- All six required sections with correct emoji headers
- A structured details table with proper formatting
- Professional, customer-friendly language throughout
- Full booking contact information

</details>

**🎯 Goal: Both non-compliant activities (kayaking and sightseeing) are now fixed to match the template. All activity cards on the website look consistent and professional. ✅**

---

## Step 4: Agent Instructions

Now that you've set up repository-wide and path-specific custom instructions, let's complete the trio with **agent instructions** — the third type of repository custom instruction.

### 📖 Theory: What are Agent Instructions?

Agent instructions are designed for **AI agents** — like Copilot cloud agent (formerly known as coding agent) — that work autonomously on your codebase.

Unlike `copilot-instructions.md` (which targets chat interactions), agent instructions help an AI agent that's **seeing your repo for the first time** understand how to navigate, build, test, and contribute effectively — like onboarding documentation for an autonomous team member.

**Key details:**

| Property | Value |
| -------- | ----- |
| **File name** | `AGENTS.md` |
| **Location** | Anywhere in the repository (the nearest one in the directory tree takes precedence) |
| **Scope** | Used by AI agents when working autonomously on the repo |
| **Alternatives** | `CLAUDE.md` or `GEMINI.md` in the repo root (for model-specific agents) |

**What to include:**

- A summary of what the repository does and the tech stack
- How to build, test, lint, and run the project
- Key architectural decisions and project layout
- Common pitfalls, workarounds, and validation steps
- Any CI/CD requirements the agent should be aware of

> 📚 Full specification: [agentsmd/agents.md repository](https://github.com/agentsmd/agents.md)
>
> 📚 Full documentation: [Adding repository custom instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions?tool=vscode#creating-repository-wide-custom-instructions-1)

### Activity: Create an `AGENTS.md` file 🤖🧭

Let's create an agent instructions file so that any AI agent working on the SunVoyage Tours project can hit the ground running.

1. Open **Copilot Chat** in **Agent** mode.

2. Ask Copilot to generate the agent instructions:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Create an AGENTS.md file in the root of this repository.
   > It should help an AI agent that has never seen this project before
   > understand how to work on it effectively.
   > Include:
   > - What the project does (tourism portal, FastAPI/Uvicorn)
   > - How to install dependencies and run the dev server
   > - The project structure (main.py, config.json, templates/, activities/, static/)
   > - Coding conventions (price format, location format, duration format, Title Case categories)
   > - How to add a new activity (create a folder in activities/ with a README.md following templates/activity-template.md)
   > - Any validation steps (check that main.py runs without errors)
   > ```

3. Review the file Copilot creates. It should contain practical, actionable guidance — not just a description. A good `AGENTS.md` reads like a checklist an agent can follow.

   <details>
   <summary>Expected content 📄</summary>

   ```markdown
   # AGENTS.md — SunVoyage Tours

   ## Project Overview
   SunVoyage Tours is a tourism portal built with Python/FastAPI, served via Uvicorn.
   Visitors browse activities, flights, and accommodations across Mediterranean destinations.

   ## Quick Start
   ```bash
   pip install -r requirements.txt
   python main.py
   ```
   The server starts at http://127.0.0.1:8000.

   ## Project Structure
   - `main.py` — FastAPI entry point
   - `config.json` — Central data source (activities, flights, accommodations)
   - `templates/` — Jinja2 HTML templates
   - `templates/activity-template.md` — Template for new activity READMEs
   - `activities/` — Each activity has its own folder with a `README.md`
   - `static/` — CSS and JavaScript files

   ## Conventions
   - Prices: `€XX / person` or `€XX / night`
   - Locations: `City, Country`
   - Durations: full words (`2 hours`, not `2h`)
   - Categories: Title Case (`Water Sports`)
   - Activity READMEs must follow `templates/activity-template.md`
   - Professional, customer-friendly tone

   ## Adding a New Activity
   1. Create a new folder under `activities/` (e.g., `activities/sailing/`)
   2. Add a `README.md` following the template in `templates/activity-template.md`
   3. Register the activity in `config.json`
   4. Run `python main.py` to verify it loads correctly

   ## Validation
   - Run `python main.py` and verify no errors on startup
   - Visit the homepage and confirm the new activity appears
   ```

   </details>

4. **Accept the changes** and save the file in the repository root.

5. **Discuss:** How is `AGENTS.md` different from `.github/copilot-instructions.md`?

   <details>
   <summary>Answer 💡</summary>

   `copilot-instructions.md` is automatically attached to **every Copilot Chat request** and focuses on coding conventions and response formatting. `AGENTS.md` is used by **autonomous AI agents** (like Copilot cloud agent) and focuses on practical onboarding: how to build, test, navigate, and validate changes. Think of `copilot-instructions.md` as a style guide and `AGENTS.md` as a getting-started guide for a new developer.

   </details>

   **🎯 Goal: You now have agent instructions that help AI agents work effectively on your repo. ✅**

---

## Step 5: Reusable Prompt Files — Guided

Now that all existing activities follow a consistent structure, you want to make it easy to **create new activities** without manually setting up every file. This is a perfect scenario for a **prompt file** — a reusable slash command that automates repetitive workflows.

### 📖 Theory: What are Prompt Files?

Prompt files (`*.prompt.md`) define reusable prompts that appear as **slash commands** (`/`) in Copilot Chat. They can reference other workspace files (like templates and configurations) to provide context.

| Aspect | Details |
| ------ | ------- |
| **File extension** | `.prompt.md` |
| **Default location** | `.github/prompts/` directory |
| **Invocation** | Type `/prompt-name` in the Copilot Chat input |
| **Context** | Can reference files using markdown links or `#file:` syntax |
| **Scope** | Reusable by anyone who clones the repository |

> 💡 **Tip:** Use prompt files to define repeatable tasks and workflows. Focus on **WHAT** needs to be done. Reference instructions for the **HOW**.

See the [VS Code Docs: Prompt Files](https://code.visualstudio.com/docs/copilot/copilot-customization#_prompt-files-experimental) page for more information.

### Activity: Create the new activity prompt with Copilot 🤖

Let's use **Agent Mode** to help us write the prompt file itself — prompt files are just markdown, and Copilot is great at writing markdown!

1. Open **Copilot Chat** in **Agent** mode.

2. Ask Copilot to create the prompt file:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Create a reusable prompt file at .github/prompts/new-activity.prompt.md
   > that automates creating a new tourism activity.
   > It should:
   > - Have frontmatter with agent: agent, a description, and an argument-hint
   > - Step 1: Gather activity info from the user if not provided
   > - Step 2: Create a new directory in activities/ with a README.md
   >   following the structure from templates/activity-template.md
   > - Step 3: Update config.json with the new activity entry
   >   using the same field format as existing entries
   > Reference the template and config.json files using relative markdown links.
   > ```

3. Review the file Copilot creates. It should contain:

   <details>
   <summary>Expected content 📄</summary>

   ```markdown
   ---
   agent: agent
   description: Create a new tourism activity for the SunVoyage website
   argument-hint: Provide the activity name and type (e.g., "Scuba Diving - Water Sports")
   ---

   # Create New Tourism Activity

   Your goal is to generate a new activity for the SunVoyage Tours website.

   ## Step 1: Gather Activity Information

   If not already provided by the user, ask for:
   - Activity name
   - Category (Water Sports, Cultural, Gastronomy, Adventure, Wellness, etc.)
   - Location (City, Country)
   - Approximate price and duration

   ## Step 2: Create Activity Structure

   1. Create a new directory in the `activities` folder with a kebab-case name based on the activity (e.g., `scuba-diving`)
   2. Create a `README.md` file in that directory following the structure from [activity-template.md](../../templates/activity-template.md)
   3. Fill in all sections with realistic, professional content appropriate for a tourism website

   ## Step 3: Update Website Configuration

   Update the activities list in [config.json](../../config.json) to include the new activity. Use the same field format as existing entries:
   - `id`: kebab-case identifier
   - `name`: display name
   - `category`: Title Case category
   - `price`: format `€XX / person`
   - `duration`: full words (e.g., `2 hours`)
   - `location`: `City, Country`
   - `image`: a relevant emoji
   - `folder`: path to the activity folder
   ```

   </details>

4. **Accept the changes** and save the file.

### Activity: Test the new activity prompt 🧪

1. Open **Copilot Chat** and ensure you're in **Agent** mode.

2. Type `/new-activity` in the chat input. You have two options:

   - Type just `/new-activity` without details — Copilot will ask what the activity should be.
   - Include the details directly: `/new-activity Sunset Sailing Cruise - Water Sports in Ibiza, Spain`

   <details>
   <summary>💡 Activity ideas to try</summary>

   ```text
   Scuba Diving Adventure - Water Sports in Costa Brava, Spain
   ```

   ```text
   Flamenco Dance Workshop - Cultural in Seville, Spain
   ```

   ```text
   Mountain Hiking Trail - Adventure in Sierra Nevada, Spain
   ```

   ```text
   Tapas Cooking Class - Gastronomy in Valencia, Spain
   ```

   ```text
   Sunset Yacht Cruise - Water Sports in Mallorca, Spain
   ```

   </details>

3. Watch Copilot work. It should:
   - Create a new folder under `activities/`
   - Generate a `README.md` following the template structure
   - Update `config.json` with a new entry

4. **Restart the server** and verify the new activity appears on the website.

5. Compare the generated content with your existing activities. Does it follow all the conventions from your instructions?

   > 🪧 **Note:** The activity-specific instructions (`activities.instructions.md`) are automatically applied because the new file matches `activities/**/*.md`. Your prompt file defined **what** to do, and the instruction file enforced **how** to do it!

<details>
<summary>Activity not showing on the website? 🔍</summary>

- Make sure you restarted the server after changes.
- Verify `config.json` was updated correctly (valid JSON, new entry in the `activities` array).
- Check that the new folder exists under `activities/` with a `README.md` file.

</details>

**🎯 Goal: A single slash command generates a fully compliant new activity — folder, README, and config entry — in seconds. ✅**

---

## Step 6: Reusable Prompt Files — Your Turn! 🏆

You've automated activity creation with a prompt file. Now think about what **other repetitive tasks** in this project could benefit from the same approach.

### The Scenario

The SunVoyage Tours website also manages **flights** and **accommodations** through `config.json`. Adding new entries requires knowing the exact JSON structure, field names, and formatting conventions. This is error-prone and slow when done manually.

### Your Task

Create a **new prompt file** that automates one of these workflows:

1. **Option A:** Create a `/new-flight` prompt that adds a new flight route to `config.json`
2. **Option B:** Create a `/new-accommodation` prompt that adds a new accommodation listing to `config.json`
3. **Option C (Advanced):** Create a `/travel-package` prompt that bundles a flight + accommodation + activity into a special package deal and adds it as a new section in `config.json` and the website

### Requirements

- The prompt file must be in `.github/prompts/` with the `.prompt.md` extension
- It must include `agent: agent`, a `description`, and an `argument-hint` in the frontmatter
- It must reference `config.json` so Copilot creates the new activity that will appear in the website
- It should guide Copilot to follow the same formatting conventions (euro prices, location format, etc.)

> 💡 **Tip:** You can use **Agent Mode** to generate the prompt file itself — just like we did in Step 4! Try asking Copilot:
>
> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
>
> ```prompt
> Create a prompt file similar to .github/prompts/new-activity.prompt.md
> but for adding a new flight route to the website.
> ```

<details>
<summary>Hints 💡</summary>

- Look at the existing flight entries in `config.json` to understand the field structure (`id`, `route`, `airline`, `price`, `duration`, `frequency`).
- Your prompt file should reference `config.json` with a relative markdown link just like the activity prompt does: `[config.json](../../config.json)`.
- For Option C, you would need to add a new `"packages"` array to `config.json` and update `templates/index.html` to display it. This is a bigger challenge — consider using **Plan Agent** first to design the approach!
- Start with Option A or B if this is your first time — Option C is a stretch goal.

</details>

<details>
<summary>Example: /new-flight prompt structure ✅</summary>

```markdown
---
agent: agent
description: Add a new flight route to the SunVoyage website
argument-hint: Provide route details (e.g., "Berlin → Mallorca, 2h 45m, €159")
---

# Add New Flight Route

Your goal is to add a new flight route to the SunVoyage Tours website.

## Step 1: Gather Flight Information

If not already provided, ask for:
- Origin and destination cities
- Flight duration
- Price
- Frequency (which days of the week)

## Step 2: Update Configuration

Add the new flight to the `flights` array in [config.json](../../config.json) following the existing format:
- `id`: kebab-case short identifier (e.g., `ber-mal`)
- `route`: use arrow format (e.g., `Berlin → Mallorca`)
- `airline`: always `SunVoyage Air`
- `price`: euro format (e.g., `€159`)
- `duration`: compact format (e.g., `2h 45m`)
- `frequency`: comma-separated days or `Daily`
```

</details>

**🎯 Goal: You have at least one additional prompt file that automates adding flights, accommodations, or packages to the website. ✅**

---

## Step 7: Skills — Guided

You've customized how Copilot understands your project and automated content creation. But what about the **quality of the code** it writes? Right now, when Copilot generates JavaScript for the website, it uses generic knowledge. It doesn't know we prefer certain patterns or that we care about security.

That's where **Skills** come in. A skill is a small file of **expert knowledge** that Copilot reads before writing code — like giving it a cheat-sheet from a senior developer.

### 📖 Theory: What are Skills?

A skill is a `SKILL.md` file that gives Copilot domain expertise. While instructions say "follow these rules" and prompts say "do this task", a skill says **"here is how an expert does it — apply this knowledge."**

| Aspect | Details |
| ------ | ------- |
| **File name** | `SKILL.md` |
| **Location** | Inside a folder under `.github/skills/` |
| **Frontmatter** | `name` and `description` — tells Copilot when to use it |
| **Content** | Best practices, patterns, and do's/don'ts |

> 💡 **Tip:** Keep skills focused on one area. A small, specific skill is more useful than a massive generic one.

❕ **Important:** The `description` field in the frontmatter is **the most critical part** of a skill. Copilot reads it to decide whether to load the skill for a given task. If the description doesn't mention the right keywords (e.g., "JavaScript", "security", "web"), Copilot won't know when to apply it — and your skill will be ignored. Make the description specific and include the key terms that match the kind of tasks you want the skill to activate for.

See the [VS Code Docs: Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills) page for more information.

### Activity: Create a simple web-enhancer skill 🧑‍💻

We'll build a tiny skill that teaches Copilot two things: **modern JavaScript patterns** and **basic security rules**. This is enough to noticeably improve the code it generates for our website.

1. Create the skill file:

   ```text
   .github/skills/web-enhancer/SKILL.md
   ```

2. Add the following content:

   ```markdown
   ---
   name: web-enhancer
   description: 'Best practices for JavaScript and security in web projects. Use when writing or modifying HTML, CSS, or JavaScript code.'
   ---

   # Web Enhancer Skill

   Apply these rules when writing or modifying frontend code.

   ## JavaScript Rules

   - Use `const` and `let` — never `var`
   - Use `addEventListener` — never inline `onclick` attributes
   - Use `querySelector` / `querySelectorAll` for DOM selection
   - Use `async`/`await` with try/catch for fetch calls
   - Use template literals instead of string concatenation
   - Always handle the case where an element might not exist before using it

   ## Security Rules

   - Use `textContent` instead of `innerHTML` when inserting user-provided text
   - Never use `eval()` or `new Function()` with dynamic strings
   - Validate and sanitize any user input before using it
   - Do not store sensitive data in `localStorage`

   ## Do's and Don'ts

   - ✅ Use semantic HTML (`<nav>`, `<main>`, `<section>`, `<article>`)
   - ✅ Add `loading="lazy"` to images below the fold
   - ✅ Use `defer` for script tags
   - ✅ Provide error feedback to the user, not just console logs
   - ❌ Never insert unsanitized user input into the DOM
   - ❌ Never use inline styles — use CSS classes
   - ❌ Never ignore errors from fetch calls
   ```

3. Save the file.

### Activity: See the skill in action 🚀

Before testing the skill, take a moment to look at the current state of the code. Open `static/js/app.js` and `templates/index.html` and notice these problems — the website works fine, but the code is **full of bad practices**:

| File | Issue | Skill rule violated |
| ---- | ----- | ------------------- |
| `app.js` | Uses `var` everywhere | JS: use `const`/`let` |
| `app.js` | Uses `getElementById` and `getElementsByTagName` | JS: use `querySelector` |
| `app.js` | Uses `anchors[i].onclick = ...` | JS: use `addEventListener` |
| `app.js` | Uses string concatenation (`"Loaded " + data.length`) | JS: use template literals |
| `app.js` | `fetch()` has no error handling (no try/catch, no `.catch()`) | JS: use async/await with try/catch |
| `app.js` | Sets `innerHTML` with concatenated strings | Security: use `textContent` |
| `app.js` | Stores `"demo-secret-token-abc123"` in `localStorage` | Security: don't store secrets |
| `index.html` | Inline styles on the hero subtitle (`style="font-size:..."`) | Don'ts: use CSS classes |
| `index.html` | Scroll-to-top button created entirely with inline styles | Don'ts: use CSS classes |
| `index.html` | Uses `btn.onclick = ...` and `window.onscroll = ...` | JS: use `addEventListener` |
| `index.html` | Script tag at the bottom without `defer` | Do's: use `defer` |

Now let's ask Copilot to fix them — with the skill guiding the output.

1. Open **Copilot Chat** in **Agent** mode.

2. Ask Copilot to clean up the code:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Review the JavaScript in static/js/app.js and the inline scripts in
   > templates/index.html. Fix any code quality and security issues.
   > ```

> 💡 **Tip:** Drag the files to the chat to give it more context.

3. Review the changes. With the skill active, Copilot should:
   - Replace `var` with `const`/`let`
   - Switch from `getElementById`/`getElementsByTagName` to `querySelector`/`querySelectorAll`
   - Replace `onclick`/`onscroll` assignments with `addEventListener`
   - Use template literals instead of string concatenation
   - Wrap `fetch()` in `async`/`await` with try/catch
   - Replace `innerHTML` with `textContent` or safe alternatives
   - Remove the secret token from `localStorage`
   - Move inline styles to CSS classes
   - Add `defer` to the script tag

4. **Accept the changes**, restart the server, and verify everything still works.

   **🎯 Goal: Copilot fixes all the bad practices because the skill provides expert guidance before it modifies code. ✅**

<details>
<summary>Skill not being applied? 🤷</summary>

- Make sure the file is at exactly `.github/skills/web-enhancer/SKILL.md`.
- The `description` in the frontmatter must mention keywords like "JavaScript", "web", "HTML" so Copilot knows when to load it.
- Restart VS Code if the skill was just created.

</details>

---

## Step 8: Skills That Use Prompt Files — Your Turn! 🏆

You've seen how a skill improves code quality. Now let's discover another powerful feature: **skills can reference other files** — including the prompt files you already created.

This means you can build a skill that combines expert knowledge with an automated workflow. Think of it as giving Copilot both the **"what to do"** (the prompt) and the **"how to do it well"** (the skill rules).

### 📖 Theory: Skills Can Reference Files

Inside a `SKILL.md` file, you can link to other files in your workspace using regular markdown links — just like prompt files do. When Copilot loads the skill, it also reads the linked files for additional context.

This is powerful because it lets you **reuse** the prompt files you already built. For example, a skill can say: "When creating activities, follow the workflow in the new-activity prompt file, but also apply these extra rules."

### Your Task

Create a new skill called that specializes in creating activities. In this exercice you should:

- Reference the `/new-activity` prompt file you created in Step 4 (so Copilot knows the workflow)
- Override the location so that it's **always** `Mallorca, Spain`
- Override the category so that it's **always** `WaterSport`
- Always ask the user about the **price**, **name** and **duration** (don't assume)
- Let Copilot fill out the rest based on the prompt-file

### How to do it

1. Create the skill file:

   ```text
   .github/skills/activity-creation/SKILL.md
   ```

2. Add the following content:

   ```markdown
   ---
   name: ##
   description: '##. Use when ##'
   ---

   # Activities Skill

   When creating new activities, follow the workflow in
   [enter-prompt-file-name](enter-path-to-prompt-file) but apply
   these additional rules:

   ## Location

   - 
   
   ## Category

   -   

   ## Required Information

   - 
   - 
   -  
   - If any of these fields are missing from the user's request, do NOT proceed. Instead, ask the user to provide the missing values before creating anything.
   - 
   ```

3. Save the file.

   > 🪧 **Note:** See how the skill links to `new-activity.prompt.md`? This tells Copilot to read the prompt file's workflow (create folder, create README, update config.json) while also applying the activity-specific rules. You don't have to repeat the full workflow — just reference it and add your overrides.

### Activity: Test the Activity Creation skill 🏝️

1. Open **Copilot Chat** in **Agent** mode.

2. Ask Copilot to create a new activity:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Create a new scuba-diving activity
   > ```

3. Observe how Copilot behaves:
   - It should **not ask** for the location (the skill says it's always Mallorca, Spain)
   - It should **not ask** for the category (the skill says it's always WaterSport)
   - It should follow the same workflow from the prompt file (create folder, README, update config.json)

4. **Restart the server** and verify the new activity appears on the website with everything as you specified.

   **🎯 Goal: The skill combines the new-activity prompt workflow with specific rules — showing that skills can reference and extend existing files. ✅**

<details>
<summary>Skill not working? 🤷</summary>

- Make sure the `description` mentions "creating" and "activity" — Copilot uses the description to decide when to load it.
- Check that the relative path to the prompt file is correct: `../../prompts/new-activity.prompt.md` ().
- Restart VS Code if the skill was just created.

</details>

---

## Congratulations! 🎉

You've completed **Lab 02 — Copilot Custom Instructions**! Here's a recap of what you learned:

| Step | What You Did |
| ---- | ------------ |
| **Step 1** | Set up custom instructions: organization (review), repository-wide custom instructions (hands-on), and personal (theory) |
| **Step 2** | Built path-specific custom instructions and used them to fix the kayaking activity |
| **Step 3** | Independently fixed the sightseeing activity using the same approach |
| **Step 4** | Created agent instructions (`AGENTS.md`) to onboard AI agents to the repo |
| **Step 5** | Created a reusable prompt file to automate new activity creation |
| **Step 6** | Designed your own prompt file for flights, accommodations, or packages |
| **Step 7** | Built a web-coder skill to improve JavaScript quality and security |
| **Step 8** | Created a skill that references prompt files to specialize activity creation |

### Key Takeaways

- **Custom instructions** eliminate repetitive guidance — set them once, benefit every time.
- **Three levels** let you tailor Copilot at the organization, repository, and personal scope.
- **Three types of repository instructions**: repository-wide (`copilot-instructions.md`), path-specific (`*.instructions.md`), and agent instructions (`AGENTS.md`).
- **Priority order**: Personal > Repository > Organization — personal preferences always win.
- **Path-specific custom instructions** (`*.instructions.md`) target only the files that need them using glob patterns.
- **Prompt files** (`*.prompt.md`) package multi-step workflows into reusable slash commands.
- **Skills** (`SKILL.md`) give Copilot deep domain expertise so it writes higher-quality, specialized code.
- **Agent Mode** can create the instruction files, prompt files, and skills themselves — let Copilot do the heavy lifting!

### What's Next?

- Explore the [Customization Library](https://docs.github.com/en/copilot/tutorials/customization-library) for more instruction examples
- Try creating instructions for your own projects
- Experiment with combining multiple instruction files for different areas of your codebase
- Share your prompt files with your team to standardize common workflows

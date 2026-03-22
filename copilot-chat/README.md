# Lab 01 — Copilot Chat

Explore **GitHub Copilot Chat** — your AI pair programmer that lives right inside the IDE. Ask it to explain code, fix bugs, write tests, and more.

## What You'll Learn

Today's goal will be to learn about GitHub Copilot Chat, the AI-powered UI that GitHub offers, and how to get the most out of the three different modes it provides:

- **Ask Mode** — Onboard to a project, explore code, and get answers
- **Agent Mode** — Let Copilot autonomously fix bugs, add features, and iterate on code
- **Plan Agent** — Design an implementation plan before writing any code

By the end of this lab you will have used all three modes to fix a bug, add new features, and write tests for a FastAPI web application.

## Step 1: Hello Copilot

Welcome to your **"Getting Started with GitHub Copilot"** exercise! :robot:

In this exercise, you will be using different GitHub Copilot features to work on a website that allows students of Mergington High School to sign up for extracurricular activities. 🎻 ⚽️ ♟️

### 📖 Theory: Getting to know GitHub Copilot

GitHub Copilot is an AI coding assistant that helps you write code faster and with less effort, allowing you to focus more energy on problem solving and collaboration.

GitHub Copilot has been proven to increase developer productivity and accelerate the pace of software development. For more information, see [Research: quantifying GitHub Copilot’s impact on developer productivity and happiness in the GitHub blog.](https://github.blog/news-insights/research/research-quantifying-github-copilots-impact-on-developer-productivity-and-happiness/)

As you work in your IDE, you'll most often interact with GitHub Copilot in the following ways:

| Interaction Mode          | 📝 Description                                                                                                                 | 🎯 Best For                                                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| **⚡ Inline suggestions** | AI-powered code suggestions that appear as you type, offering context-aware completions from single lines to entire functions. | Completion of the current line, sometimes a whole new block of code                                             |
| **💭 Inline Chat**        | Interactive chat scoped to your current file or selection. Ask questions about specific code blocks.                           | Code explanations, debugging specific functions, targeted improvements                                          |
| **💬 Ask Mode**           | Optimized for answering questions about your codebase, coding, and general technology concepts.                                | Understanding how code works, brainstorming ideas, asking questions                                             |
| **🤖 Agent Mode**         | Recommended default mode for most coding tasks: autonomous edits, tool use, and follow-through until the task is done.         | Daily coding tasks, from scoped fixes to larger multi-file implementation work                                   |
| **🧭 Plan Agent**         | Optimized for drafting a plan and asking clarifying questions before any code changes are made.                                | When you want a reviewed plan first, then hand off to implementation                                            |

As you work, you'll find GitHub Copilot can help out in several places across the `github.com` website and in your favorite coding environments such as VS Code, Jet Brains, and Xcode!

> [!TIP]
> You can learn more about current and upcoming features in the [GitHub Copilot Features](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features) documentation.

### :keyboard: Activity: Get a project intro from Copilot Chat

Let's start up our development environment, use copilot to learn a bit about the project, and then give it a test run.

1. Start by cloning this repository into your local machine.

2. If in Visual Studio Code, in the left sidebar, click the extensions tab and verify that the `GitHub Copilot` and `Python` extensions are installed and enabled.

1. At the top of VS Code, locate and click the **Toggle Chat icon** to open a Copilot Chat side panel.

   > 🪧 **Note:** If this is your first time using GitHub Copilot, you will need to accept the usage terms to continue.

1. Make sure you are in **Ask Mode** for our first interaction.

1. Enter the below prompt to ask Copilot to introduce you to the project.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Please briefly explain the structure of this project.
   > What should I do to run it?
   > ```

   Now add the src folder as a context and repeat the same question. 

   Also, you can use the #codespace, that will allow copilot to see the whole repo content and its codebase.

1. Now that we know a bit more about the project, let's actually try running it!

### :keyboard: Activity: Use Copilot to help remember a terminal command 🙋

Great work! Now that we are familiar with the app and we know it works, let's ask copilot for help starting a branch so we can do some customizing.

1. In VS Code's bottom panel, select the **Terminal** tab and on the right side click the plus `+` sign to create a new terminal window.

   > 🪧 **Note:** This will avoid stopping the existing debug session that is hosting our web application service.

1. Within the new terminal window use the keyboard shortcut `Ctrl + I` (windows) or `Cmd + I` (mac) to bring up **Copilot's Terminal Inline Chat**.

1. Let's ask Copilot to help us remember a command we have forgotten: creating a branch and publishing it.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hey copilot, how can I create and publish a new Git branch called "accelerate-with-copilot"?
   > ```

   > 💡 **Tip:** If Copilot doesn't give you quite what you want, you can always continue explaining what you need. Copilot will remember the conversation history for follow-up responses.

1. Press the `Run` button to let Copilot insert the terminal command for us. No need to copy and paste!

1. After a moment, look in the VS Code lower status bar, on the left, to see the active branch. It should now say `accelerate-with-copilot`. If so, you are all done with this step!

## Step 2: Getting work done with Copilot

In the previous step, GitHub Copilot was able to help us onboard to the project. That alone is a huge time saver, but now let's get some work done!

:bug: **THERE IS A BUG ON THE WEBSITE** :bug:

We’ve discovered that something’s off in the signup flow.
Students can currently register for the same activity **more than once**! Let’s see how far Copilot can take us in uncovering the cause and shaping a clean fix.

Before we dive in, a quick primer on how Copilot works. 🧑‍🚀

### 📖 Theory: How Copilot works

In short, you can think of Copilot like a very specialized coworker. To be effective with them, you need to provide them background (context) and clear direction (prompts). Additionally, different people are better at different things because of their unique experiences (models).

- **How do we provide context?:** In our coding environment, Copilot will automatically consider nearby code and open tabs. If you are using chat, you can also explicitly refer to files.

- **What model should we pick?:** For our exercise, it shouldn't matter too much. Experimenting with different models is part of the fun! That's another lesson! 🤖

- **How do I make prompts?:** Being explicit and clear helps Copilot do the best job. But unlike some traditional systems, you can always clarify your direction with followup prompts.

### :keyboard: Activity: Use Copilot to fix our registration bug :bug:

1. Let's ask Copilot to suggest where our bug might be coming from. Open the **Copilot Chat** panel in **Ask mode** and ask the following.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Students are able to register twice for an activity.
   > Where could this bug be coming from?
   > ```

1. Now that we know the issue is in the `src/app.py` file and the `signup_for_activity` method, let's follow Copilot's recommendation and go fix it (semi-manually). We'll start with a comment and let Copilot finish the correction.
   1. Open the `src/app.py` file.

      > 💡 **Tip:** If Copilot mentioned `src/app.py` in chat, you can click the file directly in the chat view to open it.

   1. Near the bottom of the file, find the `signup_for_activity` function.

   1. Find the comment line that describes adding a student. Above this is where it seems logical to do our registration check.

   1. Enter the below comment and press enter to go to the next line. After a moment, temporary shadow text will appear with a suggestion from Copilot! Nice! :tada:

      Comment:

      ```python
      # Validate student is not already signed up
      ```

   1. Press `Tab` to accept Copilot's suggestion and convert the shadow text to code.

   <details>
   <summary>Example Results</summary><br/>

   Copilot is growing every day and may not always produce the same results. If you are unhappy with the suggestions, here is an example of a valid suggestion result we produced during the making of this exercise. You can use it to continue forward.

   ```python
   @app.post("/activities/{activity_name}/signup")
   def signup_for_activity(activity_name: str, email: str):
      """Sign up a student for an activity"""
      # Validate activity exists
      if activity_name not in activities:
         raise HTTPException(status_code=404, detail="Activity not found")

      # Get the activity
      activity = activities[activity_name]

      # Validate student is not already signed up
      if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already signed up")

      # Add student
      activity["participants"].append(email)
      return {"message": f"Signed up {email} for {activity_name}"}
   ```

   </details>

### :keyboard: Activity: Let Copilot generate sample data 📋

In new project developments, it's often helpful to have some realistic looking fake data for testing. Copilot is excellent at this task, so let's add some more sample activities and introduce another way to interact with Copilot using **Inline Chat**

**Inline Chat** and the **Copilot Chat** panel are similar, but differ in scope: Copilot Chat handles broader, multi-file or exploratory questions; Inline Chat is faster when you want targeted help on the exact line or block in front of you.

1. Near the top of the `src/app.py` file (about line 23), find the `activities` variable, where our example extracurricular activities are configured.

1. Highlight the entire `activities` dictionary by clicking and dragging your mouse from the top to the bottom of the dictionary. This will help provide context to Copilot for our next prompt.

1. Bring up Copilot inline chat by using the keyboard command `Ctrl + I` (windows) or `Cmd + I` (mac).

   > 💡 **Tip:** Another way to bring up Copilot inline chat is: `right click` on any of the selected lines -> `Open Inline Chat`.

1. Enter the following prompt text and press enter or the **Send** button on the right.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Add 2 more sports related activities, 2 more artistic
   > activities, and 2 more intellectual activities.
   > ```

1. After a moment, Copilot will directly start making changes to the code. The changes will be stylized differently to make any additions and removals easy to identify. Take a moment to inspect and verify the changes, and then press the **Keep** button.

   <details>
   <summary>Example Results</summary><br/>

   Copilot is growing every day and may not always produce the same results. If you are unhappy with the suggestions, here is an example result we produced during the making of this exercise. You can use it to continue forward, if having trouble.

   ```python
   # In-memory activity database
   activities = {
      "Chess Club": {
         "description": "Learn strategies and compete in chess tournaments",
         "schedule": "Fridays, 3:30 PM - 5:00 PM",
         "max_participants": 12,
         "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
      },
      "Programming Class": {
         "description": "Learn programming fundamentals and build software projects",
         "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
         "max_participants": 20,
         "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
      },
      "Gym Class": {
         "description": "Physical education and sports activities",
         "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
         "max_participants": 30,
         "participants": ["john@mergington.edu", "olivia@mergington.edu"]
      },
      "Basketball Team": {
         "description": "Competitive basketball training and games",
         "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
         "max_participants": 15,
         "participants": []
      },
      "Swimming Club": {
         "description": "Swimming training and water sports",
         "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
         "max_participants": 20,
         "participants": []
      },
      "Art Studio": {
         "description": "Express creativity through painting and drawing",
         "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
         "max_participants": 15,
         "participants": []
      },
      "Drama Club": {
         "description": "Theater arts and performance training",
         "schedule": "Tuesdays, 4:00 PM - 6:00 PM",
         "max_participants": 25,
         "participants": []
      },
      "Debate Team": {
         "description": "Learn public speaking and argumentation skills",
         "schedule": "Thursdays, 3:30 PM - 5:00 PM",
         "max_participants": 16,
         "participants": []
      },
      "Science Club": {
         "description": "Hands-on experiments and scientific exploration",
         "schedule": "Fridays, 3:30 PM - 5:00 PM",
         "max_participants": 20,
         "participants": []
      }
   }
   ```

   </details>

1. You can now go to your website and verify that the new activities are visible.

### :keyboard: Activity: Use Copilot to describe our work 💬 (Optional)

Nice work fixing that bug and expanding the example activities! Now let's get our work committed and pushed to GitHub, again with the help of Copilot!

1. In the left sidebar, select the `Source Control` tab.

   > 💡 **Tip:** Opening a file from the source control area will show the differences to the original rather than simply opening it.

1. Find the `app.py` file and press the `+` sign to collect your changes together in the staging area.

1. Above the list of staged changes, find the **Message** text box, but **don't enter anything** for now.
   - Typically, you would write a short description of the changes here, but now we have Copilot to help out!

1. To the right of the **Message** text box, find and click the **Generate Commit Message** button (sparkles icon).

1. Press the **Commit** button and **Sync Changes** button to push your changes to GitHub.

1. Wait a moment for Mona to check your work, provide feedback, and share the next lesson.

## Step 3: Engage Hyperdrive - Copilot Agent Mode 🚀

### 📖 Theory: What is Copilot Agent Mode?

Copilot [agent mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode) is the next evolution in AI-assisted coding. Acting as an autonomous peer programmer, it performs multi-step coding tasks at your command.

Copilot Agent Mode responds to compile and lint errors, monitors terminal and test output, and auto-corrects in a loop until the task is completed.

#### Agent Mode (at a glance)

| Aspect | 👩‍🚀 Agent Mode |
| --- | --- |
| Autonomy and planning | Breaks down high-level requests into multi-step work and iterates until the task is complete. |
| Context gathering | Uses your current context and can discover additional relevant files when needed. |
| Tool use | Selects and invokes tools automatically; you can also direct tools with mentions like `#codebase`. |
| Approval and safety gates | Sensitive actions can require approval before execution, helping you stay in control. |

#### 🧰 Agent Mode Tools

Agent mode uses tools to accomplish specialized tasks while processing a user request. Examples of such tasks are:

- Finding relevant files to complete your prompt
- Fetching contents of a webpage
- Running tests or terminal commands

Now, let's give **Agent Mode** a try! 👩‍🚀

### :keyboard: Activity: Use Copilot to add a new feature! :rocket:

Our website lists activities, but it's keeping the guest list secret 🤫 

Let's use Copilot to change the website to display signed up students under each activity!

1. At the bottom of Copilot Chat window, use the dropdown to switch to **Agent** mode.

1. Open the files related to our webpage then drag each editor window (or file) to the chat panel, informing Copilot to use them as context.

   - `src/static/app.js`
   - `src/static/index.html`
   - `src/static/styles.css`

   > 🪧 **Note:** Adding files as context is optional. If you skip this, Copilot Agent Mode can still use tools like `#codebase` to search for relevant files from your prompt. Adding specific files helps point Copilot in the right direction, which is especially useful in larger codebases.

   > 💡 **Tip:** You can also use the **Add Context...** button to provide other sources of context items, like a GitHub issue or the results of a terminal window.

1. Ask Copilot to update our project to display the current participants of activities. Wait a moment for the edit suggestions to arrive and be applied.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Hey Copilot, can you please edit the activity cards to add a participants section.
   > It will show what participants that are already signed up for that activity as a bulleted list.
   > Remember to make it pretty!
   > ```

   After Copilot finishes work, you are in control of what changes get to stay. 

   Using the **Keep** buttons shown below, you can accept/discard all changes or review and decide change by change. This can be done either from the chat panel view or while inspecting each edited file.

1. Before we simply accept the changes, please check our website again and verify everything is updated as expected. 
   
   Here is an example of an updated activity card. You may need to restart the app or refresh the page.

   > 🪧 **Note:** Your activity card may look different. Copilot won't always produce the same results.

1. Now that we have confirmed our changes are good, use the panel to cycle through each suggested edit and press **Keep** to apply the change.

   > 💡 **Tip:** You can accept the changes directly, modify them, or provide additional instruction to refine them using the chat interface.

### :keyboard: Activity: Use Agent mode to add functional "unregister" buttons

Let's experiment with some more open-ended requests that will add more functionality to our web application.

If you don't get the desired results, you can try other models or provide follow-up feedback to refine the results.

1. Make sure your Copilot is still in **Agent** mode.

1. Click on the **Tools** icon and explore all Tools currently available to Copilot Agent Mode.

1. Time for our test! Let's ask Copilot to add functionality for removing participants.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > #codebase Please add a delete icon next to each participant and hide the bullet points.
   > When clicked, it will unregister that participant from the activity.
   > ```

   The `#codebase` tool is used by Copilot to find relevant files, code chunks that are relevant to the task at hand.

   > 🪧 **Note:** In this lab we explicitly include the `#codebase` tool to get the most repeatable results.
   > Feel free to try the prompt **without** `#codebase` and observe whether Agent Mode decides to gather broader project context on its own.

1. When Copilot is finished, inspect the code changes and the results on the website. If you like the results, press the **Keep** button. If not, try providing Copilot some feedback to refine the results.

   > 🪧 **Note:** If you don't see updates on the website, you may need to restart the code.

1. Ask Copilot to fix a registration bug.

   > 💡 **Tip:** We recommend testing the registration flow yourself so you can clearly see the before/after changes behavior.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > I've noticed there seems to be a bug.
   > When a participant is registered, the page must be refreshed to see the change on the activity.
   > ```

1. When Copilot is finished, inspect the results and validate the registration flow on the website.

   If you like the results, press the **Keep** button. If not, try providing Copilot some feedback.

## Step 4: Plan your implementation with the Planning Agent 🧭

In the last step, Agent Mode helped us move fast and ship new functionality. 🚀

Now let's slow down for one round and work like architects: define a strong testing approach first, then hand it off for implementation. This gives us better clarity, fewer surprises, and cleaner results. 🧪

### 📖 Theory: What is Copilot Plan Agent?

Copilot [Plan Agent](https://code.visualstudio.com/docs/copilot/agents/planning) helps you design a solution before any code is changed.

Instead of jumping straight into edits, it researches your request, asks clarifying questions, and drafts an implementation plan you can refine.

#### Plan Agent (at a glance)

| Aspect | 🧭 Plan Agent |
| --- | --- |
| Purpose | Creates a structured implementation plan before coding starts. |
| Context gathering | Uses read-only research to understand requirements and constraints. |
| Collaboration style | Asks clarifying questions, then updates the plan using your answers. |
| Iteration | Supports multiple refinement passes before implementation. |
| Safety | Does not edit files until you approve the plan and hand off to **Agent Mode**. |
| Handoff | **Start implementation** button hands off the approved plan to **Agent Mode** for coding. |

> [!TIP]
> You can start from a high-level request and then add constraints and details in follow-up prompts.

### ⌨️ Activity: Plan and implement backend tests

Your backend still has zero test coverage. Use **Plan Agent** to create a plan, answer questions, and then launch implementation.

1. Open the **Copilot Chat** panel and switch to **Plan Agent**.

1. Let's start with a broad prompt and Copilot will help us fill in the details:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > I want to add backend FastAPI tests in a separate tests directory.
   > ```

1. Wait for Copilot to generate its first plan. If it asks you any questions, answer them to the best of your ability. 

   > 🪧 **Note:** Don't worry about getting it perfect, you can always refine the plan later.

1. You can refine the plan and provide additional details in follow up prompts

   Here are some examples:

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Let's use the AAA (Arrange-Act-Assert) testing pattern to structure our tests
   > ```

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=social&logo=github%20copilot)
   >
   > ```prompt
   > Make sure we use `pytest` and add it to `requirements.txt` file
   > ```


1. Review the proposed plan and when you are happy with it, click **Start implementation** to hand off to **Agent Mode**.

   Notice that clicking the button switched from **Plan** to **Agent Mode**. From this point on, Copilot can edit your codebase, just like before.

1. Watch Copilot implement the plan you just created. It may ask for permissions to run certain tools (e.g., run commands or create virtual environments). Approve these permissions so it can continue working.

1. Review the changes and make sure tests run successfully. If needed, continue guiding until implementation is complete.

   **🎯 Goal: Get all tests passing (green) before you move on. ✅**

   > 🪧 **Note:** Agent Mode may complete this in one pass, or it may need follow-up prompts from you.

## Congratulations! 🎉

You've completed Lab 02! Here's a recap of what you learned:

- **Ask Mode** — Used Copilot Chat to onboard to a new project, understand its structure, and recall terminal commands
- **Inline Suggestions & Inline Chat** — Fixed a duplicate-registration bug with code completions and generated sample data using inline chat
- **Agent Mode** — Let Copilot autonomously add a participants display, unregister buttons, and fix a UI refresh bug across multiple files
- **Plan Agent** — Designed a testing strategy collaboratively before handing off implementation to Agent Mode

You're now equipped to use all three Copilot Chat modes in your daily workflow. Head over to the other labs in this repository to keep exploring!
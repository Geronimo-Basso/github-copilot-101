# Lab 5 — Advanced GitHub Copilot CLI: Orchestration and Real-World Workflows

Welcome back. In Lab 4 you got comfortable with the **basics** of GitHub Copilot CLI — a single session, a few prompts, the slash commands. This lab takes that foundation in two complementary directions.

| Phase | What you'll do | Why it matters |
|---|---|---|
| **Phase 1 — Squad orchestration** | Hire a small team of named agents (Researcher, Structurer, Developer, Lead) on top of Copilot CLI and have them produce a Slidev presentation end-to-end. | Shows what becomes possible when one CLI session isn't enough — when work needs a researcher, a structurer, and a reviewer talking to each other without losing context. |
| **Phase 2 — Full Copilot CLI walkthrough** | Use the **single** Copilot CLI session — `@` context, `/plan`, `/agent`, `/review`, headless `-p`, `/pr` — to add a real feature to the FastAPI app you already know from Lab 1. | Shows the everyday surface of Copilot CLI: the workflow you'll use most days, on a real codebase, from idea to PR. |

Both phases share the same CLI you already know. Phase 1 is about *adding* a coordination layer on top; Phase 2 is about getting the full value out of the CLI itself. You can run them in either order, but reading them in sequence makes the contrast clear: by the end you'll know when reaching for an orchestrated team beats a single session, and vice versa.

**Stack:** GitHub Copilot CLI · Squad · Slidev · Node.js 18+ · Python 3.10+

---

# Phase 1 — Squad orchestration

In this phase you'll take the same CLI you already know, add a thin orchestration layer on top of it called **[Squad](https://github.com/bradygaster/squad)** by Brady Gaster, and use a small team of named agents to research a topic, structure it, and produce a working **[Slidev](https://sli.dev/)** presentation. By the end of Phase 1 you will have a deck you can run locally and export to PDF, plus a feel for when orchestration earns its keep.

## What Phase 1 covers

We'll move from theory to practice in eight phases. The first and third are short, mostly conceptual — read them carefully, you'll lean on those ideas later. The rest are hands-on.

---

## 1. Why orchestration, and what we're using

Before we touch a terminal, let's agree on *why* we're adding a tool on top of Copilot CLI. A single CLI session is one assistant in one context window. That assistant carries everyone's hat at once: it researches, designs, writes code, and reviews. It works, but three things start to break as the task grows.

The first is **context bleed**. The longer the session runs, the more the assistant has to juggle, and the more likely it is to forget an early constraint or contradict an earlier decision. The second is **lack of parallelism**. Even when two pieces of work are independent — say, gathering research and scaffolding a project — a single session does them one after the other. The third is **memory loss across sessions**. Close the terminal and the next session starts cold.

Squad addresses all three by giving you a **team of named agents** that live as files in your repo. Each agent has its own narrow charter, its own private memory (`history.md`), and a shared decisions ledger that the whole team reads from. A *coordinator* sits on top, decides who does what, and runs them in parallel when it can. None of this replaces Copilot CLI — Squad runs on top of it, via `copilot --agent squad`.

### When orchestration helps — and when it gets in the way

Before we go further, let's be honest about the trade-offs. Orchestration is not a free upgrade; it's a different shape of work. Here's a side-by-side comparison so you know which mode a given task belongs in:

| Dimension | Single Copilot CLI session | Orchestrated team (Squad) |
|-----------|----------------------------|---------------------------|
| Setup cost | Open a terminal, type `copilot` | Install Squad, hire a team, write charters |
| Best at | Quick edits, one-off scripts, focused single-file changes | Multi-step deliverables that touch several concerns |
| Memory | Lasts as long as the session | Persistent, file-backed, survives across sessions |
| Parallelism | Sequential by nature | Multiple agents work in parallel via `mode: "background"` |
| Decision history | Lives in your scrollback (and is lost) | Captured in `.squad/decisions.md` and reviewable |
| Risk | Lower — you always see exactly what's happening | Higher — agents can run concurrently and produce more output than you can read in real time |
| Failure mode | Forgets earlier constraints, drifts in long sessions | Coordinator routes wrong agent, charters conflict, decisions ledger gets noisy |

A rough heuristic: if you can describe the task in one sentence and the deliverable is one file, use a single CLI session. If the task takes three sentences to describe and the deliverable spans multiple files or stages of work, orchestration starts to pay off. A presentation built from research is exactly the second case, which is why we picked it for this lab.

Avoid orchestration for: tiny refactors, throwaway scripts, anything where you'd waste more time describing the work to the team than just doing it. Don't use a forklift to move a chair.

---

### How the coordinator routes work

You'll spend the rest of this lab talking to the coordinator, so it helps to know the mental model. When you send a message, the coordinator does five things in order, very quickly:

1. **Captures directives.** If you said *"always cite primary sources"*, that's a rule the team should remember — it goes into the decisions ledger before any work runs.
2. **Picks the agent.** Did you name someone (*"{Researcher}, …"*)? They get the work. Did you say *"team"*? Multiple agents get spawned in parallel. Did you say nothing? The coordinator picks the best match from the routing table.
3. **Picks a response mode.** Direct (the coordinator answers you itself), Lightweight (one agent, minimal ceremony), Standard (one agent, full charter context), or Full (multi-agent fan-out with the Scribe logging behind them).
4. **Spawns the agent(s).** Each spawn includes the agent's full charter, their private history, and the team decisions ledger so they walk in with context.
5. **Collects results, then asks: does this unblock follow-up work?** If yes, more spawns happen automatically.

Two practical takeaways from this. First, **be specific about who you're talking to.** Naming an agent (*"{Lead}, …"*) bypasses the routing logic and is faster. Second, **directives are sticky.** Saying *"never use jargon in slide titles"* once will be applied to every subsequent slide the team writes — you don't need to repeat it.

---

## Slidev fits this model perfectly

Slidev decks are just **Markdown files with YAML front-matter**. No drag-and-drop editor, no binary format, no proprietary file. That makes them an ideal target for a code-generating team: the researcher writes notes, the structurer turns notes into an outline, the developer writes `slides.md`, and the lead reviews it — exactly the kind of pipeline orchestration is good at. You also get the side benefits of any Markdown-based tool: diffs are readable, code review works, and you can hand-edit anything the team produces.

### A deep dive on Slidev's customization surface

If your only experience with slide tools is PowerPoint or Keynote, you're about to be surprised by how much you can do with Slidev. The whole point of this lab is to get a polished deck out of the team — so it's worth knowing the surface area you can ask the agents to use. The rest of this section is a guided tour of what Slidev offers; don't try to memorize it, just skim so you know what to ask for in Phase 7.

#### Themes

A theme in Slidev is an npm package that ships typography, color palette, default layouts, and slide chrome. You activate one by setting `theme:` in the front-matter of `slides.md`.

When you start the dev server, Slidev detects that the theme isn't installed and offers to install it for you (`y` to accept). Some themes worth knowing:

| Theme | Best for | Notes |
|-------|----------|-------|
| `default` | Quick decks, generic content | Built into Slidev, no install required |
| `seriph` | Talks, academic content, anything that should feel "considered" | Elegant serif typography, subtle accents |
| `apple-basic` | Product-style decks, demos, design-led talks | Clean white space, large headings, Apple-keynote feel |
| `bricks` | High-energy decks, modern tech topics | Blocky color sections, bold contrast |
| `shibainu` | Casual, friendly decks | Hand-drawn feel, soft palette |
| `bricks-pixel` | Retro / playful decks | 8-bit pixel aesthetic |

The community gallery at <https://sli.dev/resources/theme-gallery> has dozens more. Theme packages follow the convention `slidev-theme-{name}` on npm, so any package matching that pattern is fair game — you can install one manually with `npm i slidev-theme-{name}` inside `deck/` and reference it in the front-matter.

**Switching themes mid-project** is one front-matter edit away. The team can do this for you:

> *"{Developer}, swap the deck from `seriph` to `apple-basic`. Install the theme package if it isn't already, and re-check that all slides still render — some themes don't ship every layout."*

That last caveat matters: themes can override which layouts exist, so a theme switch might break a slide that uses a layout the new theme doesn't define. Slidev will tell you in the dev server output which layout was missing.

For this lab we'll start with the `seriph` theme because it works out of the box and looks good immediately. You can swap it later — it's one front-matter line.

### The team we'll build

Here's the mapping we'll set up in Phase 4:

| Squad role | Job in this lab |
|------------|------------------|
| Lead | Decides deck structure and slide count, reviews drafts |
| Researcher | Gathers facts and citations on the chosen topic |
| Content Structurer | Turns research into a slide-by-slide outline |
| Slidev Developer | Writes `deck/slides.md` and runs the dev server |
| Scribe | Built-in. Records decisions and session history |

### Where you can actually run all of this: terminal or VS Code

One thing worth clearing up before we install anything: **Copilot CLI isn't only for the standalone terminal**. Once it's installed on your machine, you can drive it from a regular terminal *or* from inside VS Code, and Squad rides along either way. Pick whichever surface you're more comfortable in for this lab — the steps below work in both.

**Option A — Standalone terminal.** The classic flow: open Terminal/iTerm/Windows Terminal, `cd` into your working directory, and run `copilot`. This is what the rest of the lab assumes by default. Nothing special; the agent runs in whatever shell you launched.

**Option B — VS Code's integrated terminal.** Open the project folder in VS Code, then open the integrated terminal (`Ctrl+\`` / `Cmd+\``) and run `copilot` exactly the same way. VS Code also ships a dedicated **GitHub Copilot CLI** terminal profile and a Command Palette entry called **Chat: New Copilot CLI Session** that opens a Copilot-CLI terminal for you and reuses your VS Code GitHub authentication — no separate `/login` needed. Source: <https://code.visualstudio.com/docs/copilot/agents/copilot-cli>.

**Option C — VS Code Chat view as a background session.** From the Chat view, the **Session Target** dropdown lets you select **Copilot CLI** and run the agent as a background session managed by VS Code. These sessions run *outside* the VS Code process, so they keep going even if you close the window. This is overkill for what we're doing here, but worth knowing exists.

A few things are **shared** between VS Code Copilot Chat and Copilot CLI when both run in the same repo, which is what makes Squad portable:

- `.github/copilot-instructions.md` and any `.github/instructions/**/*.instructions.md` files
- Custom agents under `.github/agents/` (this is exactly how Squad ships its `squad.agent.md`)
- Agent Skills under `.github/skills/`

What's **not shared**: MCP server configuration. The CLI keeps its MCP config in `~/.copilot/mcp-config.json`; VS Code keeps its own in settings or `.vscode/mcp.json`. If you add an MCP server in one, you'll need to add it in the other.

This is also why Brady's Squad README tells VS Code users to *"open Copilot Chat and select the Squad agent"* and then send a kickoff message like:

> *"I'm starting a new project. Set up the team. Here's what I'm building: a recipe sharing app with React and Node."*

That works because `squad.agent.md` is a custom agent in `.github/agents/`, and VS Code picks it up automatically. In the standalone CLI, the equivalent is `copilot --agent squad --yolo`, which is what we'll run in Phase 4.

For the rest of this lab I'll write commands assuming a terminal prompt, but every prompt and CLI command is interchangeable with the VS Code integrated terminal. If you prefer to live in VS Code, do that — just make sure your terminal is Copilot CLI and not a plain shell.

That's all the theory you need to start. Onward.

---

## 2. Setting up the environment

Before installing anything, make sure you have the basics: Node.js 18+ (`node --version`), Git (`git --version`), an authenticated GitHub CLI (`gh auth status`), and a working GitHub Copilot CLI install. If Copilot CLI is new to you, the official setup guide is here: <https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli>.

Create an empty folder for this lab and open it in VS Code (`mkdir squad-slidev-lab && cd squad-slidev-lab && code .`) so you can inspect files as the agents create them. Keeping the editor open alongside the terminal is a habit worth building for the rest of the lab — the whole point of Squad is that its state is *files you can read*, and reading them is how you build trust in what the agents are doing.

### 2.1 Let Copilot CLI find the install commands for you

This is a small but important habit: when you don't know the exact install command for a tool, ask Copilot CLI before you go searching docs. Start a CLI session in this folder:

```bash
copilot
```

Then prompt:

> *"Find the official install commands for the Squad CLI by Brady Gaster (npm package `@bradygaster/squad-cli`) and for Slidev. Show me the exact commands."*

Read what it gives you, then exit the session. The commands below are what we expect — use them as the source of truth if your CLI gives you something different.

### 2.2 Install Squad

```bash
npm install -g @bradygaster/squad-cli
squad init
```

`squad init` is idempotent and safe to re-run. It scaffolds a `.squad/` folder and drops `squad.agent.md` next to it. Switch over to VS Code now and have a look at `.squad/team.md` — it will be mostly empty, but you should see the file exists.

### 2.3 Install Slidev

Slidev ships as a project scaffold rather than a global CLI, so we install it into a subfolder. Naming the folder `deck` keeps the agents' working area separate from Squad's state.

```bash
npm create slidev@latest
```

When the scaffolder asks for a folder name, type `deck`. Accept the defaults for everything else.

Now confirm Slidev runs:

```bash
cd deck
npm install
npm run dev
```

The dev server prints a local URL (default `http://localhost:3030`). Open it in a browser, click through the example slides so you know what "good" looks like, then stop the server with `Ctrl+C` and return to the project root with `cd ..`.

You're set up. Don't move on until both `squad init` and `npm run dev` worked — the rest of the lab assumes both.

---

## 3. Squad's commands and what they're for

You won't use most of Squad's 17 commands today. The full list lives in the [Squad README](https://github.com/bradygaster/squad#all-commands-17-commands), and it's worth skimming once. For this lab, four commands matter:

| Command | Purpose |
|---------|---------|
| `squad init` | Scaffolds `.squad/` (already done) |
| `squad status` | Confirms which squad is active |
| `squad doctor` | Diagnoses setup issues before you start work |
| `copilot --agent squad --yolo` | Launches a Copilot CLI session driven by the Squad coordinator |

Run a quick health check now:

```bash
squad status
squad doctor
```

If `doctor` flags anything, fix it before continuing — debugging the team is much harder than debugging the install.

There are four concepts worth carrying into Phase 4. Read these slowly.

**Coordinator vs agents.** The coordinator is what you actually talk to when you run `copilot --agent squad`. It never writes code itself — its job is to route your requests to the right agent and assemble their replies. The agents do the work in their own contexts.

**Charters and history.** Every agent has a `charter.md` (its identity and boundaries) and a `history.md` (its private memory). Both live under `.squad/agents/{name}/`. You'll inspect both in Phase 4.

**Decisions ledger.** `.squad/decisions.md` is the team's shared brain. Anything that affects more than one agent — scope, architecture, formatting rules — gets recorded here. All agents read it before starting work.

**Casting.** Squad picks character names from a single fictional universe per project. The names are persistent identifiers; they aren't role-play. Don't expect "Ripley" to talk like Ripley — the name just makes the team easier to remember.

---

## 4. Hiring the agent team

Now we wire the team up. This is where Squad earns its keep.

### 4.1 Launch the coordinator

```bash
copilot --agent squad --yolo
```

`--yolo` runs without per-tool approval prompts so the coordinator can scaffold files in one pass; drop it if you'd rather approve each action manually. The first time you run this in a fresh `.squad/` directory, the coordinator goes into *Init Mode*. It will ask what you're building before proposing names — that context is what drives the casting choice.

### 4.2 Describe the project and propose the team

Send the coordinator this message:

> *"I'm building a Slidev presentation generator. The team should be able to research a technical topic, structure a deck, and write `slides.md` for Slidev. Propose a team of 4 plus Scribe."*

The coordinator will reply with a proposed roster — roles plus cast names — and ask you to confirm. Read the proposal carefully against the table from Phase 1:

| Role | Responsibility |
|------|----------------|
| Lead | Owns deck structure, slide count, and review gates |
| Researcher | Gathers facts, quotes, and links |
| Content Structurer | Converts research into a slide-by-slide outline |
| Slidev Developer | Writes `deck/slides.md` and runs the dev server |
| Scribe | Built-in. Records decisions and session history |

If the proposal matches, reply **yes**. If it doesn't, tell the coordinator what to change ("swap the QA role for a Content Structurer") and re-confirm. Don't accept a roster you'd have to fight against later.

### 4.3 Inspect the generated agent definitions in VS Code

Once the team is hired, the coordinator will have scaffolded a full `.squad/` directory in your project. This is what was just created:

```
.squad/
├── team.md              # Roster — who's on the team
├── routing.md           # Routing — who handles what
├── decisions.md         # Shared brain — team decisions
├── ceremonies.md        # Sprint ceremonies config
├── casting/
│   ├── policy.json      # Casting configuration
│   ├── registry.json    # Persistent name registry
│   └── history.json     # Universe usage history
├── agents/
│   ├── {name}/
│   │   ├── charter.md   # Identity, expertise, voice
│   │   └── history.md   # What they know about YOUR project
│   └── scribe/
│       └── charter.md   # Silent memory manager
├── skills/              # Compressed learnings from work
├── identity/
│   ├── now.md           # Current team focus
│   └── wisdom.md        # Reusable patterns
└── log/                 # Session history (searchable archive)
```

Take a moment to appreciate that this is **all plain Markdown and JSON in your repo** — no hidden state, no external service. Everything the team "knows" lives in files you can read, edit, and version-control. That's the whole point of Squad: agent state is data, not magic.

Now read what the agents actually are, rather than just trusting the summary the coordinator gave you. Switch to VS Code and open these files one by one:

- `.squad/team.md` — confirm every member appears under the `## Members` heading.
- `.squad/agents/<lead-name>/charter.md` — read the role, scope, and boundaries.
- `.squad/agents/<researcher-name>/charter.md` — same.
- `.squad/agents/<lead-name>/history.md` — should be seeded with the project description and your name.
- `.squad/decisions.md` — likely empty; that's fine.

Two things to look for in each charter: does the **role description** match what you asked for, and are the **input/output boundaries** sensible (e.g., the Researcher writes to `.squad/research/`, the Developer writes to `deck/`)?

If anything is off, do **not** hand-edit the file. Charters are owned by the coordinator. Go back to the CLI and ask: *"Update {Name}'s charter so they also handle X."* The coordinator will rewrite it cleanly and update related files.

### 4.4 What a good charter looks like

To make the previous step concrete, here's a sketch of what one of the charters should roughly contain. Your generated file won't match word-for-word — Squad's coordinator phrases things in its own voice and adapts to the project — but the *shape* should be similar across every agent. If yours is missing entire sections, that's a signal to ask the coordinator to expand it.

**Researcher charter (sketch)**

```markdown
# {Researcher Name} — Researcher

## Role
Gathers, verifies, and synthesises factual material for the team.
Does not write slide content; produces source briefs others build from.

## Expertise
- Primary and secondary source evaluation
- Citation discipline (always links, always dated)
- Domain scan: identifying what's missing as much as what's present

## Inputs
- Topic prompts from the human
- Follow-up questions from {Lead} or {Structurer}

## Outputs
- `.squad/research/<topic>.md` — long-form brief with citations
- `.squad/research/<topic>-summary.md` — short keynote-ready distillation

## Voice
Neutral, source-cited, willing to flag uncertainty.
Never asserts a claim without a link or a "source needed" marker.

## Boundaries
- Does NOT write `deck/` files
- Does NOT make structural decisions about the presentation
- Escalates contested facts to the human, not to other agents
- MUST end every reply with `Saved to: <path>` on its own line so the human can copy the path
```

Two patterns to notice, and to look for in every other charter the coordinator generated. First, every agent has explicit **boundaries** — what they will *not* do. This is what stops the team from collapsing into a single voice. Second, every output is a **file path or a CLI message**, not a vague "deliverable". Agents that produce concrete artifacts are easy to review; agents that produce "advice" are not.

If a generated charter doesn't include both of those, ask the coordinator to add them. A team without boundaries drifts; a team without concrete outputs is hard to audit.

---

## 5. Picking a topic and researching it

With the team in place, we can start the actual work. Pick one of these topics — both have plenty of public material and benefit from comparison:

- **Comparison of main coding agent tools** (GitHub Copilot, Cursor, Claude Code, Cline, etc.)
- **Introduction to Microsoft AI Foundry**

Address the Researcher by name (replace `{Researcher}` with your researcher's cast name from Phase 4):

> *"{Researcher}, research the topic 'Comparison of main coding agent tools'. Produce a brief covering: market context, the top 4–5 tools, one paragraph each on capabilities, pricing model, IDE/CLI integration, and licensing. Cite sources with URLs. Tell me the exact path where you saved it."*

We deliberately don't pin the file path. Squad's Researcher decides where research artifacts live — typically somewhere under `<research-dir>/<topic-slug>.md` (often inside `.squad/research/` or a sibling folder), but the exact location depends on how the coordinator and your Researcher's charter were generated. **Watch the terminal when the agent finishes — it will print the path it wrote to.** That printed path is your source of truth for the rest of this phase; copy it somewhere handy.

Once you have the path, **switch to VS Code and open the file the agent created**. Read it the way you'd read a junior teammate's first draft — looking for thin sections, missing citations, claims that feel out of date.

If you find gaps, send a focused follow-up rather than rewriting it yourself:

> *"{Researcher}, the pricing section is too shallow. Expand it with current per-seat numbers for each tool and add at least two primary sources."*

Iterate until the brief is good enough to build a deck on top of. This file is the foundation for everything that comes next, so don't move on with weak material.

### 5.1 Distill the brief into keynote-ready material

The brief from the previous step is a research document — it's dense, source-cited, and not shaped for slides. Before you hand anything to the Structurer, you need a second, much shorter artifact: the **most important points the audience should walk away with**, written in slide-friendly language.

This is a separate task and worth a separate prompt. Don't skip it. If you go straight from the long brief to "build the deck", the Structurer will pick its own highlights and you'll lose control of the narrative.

Ask the Researcher to summarize their own work. Reference the brief by the path the agent printed earlier (shown below as `<brief-path>`), and let the agent decide where to drop the summary:

> *"{Researcher}, read your brief at `<brief-path>` and produce a keynote summary alongside it. Constraints: maximum 8 takeaways, each one sentence (≤20 words), audience is engineers who haven't used these tools. Add a 'Why it matters' line under each takeaway in plain language. End with the single most surprising insight from the research. Print the path you saved it to."*

Again, watch the terminal for the path — call it `<summary-path>` from here on. Open that file in VS Code when it lands. This is what the deck will actually be built from, so apply real editorial judgment: cut anything weak, reorder so the strongest points come first, and ask for one more pass if any takeaway feels generic. The shorter and sharper this file is, the better the deck will be.

Keep both `<brief-path>` and `<summary-path>` written down — Phase 6 references them when you set the format brief for the deck.

---

## 6. Defining the format before generating anything

Here is the most important habit in the whole lab: **decide the format before the agents generate anything**. Fixing a 12-slide deck after the fact is much more expensive than fixing a 12-slide outline.

Send this to the coordinator. Adjust the numbers if you like, but keep the rules concrete and binding:

> *"Team, here are the rules for the deck. Treat them as binding.*
> *1. Length: 12 slides total.*
> *2. Source material: build the deck from `<summary-path>` (the keynote summary the Researcher produced in Phase 5). The full brief at `<brief-path>` is supporting context only.*
> *3. Slide 1: `layout: cover` with title, author, one-line tagline.*
> *4. Slide 2: agenda (3–5 bullets).*
> *5. Slides 3–10: one concept per slide, max 6 bullets, max 12 words per bullet. Use `layout: two-cols` or `layout: image-right` where it adds clarity.*
> *6. Slide 11: comparison table.*
> *7. Slide 12: `layout: end` with takeaways and links.*
> *8. Front-matter: `theme: seriph`, `transition: slide-left`. Speaker notes under every slide using `<!-- ... -->`.*
> *9. No walls of text. If a slide needs more, split it.*
> *10. All output goes to `deck/slides.md`.*
> *Have {Structurer} produce the outline first, then {Lead} reviews it, then {Developer} writes the markdown."*

> **Theme swap:** if you'd rather try a different look, replace `theme: seriph` with `apple-basic`, `bricks`, or any theme from the [Slidev theme gallery](https://sli.dev/resources/theme-gallery). Slidev will offer to install the package on first run — accept the prompt. If it doesn't (e.g., a non-interactive run), install it manually with `npm install -D @slidev/theme-{name}` from inside `deck/`.

The coordinator will run the Structurer first. When the outline comes back, **open `.squad/decisions.md` in VS Code** to see what got recorded as binding rules, and read the Structurer's outline in the CLI response. This is your last cheap chance to reject something off-spec — take it. If the outline is wrong, fix it now with one more prompt. Don't let the Developer write code from a bad outline.

---

## 7. Generating the deck and iterating

Once you're happy with the outline, ask the Developer to write the deck:

> *"{Developer}, write `deck/slides.md` from the approved outline. Follow every rule from the format brief. When done, list every slide title so I can scan."*

While that runs, hop over to VS Code and watch `deck/slides.md` appear. When it's done, run the deck in a separate terminal so you can see what's actually been built:

```bash
cd deck
npm run dev
```

Open the URL Slidev prints, walk through every slide, and compare what you see against the rules from Phase 6. Slidev hot-reloads, so leave the dev server running for the rest of this phase.

Now iterate. Each iteration is one prompt — keep them surgical:

- *"Slide 5 has 9 bullets — cap at 6 and move the rest to a new slide."*
- *"Add speaker notes under each slide using Slidev's `<!-- ... -->` syntax."*
- *"Replace the bullet list on slide 8 with a Mermaid diagram."*
- *"{Lead}, review the current `deck/slides.md` against the format brief and list every violation."*

A useful rhythm: route small edits to the Developer, route structural rework to the Lead. The Lead's job is to enforce the format brief, and you'll find they catch things you missed.

### Common iteration patterns

After running this lab a few times, you'll notice the same complaints come up over and over. Here are the three most common, with the prompt shape that fixes them. Treat these as templates — fill in the slide numbers and specifics for your deck.

**Pattern 1 — "The deck is too dense."** The Developer wrote what you asked for, but every slide reads like a paragraph. Audiences zone out on dense slides. Fix it by raising the format constraints and asking for a structural pass:

> *"{Lead}, the deck is too dense. Apply these stricter rules and have {Developer} rewrite affected slides:*
> *1. No more than 5 bullets per slide.*
> *2. No bullet over 10 words.*
> *3. Any slide that violates either rule must be split into two.*
> *4. Use `layout: two-cols` where the content is genuinely a comparison.*
> *Report the new slide count when done."*

The slide count will go up. That's correct — better one idea per slide than three crammed together.

**Pattern 2 — "The structure is off."** The slides individually look fine but the deck doesn't tell a story. The agenda doesn't match the body, the conclusion doesn't follow from the middle, or the strongest point is buried at slide 9. Fix it by going back to the outline, not the slides:

> *"{Structurer}, the deck has a narrative problem. Read `deck/slides.md` and `<summary-path>`, then propose a re-ordering. The strongest takeaway should be in the first third of the deck. The agenda on slide 2 must match the actual section order. Output the new order as a numbered list of slide titles before any slides change."*

Approve the new order in the CLI before you let anyone touch `slides.md`. Re-ordering after the fact is cheap; rewriting after a bad re-order is expensive.

**Pattern 3 — "The tone is wrong."** Every slide is technically correct but the deck sounds like a Wikipedia article — or worse, a marketing brochure. Tone is set in the format brief, so go back there:

> *"{Lead}, the deck's tone is too {formal/casual/promotional/dry}. Apply these tone rules and have {Developer} rewrite headings and bullets accordingly:*
> *1. Use active voice. No passive constructions.*
> *2. No marketing adjectives ("powerful", "seamless", "cutting-edge").*
> *3. Slide titles state a finding, not a topic ("X is twice as fast as Y", not "Performance comparison").*
> *4. Body text avoids jargon unless the term has been defined on a prior slide.*
> *Don't change layouts or content order — only wording."*

Constraining the change ("only wording") is important. Without it, the team will helpfully restructure things you didn't ask them to touch.

**Pattern 4 — "Two agents disagree."** This will happen. The Lead says the deck is too long; the Developer says cutting more would lose key points. The right move is to make the disagreement explicit and let the team resolve it with a decision in the ledger:

> *"{Lead} and {Developer} disagree on whether to cut slides 8–10. Lead's position: deck must be ≤12 slides. Developer's position: those three slides each carry a unique point. Resolve this. The output of this discussion should be a single line in `.squad/decisions.md` stating the rule we'll apply for the rest of the project."*

This is genuinely the moment orchestration earns its keep. A single CLI session would have made the call without telling you; an orchestrated team makes the disagreement visible and persists the resolution for next time.

### When to stop iterating

Stop when the deck satisfies your format brief. There is always one more thing you could improve — at some point the cost outweighs the benefit. A useful gut check: if the next iteration takes longer to describe than the change is worth, you're done. Ship it.

---

## 8. Bringing in images and finishing the deck

A bullet-only deck is a tired deck. Let's add visuals and ship the result.

Slidev serves anything in `deck/public/` at the deck root, so dropping files there is enough. Copy 2–3 PNG, JPG, or SVG files into `deck/public/` (use your file manager, or just drag them into the VS Code Explorer). Confirm the files are there before moving on.

Now hand the integration to the Developer. Be explicit about which images exist — agents can't see your filesystem unless you tell them what's in it:

> *"{Developer}, the following images are now in `deck/public/`: {list filenames}. Place them on the most relevant slides using Slidev's image syntax (e.g., `layout: image-right` with `image: /file.png` in the slide front-matter, or `background: /file.png` on a `cover` layout). Use the `cover` layout on slide 1 with the largest image as the background. Keep all existing content."*

The dev server should hot-reload. Walk through the deck again and check the images render where they should.

Finally, run a closing review:

> *"{Lead}, do a final review of `deck/slides.md`. Check rule compliance, image placement, broken links, and typos. Report findings as a numbered list, then have {Developer} fix everything in one pass."*

Once the Lead signs off, ship the deck. Rather than memorising Slidev's CLI flags, just ask Copilot to do it for you in the same terminal:

> *"Export `deck/slides.md` to PDF using Slidev. If the audience needs PowerPoint, also produce a `.pptx`. Run the commands and tell me where the output landed."*

Copilot CLI knows the Slidev export commands and will run them, install any missing Playwright browsers (~300MB Chromium download on first run — if your environment blocks that, ask for `.pptx` only), and report the output paths. That's it — you have an editable Markdown source, a runnable HTML deck, and a shippable file, all from one orchestrated team.

---

# Phase 2 — Full Copilot CLI walkthrough on a real codebase

Phase 1 showed what becomes possible when you put a coordinator on top of Copilot CLI and let a named team handle the work. That's the right tool when you genuinely have multiple roles to coordinate. Most of the time, though, you don't — you have a feature to build and one CLI session to build it in. Phase 2 is about getting full value out of that single session.

We'll work on a copy of the **Mergington High School activities sign-up app** from Lab 1, already pre-copied for you at [`mergington-app/`](./mergington-app/). It's a small FastAPI backend plus a vanilla JS frontend that lets students browse and sign up for extracurricular activities. We're going to add a real feature to it — **a waitlist for activities that are full** — using the full surface of Copilot CLI: `@` mentions for context, `/plan` for design, a custom `/agent` for review, `/review` for self-checks, headless `-p` for one-shot scripts, and `/pr` to ship the result.

If you skipped Lab 4, please do that one first. Phase 2 assumes you can install the CLI, start a session, use `@` mentions, run `/plan`, manage permission flags, and invoke headless mode (`copilot -p`). We won't reintroduce those — we'll *combine* them into a real workflow. You'll also reuse the `fastapi-reviewer` custom agent from Lab 4 (lives at `~/.copilot/agents/fastapi-reviewer.agent.md` — CLI custom agents are user-level only). If you skipped Lab 4's "Custom agents" exercise, jump back and do it now; the walkthrough below uses it in Steps 3 and 6.

Before you start, get the app running so you have a baseline:

```bash
cd mergington-app
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn backend.app:app --reload
```

Confirm `http://127.0.0.1:8000` renders the activities page, then `Ctrl-C` to stop. Open `mergington-app/` in VS Code (`code .`) and keep it open the whole time so you can watch files change as Copilot edits them. From here on, every command runs inside `mergington-app/`.

## What Phase 2 covers

| # | Step | Mode |
|---|------|------|
| 1 | Walkthrough — building the waitlist feature end-to-end | Hands-on |
| 2 | Iteration patterns specific to single-CLI work | Reference |

This phase exercises two Copilot CLI features Lab 4 didn't cover hands-on: `/agent` (switching personas mid-session) and `/review` (reviewing the current diff). For everything else — install, auth, `@` mentions, `/plan`, permission flags, headless `-p` — we lean on what you learned in Lab 4.

---

## Phase 2.1 — Walkthrough: building the waitlist feature end-to-end

This is the spine of Phase 2. We'll build a real feature — *students can join a waitlist when an activity is full, and get auto-promoted when a spot frees up* — in one CLI session, following the loop **describe → plan → context → implement → test → review → ship**, without leaving the terminal except to peek at files in VS Code.

Open a CLI session at `mergington-app/` if you haven't already (`copilot`). Keep VS Code open in a second pane so you can read every file Copilot writes.

### Step 1 — Gather context

Before asking Copilot to do anything, give it the codebase. Use `@` mentions to load the relevant directories (Lab 4 Exercise B):

```
> @backend/ @frontend/ Take a look at this project. In one paragraph,
> what does the app do, and what's the data model for activities?
```

Read its summary. If it gets the data model wrong (e.g., calls activities a list when they're a dict), correct it now in plain language — it's much cheaper to fix the model's understanding here than after a bad implementation.

### Step 2 — Plan the feature

Now ask for a plan, not code:

```
> /plan Add a waitlist feature so that when an activity is full, students
> can join a waitlist instead of being rejected. When a registered student
> drops out, the next person on the waitlist is automatically promoted.
> Surface the waitlist position in the API response and in the frontend.
```

Read the proposal in full before responding. If anything is wrong or missing, push back: *"You forgot the frontend needs to show the waitlist position when signup returns 'waitlisted'. Add that to the plan."* Iterate until the plan reflects what you want.

### Step 3 — Get an expert lens with the custom agent

Now switch to the custom agent for a design review of the plan:

```
> /agent
```

Pick `fastapi-reviewer`. Then:

```
> Review the plan above. From a FastAPI correctness and idiomatic-usage
> perspective, what's missing? Specifically: HTTP status codes, response
> models, error handling for "activity not found" and "already registered".
```

The agent will respond through the lens its charter defines — pointing at status codes, suggesting Pydantic response models, flagging missing error paths. Apply its suggestions to the plan with one more prompt: *"Update the plan to incorporate those suggestions."*

When you're happy, switch back to the default agent (`/agent` → default) for implementation.

### Step 4 — Implement

Hand the approved plan to Copilot:

```
> Implement the plan. Modify backend/app.py and add any new files needed.
> Don't change frontend/ yet — we'll do that after the API is in place.
```

Copilot will propose tool calls — file reads, file edits — and ask for permission as it goes. Approve them as they come. **Watch the diff in VS Code.** If you see Copilot editing a file you didn't expect, deny the edit and ask it why.

When the API changes are in, ask it to run a smoke check:

```
> Start uvicorn in the background and curl the new endpoint with a sample
> payload to confirm it responds correctly. If it errors, show me the trace.
```

Then move on to the frontend:

```
> Now update frontend/app.js and frontend/index.html to display the
> waitlist position when signup returns waitlisted status.
```

### Step 5 — Generate tests

Tests are not optional. Ask for them explicitly:

```
> @backend/app.py Generate pytest tests for the waitlist behaviour.
> Cover: signup when activity has space, signup when activity is full
> (goes to waitlist), drop a registered student (next waitlisted is
> promoted), drop a waitlisted student (others move up one position),
> and signup for a non-existent activity.
```

In a second terminal, install pytest if it isn't already there and run them:

```bash
pip install pytest httpx
pytest
```

If tests fail, paste the failure into the CLI:

```
> Tests failed with this output:
> {paste}
> Fix the implementation, not the tests.
```

The "fix the implementation, not the tests" qualifier is important — without it, Copilot will sometimes make tests pass by weakening the assertion rather than fixing the bug.

### Step 6 — Self-review

Once tests are green, run a review pass on the whole change:

```
> /review
```

Copilot reviews the current diff. Read the output. Common findings: missing input validation, error responses that leak internal state, magic numbers that should be constants. Address them with targeted prompts (*"address finding #2 only"*).

Then run one more pass through the custom agent for a domain-specific lens:

```
> /agent
```

→ `fastapi-reviewer` →

```
> Review the final diff for FastAPI correctness, idiomatic usage, and
> testability. Skip anything already covered by /review.
```

Once `/review` and `fastapi-reviewer` both come back clean, the feature itself is done. Commit, push, and open the pull request through your usual workflow.

---

## Phase 2.2 — Iteration patterns for single-CLI work

Phase 1 had an "iteration patterns" section for orchestrated work. Single-CLI work has its own characteristic failure modes. Here are the most common, with the fix prompt to use.

| Failure mode | What you see | One-line fix prompt |
|---|---|---|
| **Hallucinated endpoint or function** | Copilot writes code that calls `app.delete_activity()` — which doesn't exist in your codebase. | *"You called `delete_activity` but that function doesn't exist. Show me the exact line in `@backend/app.py` where it's defined, or rewrite using only functions that exist."* |
| **Scope creep** | You asked for a waitlist endpoint; Copilot also reformatted three unrelated files. | *"Revert the changes to files I didn't ask you to touch. Only modify files directly required for the waitlist feature."* |
| **Lost thread after `/clear`** | You cleared context to free tokens and now Copilot has forgotten the plan. | Re-load context: *"`@backend/app.py @frontend/app.js` We were adding a waitlist feature. Re-read the plan from earlier — here it is: {paste plan}. Continue from step N."* |
| **Tests "fixed" by weakening assertions** | A failing test is now passing, but you don't trust why. | *"Show the diff between the old and new test. If you changed an assertion, justify it. If you can't, revert the test change and fix the implementation instead."* |
| **Plan was never followed** | Copilot implemented something different from `/plan`. | *"Compare the implementation to the original plan. List every divergence and justify each one. Revert any divergence that wasn't justified."* |
| **Endless permission prompts** | Each tool call requires a separate approval. | Use `/allow` for the current session to allowlist a tool you trust (e.g., `read_file`), or pass `--allow-tool {name}` when launching. |

The pattern across all of these is the same: **be specific, point at evidence, and ask for justification.** Copilot is good at responding to constraints — give it some.

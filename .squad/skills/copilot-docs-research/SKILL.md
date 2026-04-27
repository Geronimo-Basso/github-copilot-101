# Skill: Research Copilot Features Against Official Docs

**Category:** Content Verification  
**Applies to:** Lab authoring, Q&A writing, feature explanation  
**Owner:** Book (Copilot Expert)

## When to Use This Skill

Before writing content that explains Copilot behavior, features, or capabilities — especially when:
- Answering user questions about Copilot CLI, VS Code Copilot Chat, or other Copilot surfaces
- Adding Q&A sections to labs
- Verifying feature claims in existing content
- Distinguishing between similar features (e.g., modes, slash commands, tools)

## Pattern

1. **Identify authoritative sources** based on the Copilot surface:
   - **CLI:** `https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli`, `https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli`, local `copilot --help`
   - **VS Code:** `https://code.visualstudio.com/docs/copilot/*` (agents, customization, reference pages)
   - **GitHub.com:** `https://docs.github.com/en/copilot/*`
   - **Cross-surface:** GitHub blog posts, release notes, changelog

2. **Fetch and read** the relevant doc pages using `web_fetch` or `web_search`

3. **Cross-check claims:**
   - Does the official doc support what you're about to write?
   - Are there deprecated features you need to avoid?
   - Is terminology current? (e.g., "Edit mode" → "Plan mode", "REPL" → "interactive mode")

4. **Verify behavior** if possible:
   - Run local CLI commands (`copilot --help`, `echo "/help" | copilot`)
   - Test in VS Code if accessible
   - Check version numbers and preview/stable status

5. **Cite sources** in the final content — URL + anchor link

6. **Be honest about ambiguity:**
   - If docs are unclear or contradictory, say so rather than guessing
   - Flag gaps to Geronimo or the team

## Example Applications

### Lab 4 Q&A (Plan mode vs `/plan` command)
- **Sources checked:** GitHub docs (CLI concepts, CLI usage), local CLI help
- **Key findings:** Plan mode = persistent state (Shift+Tab toggle), `/plan` = one-off slash command
- **Citations added:** Two doc URLs at bottom of Q&A entry

### Lab 3 Agent Mode inventory (2026-04-20)
- **Sources checked:** 7+ code.visualstudio.com pages
- **Key corrections:** "Edit → Plan" rename is wrong (Edit deprecated, Plan is distinct agent), custom agent paths changed
- **Output:** `.squad/decisions/inbox/book-agent-mode-inventory.md`

## Anti-Patterns

❌ **Don't write from memory** — Copilot features change frequently; your training data may be outdated  
❌ **Don't guess** — if the docs don't cover it, say "not documented" rather than inventing behavior  
❌ **Don't cite unofficial sources** — Stack Overflow, Reddit, or blog posts are context only; official docs are the citation  
❌ **Don't skip version checks** — a feature may be preview-only, experimental, or require a flag

## Related Skills

- `lab-exercise-structure` — once you've verified facts, structure them per lab conventions
- `custom-agent-frontmatter-format` — when writing agent-related content, ensure frontmatter accuracy

## Success Criteria

Content you write:
- ✅ Matches current official docs
- ✅ Cites sources (URLs)
- ✅ Uses current terminology
- ✅ Flags preview/experimental status
- ✅ Acknowledges gaps rather than guessing

## Owner Notes (Book)

From charter: "When uncertain, fetch official docs. Never guess about Copilot behavior — learners trust this."

This skill formalizes the "fetch first, write second" discipline. It's the difference between reference-grade content and best-effort guessing.

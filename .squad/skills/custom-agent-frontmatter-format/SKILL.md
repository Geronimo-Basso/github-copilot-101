---
name: "custom-agent-frontmatter-format"
description: "YAML frontmatter format required for GitHub Copilot custom agent files"
domain: "github-copilot, custom-agents, yaml, configuration"
confidence: "high"
source: "official — GitHub's custom-agents documentation + Lab 3 implementation"
---

## Context

GitHub Copilot custom agent files (`.agent.md`) require **YAML frontmatter** at the top of the file. The frontmatter defines the agent's metadata, and the body below contains the system prompt/instructions.

The `name` field in frontmatter is **required** — omitting it causes the agent to fail silently (not appear in the agent picker). This was discovered during Lab 3 Exercise C initial drafting.

## Format

### Required Structure

```markdown
---
name: kebab-case-agent-name
description: One-sentence specialized purpose
tools: ['read', 'search', 'edit']
---

Your system prompt content goes here.
Tell the agent what to do, how to behave, etc.
```

### Field Reference

| Field | Required? | Type | Description | Example |
|-------|-----------|------|-------------|---------|
| `name` | **YES** | string | Kebab-case identifier for the agent. Must be unique. | `test-author`, `code-quality-reviewer` |
| `description` | Recommended | string | One-sentence summary shown in agent picker. | `Writes unit tests for existing Python code` |
| `tools` | Optional | array of strings | Whitelisted tool names the agent can use. Omit for default toolset. | `['read', 'search', 'edit']` |
| `model` | Optional | string | Model override (e.g., `gpt-5`, `claude-sonnet-4`). Defaults to user's selected model. | `gpt-5` |

### Tool Whitelisting

The `tools` field restricts what the agent can do:

```yaml
tools: ['read', 'search']  # Agent can ONLY read files and search — no edits
```

Common tools:
- `read` — read files
- `search` — search codebase
- `edit` — edit files
- `create` — create new files
- `delete` — delete files
- `run` — run shell commands
- `web_search` — search the web

Omitting `tools` gives the agent the default toolset (typically read/search/edit).

## Examples

### Example 1: Read-Only Code Reviewer (Lab 3 Exercise C.2)

```markdown
---
name: code-quality-reviewer
description: Reviews Python code for quality issues (read-only, no edits)
tools: ['read', 'search']
---

You are a code quality reviewer specializing in Python.

Your role:
- Read code and identify bugs, security issues, or maintainability problems
- Provide actionable feedback
- **NEVER edit code** — your job is to review, not fix

Focus areas:
- Security vulnerabilities (SQL injection, XSS, etc.)
- Error handling gaps
- Performance anti-patterns
- PEP 8 compliance
```

**Why the `tools` restriction?** Forces the agent to only review, not auto-fix. Students learn that tool whitelisting enforces least-privilege.

### Example 2: Test Author with Scope Constraint (Lab 3 Exercise C.3)

```markdown
---
name: test-author
description: Writes unit tests for existing Python code
tools: ['read', 'search', 'edit', 'create', 'run']
model: gpt-5
---

You are a test-writing specialist for Python applications.

Your role:
- Read existing code and write corresponding unit tests using pytest
- Create test files in `agents/tests/` directory
- Run tests to verify they pass
- Use clear, descriptive test names following the pattern `test_<function>_<scenario>`

**Scope constraint:** You ONLY work in the `agents/tests/` directory. Do NOT modify application code in `agents/backend/` or `agents/mcp_servers/`.

Test structure:
```python
def test_endpoint_returns_200_when_valid_input():
    # Arrange: set up test data
    # Act: call the function/endpoint
    # Assert: verify expected outcome
```

Always include:
- Happy path tests (expected inputs)
- Error path tests (invalid inputs, edge cases)
- Docstrings explaining what each test verifies
```

**Why `model: gpt-5`?** Pins the model for consistency. Students learn that agents can have different capabilities based on model selection.

### Example 3: Endpoint Scaffolder with Handoff Pattern (Lab 3 Exercise C.1)

```markdown
---
name: endpoint-scaffolder
description: Scaffolds new FastAPI endpoints and delegates testing to test-author agent
tools: ['read', 'search', 'edit', 'create']
---

You are an API endpoint scaffolding specialist for the FastAPI application in `agents/backend/`.

Your role:
- Create new FastAPI endpoints based on user requests
- Follow existing patterns in `agents/backend/app.py`
- Use proper type hints (Pydantic models)
- Handle errors gracefully (try/except, HTTP status codes)
- Add docstrings to every endpoint

**Handoff pattern:**
After scaffolding an endpoint, tell the user:
> "Endpoint created. To add tests, invoke the `test-author` agent with: 'Write tests for the new `<endpoint-name>` endpoint.'"

**Do NOT write tests yourself** — that's the test-author agent's job.
```

**Why the handoff?** Demonstrates separation of concerns and multi-agent workflows. Lab 3 Exercise C teaches this as one of three custom-agent patterns.

## Anti-Patterns

### ❌ Missing `name` Field

```markdown
---
description: Writes unit tests
tools: ['read', 'edit']
---

...system prompt...
```

**Result:** Agent doesn't appear in the picker. Silent failure.

### ❌ Using Spaces or Special Characters in `name`

```markdown
---
name: test author  # ❌ spaces
---
```

**Fix:** Use kebab-case: `test-author`

### ❌ Forgetting the Closing `---`

```markdown
---
name: test-author
description: Writes tests

System prompt goes here...
```

**Result:** The entire file is parsed as frontmatter, and the system prompt is empty.

**Fix:** Always close frontmatter with `---` before the body.

### ❌ Inconsistent YAML Syntax

```markdown
---
name: test-author
tools: read, search, edit  # ❌ Not an array
---
```

**Fix:** Use proper YAML array syntax: `['read', 'search', 'edit']` or:
```yaml
tools:
  - read
  - search
  - edit
```

## Verification

After creating a custom agent file:

1. **Save the file** in `.github/agents/your-agent-name.agent.md`
2. **Reload VS Code** (or wait ~5 seconds for hot reload)
3. **Open Copilot Chat** and click the agent picker (top-left, says "General")
4. **Check the list** — your agent should appear with its `name` and `description`
5. **Invoke it** — type `@your-agent-name` in chat

If the agent doesn't appear:
- Check for YAML syntax errors (run `yamllint` or paste into a YAML validator)
- Verify the `name` field is present and kebab-case
- Check file location (must be in `.github/agents/`, not `.github/agent/` or `agents/`)
- Restart VS Code if hot reload didn't trigger

## Related Skills

- **Lab Exercise Structure** (`.squad/skills/lab-exercise-structure/`) — how to teach custom agents in a lab context
- **Python Package Shadow** (`.squad/skills/python-package-shadow/`) — unrelated but similar "required format" gotcha

## References

- [GitHub Custom Agents Documentation](https://docs.github.com/en/copilot/customizing-copilot/creating-custom-agents) (official)
- Lab 3 Exercise C (`agents/README.md` lines 300-450) — three working examples
- Lab 3 Exercise E.2 (`agents/README.md` lines 750-770) — plugin packaging example reusing `test-author.agent.md`

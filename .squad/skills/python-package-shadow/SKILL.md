---
name: "python-package-shadow"
description: "Avoid naming local Python packages the same as PyPI dependencies to prevent module shadowing"
domain: "python, packaging, dependencies"
confidence: "high"
source: "earned — discovered via Lab 3 Exercise D bug (agents/mcp/ shadowing mcp PyPI package)"
---

## Context

Python's import system searches for modules in a specific order defined by `sys.path`. By default, the **current working directory (CWD)** is **first** in `sys.path` when Python is run as a script. This means:

```python
# Running from /repo/agents/
import mcp  # Python finds /repo/agents/mcp/ FIRST, not site-packages/mcp/
```

If a local directory shares the same name as an installed PyPI package, the **local directory shadows the installed package**. Imports that expect the installed package's submodules (e.g., `mcp.server.fastmcp`) fail with `ModuleNotFoundError` because the local directory doesn't contain those submodules.

**Crucially:** The shadowing is **context-dependent**. Running from a different directory (e.g., the repo root) may work fine because CWD changes, and the local directory is no longer in the import path.

## Patterns

### 1. Avoid Name Collisions with PyPI Packages

When creating a local Python package (directory with `__init__.py`), **never** name it the same as a PyPI dependency you import:

```
❌ BAD:
agents/
  mcp/               # Shadows the installed `mcp` package
    __init__.py
    activities_server.py
  requirements.txt   # Contains: mcp[cli]==1.27.0

✅ GOOD:
agents/
  mcp_servers/       # Descriptive, no collision
    __init__.py
    activities_server.py
  requirements.txt   # Contains: mcp[cli]==1.27.0
```

### 2. Descriptive Package Names

Use suffixes or qualifiers that clarify the local package's purpose:
- `mcp_servers/` (not `mcp/`) — contains MCP server implementations
- `fastapi_app/` (not `fastapi/`) — contains FastAPI application code
- `pytest_fixtures/` (not `pytest/`) — contains custom pytest fixtures

### 3. Test from Multiple Directories

When developing, test imports from **different working directories** to catch shadowing:

```bash
# Test from repo root
python -c "import mcp.server.fastmcp; print('ok')"

# Test from subdirectory where local package lives
cd agents
python -c "import mcp.server.fastmcp; print('ok')"
```

If the second test fails but the first succeeds, you likely have a shadowing issue.

### 4. Use `python -m` with Fully Qualified Paths

When running modules, use `-m` with the **full package path** from the repo root, and ensure CWD is the repo root:

```bash
# ✅ Run from repo root — no ambiguity
python -m agents.mcp_servers.activities_server

# ❌ Running from agents/ subdirectory can introduce shadowing
cd agents
python -m agents.mcp_servers.activities_server  # Still works because `-m` searches sys.path
python -c "import mcp"  # ❌ Finds local mcp/ instead of installed package
```

### 5. Check Dependencies in `requirements.txt`

Before naming a local package, **grep your `requirements.txt`** (or `pyproject.toml`, `Pipfile`, etc.):

```bash
grep -i "^mcp" requirements.txt  # Check if 'mcp' is already a dependency
```

If found, choose a different name for your local package.

## Examples

### Real-World Case: Lab 3 Exercise D

**Before (broken):**
```
agents/
  mcp/
    __init__.py
    activities_server.py
  requirements.txt  # mcp[cli]==1.27.0

# From agents/:
python -c "from mcp.server.fastmcp import FastMCP"
# ❌ ModuleNotFoundError: No module named 'mcp.server'
```

**After (fixed):**
```
agents/
  mcp_servers/
    __init__.py
    activities_server.py
  requirements.txt  # mcp[cli]==1.27.0

# From agents/:
python -c "from mcp.server.fastmcp import FastMCP"
# ✅ Works — no more shadowing
```

### Common Collisions to Avoid

| ❌ Avoid naming local packages | ✅ Use instead |
|-------------------------------|----------------|
| `mcp/` | `mcp_servers/`, `mcp_tools/` |
| `fastapi/` | `fastapi_app/`, `api/` |
| `pytest/` | `pytest_fixtures/`, `test_helpers/` |
| `requests/` | `http_client/`, `api_client/` |
| `flask/` | `flask_app/`, `web/` |
| `django/` | `django_project/`, `app/` |

## Anti-Patterns

### ❌ Assuming Imports Work Because Tests Pass in CI

CI often runs from the repo root, where shadowing doesn't occur. Users running commands from subdirectories will hit the bug:

```bash
# CI (works):
cd /repo && pytest agents/tests/  # ✅ CWD is /repo, no shadowing

# User (breaks):
cd /repo/agents && pytest tests/  # ❌ CWD is /repo/agents, shadowing occurs
```

**Fix:** Test locally from multiple directories, or enforce CWD in your test runner.

### ❌ Relying on Virtualenv Location to Prevent Shadowing

Moving the virtualenv (e.g., from `agents/.venv` to `.venv`) changes import order but **doesn't eliminate the root cause**. The local package still shadows the installed one when CWD is the wrong directory.

**Fix:** Rename the local package to avoid the collision entirely.

### ❌ Adding `.` to `.gitignore` to Hide the Problem

Ignoring the local package doesn't prevent it from shadowing imports at runtime.

**Fix:** Rename the package. Use `.gitignore` only for files that should truly be ignored (build artifacts, caches, secrets).

### ❌ Using `sys.path.insert(0, ...)` as a Workaround

Manually manipulating `sys.path` is brittle and hard to maintain:

```python
import sys
sys.path.insert(0, '/path/to/site-packages')  # ❌ Fragile
import mcp.server.fastmcp
```

**Fix:** Eliminate the name collision at the source — rename the local package.

## Detection

### Symptoms of Module Shadowing

1. **Import works from repo root, fails from subdirectory:**
   ```bash
   cd /repo && python -c "import pkg.submodule"  # ✅
   cd /repo/agents && python -c "import pkg.submodule"  # ❌
   ```

2. **Error message:**
   ```
   ModuleNotFoundError: No module named 'pkg.submodule'
   ```
   (when you **know** the package is installed)

3. **`sys.path` inspection shows CWD first:**
   ```python
   import sys
   print(sys.path[0])  # Often '' or '.' (current directory)
   ```

### Diagnostic Command

To see which module Python resolves:

```bash
python -c "import pkg; print(pkg.__file__)"
# Expected: /path/to/.venv/lib/python3.x/site-packages/pkg/__init__.py
# If shadowed: /path/to/repo/agents/pkg/__init__.py
```

If the path points to your **local directory** instead of `site-packages`, you have shadowing.

## Related Skills

- **Virtual Environment Management:** `.venv` location and activation patterns
- **Python Import System:** How `sys.path` is constructed and searched
- **Module Naming Conventions:** PEP 8 package naming guidelines (lowercase, underscores)

## References

- [PEP 328 — Absolute/Relative Imports](https://peps.python.org/pep-0328/)
- [Python Import System Documentation](https://docs.python.org/3/reference/import.html)
- Lab 3 Exercise D fix commit: `ed8808b` (2026-04-21)

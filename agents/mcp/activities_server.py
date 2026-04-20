"""Mergington activities MCP server — exposes the in-memory activities dict
to MCP-aware clients (e.g. GitHub Copilot Agent Mode)."""

from mcp.server.fastmcp import FastMCP
from agents.backend.app import activities

mcp = FastMCP("mergington-activities")


@mcp.tool()
def list_activities() -> list[str]:
    """Return the names of all extracurricular activities."""
    return list(activities.keys())


@mcp.tool()
def get_signups_count(activity: str) -> int:
    """Return the number of students signed up for a given activity.

    Raises ValueError if the activity is unknown.
    """
    if activity not in activities:
        raise ValueError(f"Unknown activity: {activity!r}")
    return len(activities[activity]["participants"])


if __name__ == "__main__":
    mcp.run()

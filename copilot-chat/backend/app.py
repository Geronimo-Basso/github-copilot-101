"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

import json
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory (frontend)
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(current_dir.parent,
          "frontend")), name="static")

# Load activities from JSON file at startup
activities_json_path = current_dir / "data" / "activities.json"
try:
    with open(activities_json_path, "r", encoding="utf-8") as f:
        activities = json.load(f)
except FileNotFoundError:
    raise RuntimeError(f"Activities data file not found: {activities_json_path}")
except json.JSONDecodeError as e:
    raise RuntimeError(f"Invalid JSON in activities data file: {e}")


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}

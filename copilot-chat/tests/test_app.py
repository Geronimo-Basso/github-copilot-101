"""Tests for the High School Management System API"""

import pytest
from fastapi.testclient import TestClient
from backend.app import app, activities


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities to their original state before each test"""
    original = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"],
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"],
        },
    }
    activities.clear()
    activities.update(original)
    yield


@pytest.fixture
def client():
    return TestClient(app)


def test_signup_success(client):
    """Test successful signup for an activity"""
    response = client.post(
        "/activities/Chess Club/signup?email=newstudent@mergington.edu"
    )
    assert response.status_code == 200
    assert "newstudent@mergington.edu" in activities["Chess Club"]["participants"]


def test_signup_duplicate_email_returns_409(client):
    """Test that signing up with a duplicate email returns HTTP 409"""
    response = client.post(
        "/activities/Chess Club/signup?email=michael@mergington.edu"
    )
    assert response.status_code == 409
    assert "already registered" in response.json()["detail"]


def test_signup_duplicate_email_does_not_add_participant(client):
    """Test that a duplicate signup does not add the email again"""
    original_count = len(activities["Chess Club"]["participants"])
    client.post("/activities/Chess Club/signup?email=michael@mergington.edu")
    assert len(activities["Chess Club"]["participants"]) == original_count


def test_signup_same_email_different_activities(client):
    """Test that the same email can register for different activities"""
    response1 = client.post(
        "/activities/Chess Club/signup?email=newstudent@mergington.edu"
    )
    response2 = client.post(
        "/activities/Gym Class/signup?email=newstudent@mergington.edu"
    )
    assert response1.status_code == 200
    assert response2.status_code == 200


def test_signup_nonexistent_activity(client):
    """Test that signing up for a nonexistent activity returns 404"""
    response = client.post(
        "/activities/Nonexistent/signup?email=student@mergington.edu"
    )
    assert response.status_code == 404

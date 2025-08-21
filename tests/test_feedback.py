import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_valid_feedback_submission(client):
    payload = {
        "rating": 5,
        "improvementText": "Great service!",
        "interestedInResearch": True,
        "email": "test@example.com"
    }
    response = client.post("/api/feedback", json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "Feedback received successfully"
    assert data["data"]["rating"] == 5


def test_invalid_rating(client):
    payload = {
        "rating": 6,
        "improvementText": "Too high",
        "interestedInResearch": False
    }
    response = client.post("/api/feedback", json=payload)
    assert response.status_code == 400


def test_missing_opinion(client):
    payload = {
        "rating": 3,
        "interestedInResearch": False
    }
    response = client.post("/api/feedback", json=payload)
    assert response.status_code == 201  
    data = response.get_json()
    assert data["message"] == "Feedback received successfully"


def test_research_opt_in_without_email(client):
    payload = {
        "rating": 4,
        "improvementText": "Looks good",
        "interestedInResearch": True
        # Missing email
    }
    response = client.post("/api/feedback", json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert "Valid email is required" in data["error"]

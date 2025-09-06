import pytest
from app import create_app, db

@pytest.fixture
def client():
    """Create and configure a new app instance for each test."""
    # Create the app with a specific test configuration
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
    })

    with app.app_context():
        db.create_all()
        yield app.test_client()  # The test client is yielded
        db.session.remove()
        db.drop_all()


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
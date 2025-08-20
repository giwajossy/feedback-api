import re
from flask import jsonify

def is_valid_email(email: str) -> bool:
    """Check if an email has a valid format."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def validate_feedback(data: dict):
    """Validate feedback input data. Returns (error_response, None) if invalid, (None, data) if valid."""
    # Validate rating
    rating = data.get("rating")
    if rating is None:
        return jsonify({"status": "error", "error": "Rating is required"}), None
    if not isinstance(rating, int) or not (1 <= rating <= 5):
        return jsonify({"status": "error", "error": "Rating must be an integer between 1 and 5"}), None

    # Validate opinion length
    opinion = data.get("opinion")
    if opinion and len(opinion) > 500:
        return jsonify({"status": "error", "error": "Opinion cannot exceed 500 characters"}), None

    # Validate research + email
    research = data.get("research", False)
    if research:
        email = data.get("email")
        if not email or not is_valid_email(email):
            return jsonify({"status": "error", "error": "Valid email is required if research opt-in is true"}), None

    return None, data

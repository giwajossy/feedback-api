from flask import Flask, request, jsonify
import re

# Initialize Flask app
app = Flask(__name__)

# In-memery storage for feedback
feedback_store = []

def is_valid_email(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None


@app.route("/api/feedback", methods=["POST"])
def submit_feedback():
    data = request.get_json() or {}

    # Validate rating
    rating = data.get("rating")
    if rating is None:
        return jsonify({"status": "error", "error": "Rating is required"}), 400
    if not isinstance(rating, int) or not (1 <= rating <= 5):
        return jsonify({"status": "error", "error": "Rating must be an integer between 1 and 5"}), 400

    # Validate opinion length
    opinion = data.get("opinion")
    if opinion and len(opinion) > 500:
        return jsonify({"status": "error", "error": "Opinion cannot exceed 500 characters"}), 400

    # Validate research opt-in logic
    research = data.get("research", False)
    if research:
        email = data.get("email")
        if not email or not is_valid_email(email):
            return jsonify({"status": "error", "error": "Valid email is required if research opt-in is true"}), 400


    feedback_store.append(data)

    return jsonify({
        "message": "Feedback received successfully",
        "data": data
    }), 201


@app.route("/")
def home():
    """Health check endpoint to verify server is running."""
    return jsonify({"message": "Feedback API is live!"}), 200

if __name__ == "__main__":
    # Run app in development mode
    app.run(debug=True)

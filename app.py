from flask import Flask, request, jsonify
from flask_cors import CORS
from validators import validate_feedback

# Initialize Flask app
app = Flask(__name__)


CORS(app)

# In-memery storage for feedback
feedback_store = []

def is_valid_email(email: str) -> bool:
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None


@app.route("/api/feedback", methods=["POST"])
def submit_feedback():
    data = request.get_json() or {}

   # Run validation
    error, validated_data = validate_feedback(data)
    if error:
        return error, 400

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

from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# In-memery storage for feedback
feedback_store = []

@app.route("/api/feedback", methods=["POST"])
def submit_feedback():
    """Handle user feedback submission."""
    data = request.get_json()

    # For now, no validation
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

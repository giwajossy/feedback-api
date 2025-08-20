from flask import Flask, jsonify

# Initialize Flask app
app = Flask(__name__)

@app.route("/")
def home():
    """Health check endpoint to verify server is running."""
    return jsonify({"message": "Feedback API is live!"}), 200

if __name__ == "__main__":
    # Run app in development mode
    app.run(debug=True)

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from flasgger import Swagger, swag_from
from middleware.request_logger import setup_request_logger
from validators import validate_feedback
from swagger_docs.swagger_config import template
from models import db, Feedback

def create_app(config_overrides=None):
    """Application factory."""
    app = Flask(__name__)

    # Default configuration
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Apply overrides
    if config_overrides:
        app.config.update(config_overrides)
    else:
        # Production/development configuration
        database_url = os.getenv('DATABASE_URL')
        if not database_url:
            raise RuntimeError("DATABASE_URL is not set in the environment.")
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
\
    CORS(app)
    Swagger(app, template=template)
    db.init_app(app)

    # Create tables if they don't exist
    with app.app_context():
        db.create_all()

    setup_request_logger(app)

    @app.route("/api/feedback", methods=["POST"])
    @swag_from("swagger_docs/feedback_swagger.yml")
    def submit_feedback():
        data = request.get_json() or {}

        # Run validation
        error, validated_data = validate_feedback(data)
        if error:
            return error, 400

        # Create feedback entry
        new_feedback = Feedback(
            rating=validated_data.get('rating'),
            improvementText=validated_data.get('improvementText'),
            interestedInResearch=validated_data.get('interestedInResearch', False),
            email=validated_data.get('email')
        )

        db.session.add(new_feedback)
        db.session.commit()

        return jsonify({
            "message": "Feedback received successfully",
            "data": validated_data
        }), 201


    @app.route("/")
    @swag_from("swagger_docs/health_check_swagger.yml")
    def home():
        return jsonify({"message": "Feedback API is live!"}), 200

    return app

if __name__ == "__main__":
    # For development, create and run the app
    app = create_app()
    app.run(debug=True)

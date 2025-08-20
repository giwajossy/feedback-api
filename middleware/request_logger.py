import time
from flask import request

def setup_request_logger(app):
    """Attach logging middleware to the Flask app."""

    @app.before_request
    def start_timer():
        request.start_time = time.time()

    @app.after_request
    def log_request(response):
        duration = round(time.time() - request.start_time, 4)
        method = request.method
        path = request.path
        status = response.status_code

        app.logger.info(
            f"{method} {path} | Status: {status} | Duration: {duration}s"
        )

        return response

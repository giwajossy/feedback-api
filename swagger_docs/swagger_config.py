
template = {
    "swagger": "2.0",
    "info": {
        "title": "Feedback API",
        "description": "A RESTful API for collecting user feedback.",
        "version": "1.0.0"
    },
    "definitions": {
        "Feedback": {
            "type": "object",
            "properties": {
                "rating": {
                    "type": "integer",
                    "description": "Rating from 1 to 5"
                },
                "opinion": {
                    "type": "string",
                    "description": "User's opinion"
                },
                "research": {
                    "type": "boolean",
                    "description": "Opt-in for research"
                },
                "email": {
                    "type": "string",
                    "description": "User's email (required if research is true)"
                }
            }
        },
        "Error": {
            "type": "object",
            "properties": {
                "message": {
                    "type": "string"
                }
            }
        }
    }
}

# Feedback API

User feedback mechanism

[API Documentation](https://feedback-api-wobm.onrender.com/apidocs/)
![Swagger Document](https://res.cloudinary.com/dd3hmuucq/image/upload/v1755731224/samples/swagger_-_feedback_api_mjblby.png)

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Development Environment](#development-environment)
- [Testing](#testing)
- [Note](#note)

## Overview
This project implements a simple feedback collection API. It is lightweight, demonstrates core backend development principles including API design, data validation, modularization, and persistent storage with PostgreSQL.


## Tech Stack
- **Python 3**
- **Flask**
- **PostgreSQL**
- **Flask-SQLAlchemy**
- **Docker** 
- **Gunicorn**
- **Flasgger**

## Features
- **Feedback Submission**: Collects feedback including rating, opinion, and optional contact info.
- **Data Validation**: Ensures feedback data adheres to predefined rules.
- **Persistent Storage**: Uses PostgreSQL to persist feedback.
- **Containerized**: Fully containerized with Docker for consistent development and deployment.

## Development Environment [docker]
**Prerequisites:** 
Docker Desktop installed and running.

**Instructions:** 

1.  Clone the repository. 
2.  Navigate to the project directory.
3.  Run the following command:
```bash
docker compose up --build
```
The API will be available at `http://localhost:8000`


## Testing
To run the tests, execute the following command in your terminal:
```bash
pytest -v
```

## Note
This API is currently deployed on Render's free tier service, which means the server sleeps after moments of inactivity. However, I will ensure to nudge the server using [Choque CLI](https://github.com/giwajossy/choque-cli); an open source tool I built to keep servers awake - with support for configurable intervals, persistent logging, and summary reporting. 
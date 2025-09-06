# Feedback API

User feedback mechanism

[API Documentation](https://feedback-api-wobm.onrender.com/apidocs/)
![Swagger Document](https://res.cloudinary.com/dd3hmuucq/image/upload/v1755731224/samples/swagger_-_feedback_api_mjblby.png)

## Table of Contents
- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [API Endpoints](#api-endpoints)
- [Run Locally](#run-locally)
- [Testing](#testing)
- [Note](#note)

## Overview
This project implements a simple feedback collection API. It is lightweight, demonstrates core backend development principles including API design, data validation, modularization, and persistent storage with PostgreSQL.


## Tech Stack
- **Python 3**
- **Flask**
- **PostgreSQL**
- **Flask-SQLAlchemy**
- **Gunicorn**
- **Flasgger**

## Features
- **Feedback Submission**: Collects feedback including rating, opinion, and optional contact info.
- **Data Validation**: Ensures feedback data adheres to predefined rules.
- **Persistent Storage**: Uses PostgreSQL to persist feedback.
- **Modular API Design**: Separation of concerns with dedicated modules for validation, request logging, and Swagger documentation.
- **Health Check Endpoint**: A basic endpoint to verify API availability.

## API Endpoints

### `POST /api/feedback`
Submits new user feedback.

### `GET /`
Health check endpoint to confirm the API is live.

## Run Locally

#### Prerequisites
- Python 3 
- PostgreSQL service running 

#### 1. Clone repo & setup virtual environment
```bash
git clone https://github.com/giwajossy/feedback-api.git
cd feedback-api
python3 -m venv venv
source venv/bin/activate
```

#### 2. Install dependencies
```bash
pip install -r requirements.txt
```
#### 3. Create and setup the database
```bash
 # [Optional] Create a database named 'feedback_db'
 createdb feedback_db

 # Set the database URL environment variable for the current session 
 export DATABASE_URL='postgresql+psycopg://localhost/feedback_db'
```


#### 4. Run the server (development)
```bash
# The database table will be created automatically on startup
flask run
```

The access root route via `http://127.0.0.1:5000`

## Testing
To run the tests, execute the following command in your terminal:
```bash
pytest -v
```

## Note
This API is currently deployed on Render's free tier service, which means the server sleeps after moments of inactivity. However, I will ensure to nudge the server using [Choque CLI](https://github.com/giwajossy/choque-cli); an open source tool I built to keep servers awake - with support for configurable intervals, persistent logging, and summary reporting. 
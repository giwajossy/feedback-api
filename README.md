# Feedback API

User feedback mechanism built using **Python** and **Flask**.

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
This project implements a simple feedback collection API. It's designed to be lightweight and easily deployable, demonstrating core backend development principles including API design, data validation, and modularization.


## Tech Stack
- **Python 3**
- **Flask**
- **Gunicorn**
- **Flasgger**

## Features
- **Feedback Submission**: Allows users to submit feedback including rating, opinion, and optional contact information.
- **Data Validation**: Ensures incoming feedback data adheres to predefined rules.
- **Modular API Design**: Separation of concerns with dedicated modules for validation, request logging, and Swagger documentation.
- **In-memory Storage**: Simple in-memory storage for submitted feedback [can be easily extended to a persistent database].
- **Health Check Endpoint**: A basic endpoint to verify API availability.

## API Endpoints

### `POST /api/feedback`
Submits new user feedback.

### `GET /`
Health check endpoint to confirm the API is live.

## Run Locally

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

#### 3. Run the server (development)
```bash
python app.py
```

The access root route via `http://127.0.0.1:5000`

## Testing
To run the tests, execute the following command in your terminal:
```bash
pytest -v
```

## Note
This API is currently deployed on Render's free tier service, which means the server sleeps after moments of inactivity. However, I will ensure to nudge the server using [Choque CLI](https://github.com/giwajossy/choque-cli); an open source tool I built to keep servers awake - with support for configurable intervals, persistent logging, and summary reporting. 
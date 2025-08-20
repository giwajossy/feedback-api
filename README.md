# Feedback API

User feedback mechanism built using **Python** and **Flask**

### Tech Stack

- Python 3
- Flask (backend framework)
- Gunicorn (WSGI server for deployment)


### Getting Started

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

Visit http://127.0.0.1:5000 → you should see:

 ```json
 {"message": "Feedback API is live!"}
 ```

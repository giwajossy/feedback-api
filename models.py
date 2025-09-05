from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    improvementText = db.Column(db.String(500), nullable=True)
    interestedInResearch = db.Column(db.Boolean, default=False)
    email = db.Column(db.String(120), nullable=True)

    def __repr__(self):
        return f'<Feedback {self.id}>'

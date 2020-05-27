from database import db

class Adress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Adress = db.Column(db.String(255), nullable=False, unique=True)
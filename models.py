from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.Integer, unique=True,nullable=False)
    password = db.Column(db.String,nullable=False)


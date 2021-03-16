from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models import db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///pops.sqlite"
db.init_app(app)
db.create_all()

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/about_us")
def about():
    return render_template("about_us.html")



if __name__ == '__main__':
    app.run()

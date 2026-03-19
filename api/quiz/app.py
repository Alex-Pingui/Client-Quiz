import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

def mkpath(p):
    return os.path.normpath(
        os.path.join(os.path.dirname(__file__), p)
    )

app=Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+mkpath("../db/quiz.db")
app.config["SQLALCHEMY_ECHO"]=True

db=SQLAlchemy(app)
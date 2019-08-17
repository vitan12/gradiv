from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/bestdb"
mongo1 = PyMongo(app, uri="mongodb://localhost:27017/bestdb")

mongo = PyMongo(app)

from gradivflask import routes
from mongodb import crud_operations

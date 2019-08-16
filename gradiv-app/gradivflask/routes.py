from flask import render_template
from gradivflask import app
from flask_pymongo import PyMongo

@app.route('/')
@app.route('/index')
def index():
    mongo1 = PyMongo(app, uri="mongodb://localhost:27017/bestdb")
    mongo_test = mongo1.db.testCol.find_one({"hello": "world"})
    return render_template('index.html', test=mongo_test)

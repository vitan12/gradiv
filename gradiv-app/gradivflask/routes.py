from flask import render_template, request
from gradivflask import app
from flask_pymongo import PyMongo
from datetime import time
from mongodb import parsing

mongo1 = PyMongo(app, uri="mongodb://localhost:27017/gradb")

@app.route('/')
@app.route('/index')
def index():
    mongo_test = mongo1.db.testCol.find_one({"hello": "world"})
    db_test = mongo1.db.stats.find_one({})
    return render_template('index.html', test=db_test)

@app.route("/chart_test")
def chart_test():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('chart.html', values=values, labels=labels, legend=legend)

@app.route("/get_test", methods=['GET', 'POST'])
def get_test():
    # test idea of using get requests to manipulate graph on page
    # we will implement this first then integrate with the actual json
    test = request.args.get('keyword')
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('requests.html', curr_value=test, values=values, labels=labels, legend=test)

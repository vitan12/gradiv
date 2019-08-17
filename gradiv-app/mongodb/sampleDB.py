from pymongo import MongoClient
from random import randint
from flask_pymongo import PyMongo


mongo1 = MongoClient(port=27017)
db = mongo1.gradb

print ("Hello")
#purges the db
db.schools.drop()

#testing read/write operations of the db
names = ['Upenn','Princeton','Penn State', 'Harvard', 'Colombia','Vanderbilt','UIUC', 'Georgia Tech','Johns Hopkins']
grad_school_type = ['Engineering','Medicine','MBA','Computer Science']
difficulty = ['Very Hard', 'Hard', 'Medium', 'Easy', 'Super Easy', 'Safety']
for x in range(1, 501):
    university = {
        'name' : names[randint(0, (len(names)-1))] + ' University ' + grad_school_type[randint(0, (len(grad_school_type)-1))],
        'rating' : randint(0, 5),
        'difficulty' : difficulty[randint(0, (len(difficulty)-1))] 
    }

    result = db.schools.insert_one(university)
    
    print('Created {0} of 500 as {1}'.format(x,result.inserted_id))

print('finished creating 500 schools')

#TODO
#import from json
#push to database
#compile data from usnews and gradcafe into one json object per

#create seperate file
#create crud functions within python that can be imported and called by the flask app.
    #totall # of applicants in the US vs total vs international
    #filter by GPA/GRE/university/program/year applied using text inputs


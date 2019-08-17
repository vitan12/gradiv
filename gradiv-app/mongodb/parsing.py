from pymongo import MongoClient
from flask_pymongo import PyMongo
import json
import re


mongo = MongoClient(port=27017)
db = mongo.gradb

db.applications.drop()
db.stats.drop()

reviews = db['applications']
university_stats = db['stats']



with open('../scraping_scripts/gradcafe/gradcafe-multiple.json') as f:
    file_data = json.load(f)

for d in file_data["posts"]:
    reviews.insert(d)  
#print(file_data)

regex = re.compile('/accepted/', re.IGNORECASE)

university = {
        'name' : "Princeton university",
        'total_applications' : reviews.count(),
        'accepted' : reviews.find({'result': regex}).count(),
        'americans' : reviews.find({'applicant_type': 'A'}).count(),
        'usInt' : reviews.find({'applicant_type': 'U'}).count(),
        'international' : reviews.find({'applicant_type': 'I'}).count(),
    }

result = university_stats.insert_one(university)

print (university_stats.count())


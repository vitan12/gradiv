from pymongo import MongoClient
from flask_pymongo import PyMongo
import json
import re


mongo = MongoClient(port=27017)
db = mongo.gradb
reviews = db['applications']
university_stats = db['stats']

with open('../scraping_scripts/gradcafe/gradcafe-multiple.json') as f:
    file_data = json.load(f)

reviews.insert_many(file_data)  

regex = re.compile('/accepted/', re.IGNORECASE)

university = {
        'name' : "Princeton university",
        'total_applications' : university_stats.count(),
        'accepted' : university_stats.find({'result': regex}).count(),
        'americans' : university_stats.find({'applicant_type': 'A'}).count(),
        'usInt' : university_stats.find({'applicant_type': 'U'}).count(),
        'international' : university_stats.find({'applicant_type': 'I'}).count(),
    }

result = university_stats.insert_one(university)

print ("Hello")


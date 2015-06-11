import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.students
scores = db.grades

def find():
    query = {'type': 'homework'}

    try:

        cursor = scores.find(query)
        cursor = cursor.sort([('student_id', pymongo.ASCENDING),
                              ('score', pymongo.DESCENDING)])

    except Exception as e:
        print "Unexpected error:", type(e), e

    user = cursor[0]
    for doc in cursor:
        print "Checking for", doc['student_id']
        if doc['student_id'] == user['student_id']:
            print "skip"
        else:
            _id = user['_id']
            scores.delete_one({'_id': _id})
            print "Deleted for ", user['student_id']
        user = doc
    scores.delete_one({'_id': doc['_id']})

find()

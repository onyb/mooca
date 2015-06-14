import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.school
scores = db.students

def update():
    try:
        cursor = scores.find({})

    except Exception as e:
        print "Unexpected error:", type(e), e

    for doc in cursor:
        _id = doc['_id']
        pruned_scores = []
        mx = -1
        for each in doc['scores']:
            if each['type'] == "homework":
                if each['score'] > mx:
                    mx = each['score']
            else:
                pruned_scores.append(each)

        pruned_scores.append({
                                    'type': 'homework',
                                    'score': mx
                            })

        scores.update({'_id': _id}, {'$set': {'scores': pruned_scores}})

update()

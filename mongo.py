import pymongo
import os
if os.path.exists("env.py"):
    import env

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("MONGO is connceted!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to Mongo DB: %s") % e

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

#new_doc = {'first': 'Douglas', 
            #'last': 'Adams', 
            #'dob': '12/03/1952', 
            #'gender': 'male', 
            #'hair_colour': 'grey', 
            #'occupation': 'writer', 
            #'nationality': 'English'} 

#coll.insert(new_doc)

#new_docs = [{'first': 'Terry',
            #'last': 'Pratchett',
            #'dob': '28/04/1948',
            #'gender': 'male',
            #'hair_colour': 'not much',
            #'occupation': 'writer',
            #'nationality': 'English'},
            #{'first': 'George',
            #'last': 'R R Martin',
            #'dob': '20/09/1948',
            #'gender': 'male',
            #'hair_colour': 'white',
            #'occupation': 'writer',
            #'nationality': 'American'}]
#coll.insert_many(new_docs)

#doc_del = coll.delete_one({'first': 'Douglas'})

coll.update_one({'nationality': 'American'}, {'$set': {'hair_colour': 'maroon'}})

documents = coll.find({'nationality': 'American'})

for doc in documents:
    print(doc)
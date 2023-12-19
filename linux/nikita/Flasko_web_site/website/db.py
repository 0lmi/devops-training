from pymongo import MongoClient
from envparse import Env

env = Env()
MONGODB_URL = env.str("MONGODB_URL", default="mongodb://localhost:27017")

client = MongoClient(MONGODB_URL)
notes = MongoClient(MONGODB_URL)


dbname = client['user_auth']
dbname = notes['user_note']

collection_name = dbname["users"]
collection_name = dbname["notes"]


def create_user(email, first_name, password):
    dbname = client['user_auth']
    user = {
        "email": email,
        "first_name": first_name,
        "password": password
    }
    
    x = dbname["users"].insert_one(user)
    

def get_user(email):
    dbname = client['user_auth']
    myquery = { "email": email }
    mydoc = dbname["users"].find_one(myquery)
    return mydoc


def create_note(note):
    note_insert = { "note": note }

    y = dbname["notes"].insert_one(note_insert)


def get_note(note):
    mydoc = { "note": note }
    myquery = dbname["notes"].find_one(mydoc)
    return myquery







from pymongo import MongoClient
from envparse import Env
from bson.objectid import ObjectId

env = Env()
MONGODB_URL = env.str("MONGODB_URL", default="mongodb://localhost:27017")

client = MongoClient(MONGODB_URL)
notes = MongoClient(MONGODB_URL)


dbname = client['user_auth']
dbname = notes['user_notes']

collection_name = dbname["users"]
my_col = dbname["all_notes"]


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


def create_note(note_html):
    dbname = notes['user_notes']
    note_plan = {
        "note_html": note_html
    }
    
    x = dbname["all_notes"].insert_one(note_plan)
    
def find_note():
    dbname = notes['user_notes']
    all_notes = dbname["all_notes"].find()
    return [note['note_html'] for note in all_notes]


def delete_note():
    dbname = notes['user_notes']
    plan = dbname["all_notes"].delete_one()
    return plan
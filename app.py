from models import User, Character, Match
from database import Database

db = Database()

def create(obj):
    if isinstance(obj, User):
        return db.get_collection("users").insert_one(obj.__dict__).inserted_id
    elif isinstance(obj, Character):
        return db.get_collection("characters").insert_one(obj.__dict__).inserted_id
    elif isinstance(obj, Match):
        return db.get_collection("matches").insert_one(obj.__dict__).inserted_id
    else:
        raise ValueError("Invalid object type")

def read(query):
    if "id" in query:
        if "characters" in query:
            return db.get_collection("characters").find_one(query)
        elif "users" in query:
            return db.get_collection("users").find_one(query)
        elif "matches" in query:
            return db.get_collection("matches").find_one(query)
    else:
        raise ValueError("Invalid query")

def update(obj, updates):
    if isinstance(obj, User):
        return db.get_collection("users").update_one({"id": obj.id}, {"$set": updates}).modified_count
    elif isinstance(obj, Character):
        return db.get_collection("characters").update_one({"id": obj.id}, {"$set": updates}).modified_count
    elif isinstance(obj, Match):
        return db.get_collection("matches").update_one({"id": obj.id}, {"$set": updates}).modified_count
    else:
        raise ValueError("Invalid object type")

def delete(obj):
    if isinstance(obj, User):
        return db.get_collection("users").delete_one({"id": obj.id}).deleted_count
    elif isinstance(obj, Character):
        return db.get_collection("characters").delete_one({"id": obj.id}).deleted_count
    elif isinstance(obj, Match):
        return db.get_collection("matches").delete_one({"id": obj.id}).deleted_count
    else:
        raise ValueError("Invalid object type")

from database.db import get_db


def get_admin_collection():
    db = get_db()
    return db["admin"]


def find_admin(email):
    admin_collection = get_admin_collection()
    return admin_collection.find_one({"email": email})
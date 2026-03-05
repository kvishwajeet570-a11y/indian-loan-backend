from database.db import get_db
from datetime import datetime


def get_users_collection():
    
    db = get_db()
    return db["users"]


def create_user(data):

    users_collection = get_users_collection()

    user = {
        "name": data["name"],
        "email": data["email"],
        "password": data["password"],
        "created_at": datetime.utcnow(),
        "wallet_balance": 0,
        "is_admin": False
    }

    return users_collection.insert_one(user)


def find_user_by_email(email):

    users_collection = get_users_collection()

    return users_collection.find_one({"email": email})

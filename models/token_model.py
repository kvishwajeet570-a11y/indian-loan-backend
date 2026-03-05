from database.db import get_db
from datetime import datetime

db = get_db()
token_collection = db["token_blacklist"]


def save_token_model(token):

    token_collection.insert_one({
        "token": token,
        "date": datetime.utcnow()
    })


def check_token_model(token):

    data = token_collection.find_one({
        "token": token
    })

    return data is not None


def delete_old_token_model(old_date):

    token_collection.delete_many({
        "date": {"$lt": old_date}
    })
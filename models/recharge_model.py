from database.db import get_db
from datetime import datetime


def get_recharge_collection():
    db = get_db()
    db = get_db()
    return db["recharges"]


# create recharge
def create_recharge_model(data):

    recharge_collection = get_recharge_collection()

    data["date"] = datetime.utcnow()

    recharge_collection.insert_one(data)


# recharge history
def get_recharge_history_model(email):

    recharge_collection = get_recharge_collection()

    data = list(
        recharge_collection.find(
            {"email": email},
            {"_id": 0}
        )
    )

    return data
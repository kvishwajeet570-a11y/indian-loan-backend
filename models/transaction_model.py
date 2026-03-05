from database.db import get_db
from datetime import datetime

db = get_db()
transaction_collection = db["transactions"]


def create_transaction_model(email, amount, type, source):

    transaction_collection.insert_one({
        "email": email,
        "amount": amount,
        "type": type,  # credit / debit
        "source": source,  # recharge, commission, payout
        "date": datetime.utcnow()
    })


def get_transaction_model(email):

    return list(
        transaction_collection.find(
            {"email": email},
            {"_id": 0}
        ).sort("date", -1)
    )


def get_all_transaction_model():

    return list(
        transaction_collection.find(
            {},
            {"_id": 0}
        ).sort("date", -1)
    )
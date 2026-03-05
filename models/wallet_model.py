from database.db import get_db
from datetime import datetime


def get_wallet_collection():
    # db removed
    db = get_db()
    return db["wallet"]


def get_transaction_collection():
    # db removed
    db = get_db()
    return db["transactions"]


def get_wallet(email):

    wallet_collection = get_wallet_collection()

    wallet = wallet_collection.find_one({"email": email})

    if not wallet:

        wallet_collection.insert_one({
            "email": email,
            "balance": 0,
            "created_at": datetime.utcnow()
        })

        wallet = wallet_collection.find_one({"email": email})

    return wallet


def update_balance(email, amount):

    wallet_collection = get_wallet_collection()

    wallet_collection.update_one(
        {"email": email},
        {"$inc": {"balance": amount}}
    )


def create_transaction(email, amount, type):

    transaction_collection = get_transaction_collection()

    transaction_collection.insert_one({
        "email": email,
        "amount": amount,
        "type": type,
        "date": datetime.utcnow()
    })


def get_transactions(email):

    transaction_collection = get_transaction_collection()

    data = list(
        transaction_collection.find(
            {"email": email},
            {"_id": 0}
        )
    )

    return data
from database.db import get_db
from datetime import datetime

db = get_db()

users_collection = db["users"]
loans_collection = db["loans"]
transactions_collection = db["transactions"]


def system_stats():

    users = users_collection.count_documents({})
    loans = loans_collection.count_documents({})
    transactions = transactions_collection.count_documents({})

    return {
        "users": users,
        "loans": loans,
        "transactions": transactions
    }


def last_transactions(limit=10):

    data = list(
        transactions_collection
        .find({}, {"_id": 0})
        .sort("date", -1)
        .limit(limit)
    )

    return data


def system_health():

    return {
        "status": "running",
        "time": datetime.utcnow()
    }
from database.db import get_db
from datetime import datetime

db = get_db()

fraud_collection = db["fraud_logs"]


def log_fraud(email, reason):

    fraud_collection.insert_one({
        "email": email,
        "reason": reason,
        "date": datetime.utcnow()
    })


def get_fraud_logs():

    return list(
        fraud_collection.find(
            {},
            {"_id": 0}
        ).sort("date", -1)
    )


def is_suspicious(amount):

    if amount > 100000:
        return True

    return False
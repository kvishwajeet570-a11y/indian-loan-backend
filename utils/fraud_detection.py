from database.db import get_db
from datetime import datetime

db = get_db()

fraud_collection = db["fraud_logs"]


def check_fraud(email, ip=None):

    fraud = fraud_collection.find_one({
        "email": email
    })

    if fraud:
        return True

    return False


def log_fraud(email, reason, ip=None):

    fraud_collection.insert_one({
        "email": email,
        "reason": reason,
        "ip": ip,
        "date": datetime.utcnow()
    })

    return True
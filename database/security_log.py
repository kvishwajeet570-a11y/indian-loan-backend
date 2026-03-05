from database.db import get_db
from datetime import datetime

db = get_db()

security_collection = db["security_logs"]


def get_security_collection():
    return security_collection


# SAVE SECURITY LOG
def save_security_log(action, email, ip):

    security_collection.insert_one({
        "action": action,
        "email": email,
        "ip": ip,
        "date": datetime.utcnow()
    })


# GET SECURITY LOGS
def get_security_logs():

    return list(
        security_collection.find(
            {},
            {"_id": 0}
        ).sort("date", -1)
    )
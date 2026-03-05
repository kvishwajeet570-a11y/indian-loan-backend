from database.db import get_db
from datetime import datetime

db = get_db()

monitor_collection = db["monitor_logs"]


def save_monitor_log(action, email):
    monitor_collection.insert_one({
        "action": action,
        "email": email,
        "date": datetime.utcnow()
    })


def get_monitor_logs():
    return list(
        monitor_collection.find(
            {},
            {"_id": 0}
        ).sort("date", -1)
    )
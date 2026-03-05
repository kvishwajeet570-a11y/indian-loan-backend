from database.db import get_db
from datetime import datetime

db = get_db()

backup_collection = db["backup_logs"]


def get_backup_collection():
    return backup_collection


def save_backup_log(filename):

    backup_collection.insert_one({
        "file": filename,
        "date": datetime.utcnow(),
        "status": "success"
    })


def get_backup_logs():

    return list(
        backup_collection.find(
            {},
            {"_id": 0}
        ).sort("date", -1)
    )
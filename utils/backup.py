import json
import os
from datetime import datetime
from database.db import get_db

db = get_db()

BACKUP_FOLDER = "backup"


def create_backup():

    if not os.path.exists(BACKUP_FOLDER):
        os.mkdir(BACKUP_FOLDER)

    backup_data = {}

    collections = db.list_collection_names()

    for collection in collections:
        backup_data[collection] = list(
            db[collection].find({}, {"_id": 0})
        )

    filename = f"{BACKUP_FOLDER}/backup_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w") as file:
        json.dump(
            backup_data,
            file,
            indent=4,
            default=str
        )

    return filename
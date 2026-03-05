from database.db import get_db
from datetime import datetime




def get_security_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["security_logs"]



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

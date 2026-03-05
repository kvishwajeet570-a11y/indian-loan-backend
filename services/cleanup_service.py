import os
from datetime import datetime, timedelta

from database.db import get_db




def get_otp_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["otp"]


def get_token_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["token_blacklist"]


def get_fraud_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["fraud_logs"]



# DELETE EXPIRED OTP

def cleanup_otp():

    expiry_time = datetime.utcnow()

    result = otp_collection.delete_many(

        {"expiry": {"$lt": expiry_time}}

    )

    return result.deleted_count


# DELETE OLD BLACKLIST TOKEN

def cleanup_tokens():

    old_time = datetime.utcnow() - timedelta(days=7)

    result = token_collection.delete_many(

        {"date": {"$lt": old_time}}

    )

    return result.deleted_count


# CLEAN FRAUD LOGS (30 days)

def cleanup_fraud():

    old_time = datetime.utcnow() - timedelta(days=30)

    result = fraud_collection.delete_many(

        {"date": {"$lt": old_time}}

    )

    return result.deleted_count


# CLEAN LOG FILES

def cleanup_logs():

    folder = "logs"

    deleted = 0

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        file_time = datetime.fromtimestamp(

            os.path.getctime(path)

        )

        if datetime.utcnow() - file_time > timedelta(days=30):

            os.remove(path)

            deleted += 1

    return deleted


# CLEAN TEMP FILES

def cleanup_temp():

    folder = "training/temp"

    deleted = 0

    if not os.path.exists(folder):

        return 0

    for file in os.listdir(folder):

        path = os.path.join(folder, file)

        os.remove(path)

        deleted += 1

    return deleted


# MASTER CLEANUP

def run_cleanup():

    otp = cleanup_otp()

    token = cleanup_tokens()

    fraud = cleanup_fraud()

    logs = cleanup_logs()

    temp = cleanup_temp()

    return {

        "status": True,

        "otp_deleted": otp,

        "token_deleted": token,

        "fraud_deleted": fraud,

        "logs_deleted": logs,

        "temp_deleted": temp

    }

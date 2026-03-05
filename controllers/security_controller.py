from database.db import get_db
from datetime import datetime
from services.cleanup_service import run_cleanup

db = get_db()

security_collection = db["security"]
blocked_collection = db["blocked_users"]


def get_security_collection():
    return security_collection


def get_blocked_collection():
    return blocked_collection


# Block User
def block_user_controller(data):

    email = data["email"]

    blocked_collection.update_one(
        {"email": email},
        {
            "$set": {
                "email": email,
                "blocked": True,
                "date": datetime.utcnow()
            }
        },
        upsert=True
    )

    return {
        "status": True,
        "message": "User Blocked Successfully"
    }


# Unblock User
def unblock_user_controller(data):

    email = data["email"]

    blocked_collection.delete_one(
        {"email": email}
    )

    return {
        "status": True,
        "message": "User Unblocked"
    }


# Check Block
def check_block_controller(email):

    user = blocked_collection.find_one({"email": email})

    if user:
        return True

    return False


# Log Security Event
def log_security_event(event, ip, device):

    security_collection.insert_one({
        "event": event,
        "ip": ip,
        "device": device,
        "date": datetime.utcnow()
    })

    return True


# Get Security Logs
def get_logs_controller():

    logs = list(
        security_collection.find(
            {},
            {"_id": 0}
        ).sort("date", -1)
    )

    return {
        "status": True,
        "data": logs
    }


# Run Cleanup
def cleanup_controller():
    return run_cleanup()
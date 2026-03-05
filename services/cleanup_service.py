from database.db import get_db
from datetime import datetime, timedelta

db = get_db()

otp_collection = db["otp"]
token_collection = db["token_blacklist"]
fraud_collection = db["fraud_logs"]


def run_cleanup():

    now = datetime.utcnow()

    # OTP delete (10 minutes old)
    otp_collection.delete_many({
        "date": {"$lt": now - timedelta(minutes=10)}
    })

    # Token delete (1 day old)
    token_collection.delete_many({
        "date": {"$lt": now - timedelta(days=1)}
    })

    # Fraud logs delete (30 days old)
    fraud_collection.delete_many({
        "date": {"$lt": now - timedelta(days=30)}
    })

    return {
        "status": True,
        "message": "Cleanup completed"
    }
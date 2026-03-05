from datetime import datetime, timedelta
from database.db import get_db

db = get_db()

otp_collection = db["otp"]
token_collection = db["token_blacklist"]
fraud_collection = db["fraud_logs"]


def clean_expired_otp():
    otp_collection.delete_many({
        "expire": {"$lt": datetime.utcnow()}
    })


def clean_old_tokens(days=7):
    old_date = datetime.utcnow() - timedelta(days=days)

    token_collection.delete_many({
        "date": {"$lt": old_date}
    })


def clean_old_fraud_logs(days=30):
    old_date = datetime.utcnow() - timedelta(days=days)

    fraud_collection.delete_many({
        "date": {"$lt": old_date}
    })
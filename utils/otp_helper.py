from database.db import get_db
from datetime import datetime, timedelta
import random

db = get_db()

otp_collection = db["otp"]


def generate_otp():
    return str(random.randint(100000, 999999))


def save_otp(phone):
    otp = generate_otp()

    otp_collection.insert_one({
        "phone": phone,
        "otp": otp,
        "expire": datetime.utcnow() + timedelta(minutes=5)
    })

    return otp


def verify_otp(phone, otp):
    data = otp_collection.find_one({
        "phone": phone,
        "otp": otp
    })

    if not data:
        return False

    if data["expire"] < datetime.utcnow():
        return False

    return True
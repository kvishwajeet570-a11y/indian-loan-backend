import random
from datetime import datetime, timedelta
from database.db import get_db

db = get_db()

otp_collection = db["otp"]


def generate_otp():

    return str(random.randint(100000, 999999))


def save_otp(email):

    otp = generate_otp()

    otp_collection.insert_one({
        "email": email,
        "otp": otp,
        "expiry": datetime.utcnow() + timedelta(minutes=5)
    })

    return otp


def verify_otp(email, otp):

    data = otp_collection.find_one({
        "email": email,
        "otp": otp
    })

    if not data:
        return False

    if data["expiry"] < datetime.utcnow():
        return False

    return True
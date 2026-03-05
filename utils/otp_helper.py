import random

from datetime import datetime, timedelta

from database.db import get_db

from utils.mail_config import send_email





def get_otp_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["otp"]



# ============================================
# GENERATE OTP
# ============================================

def generate_otp():

    return str(

        random.randint(

            100000,

            999999

        )

    )


# ============================================
# SEND OTP
# ============================================

def send_otp(email):

    otp = generate_otp()

    expiry = datetime.utcnow() + timedelta(minutes=5)


    otp_collection.update_one(

        {"email": email},

        {

            "$set": {

                "otp": otp,

                "expiry": expiry

            }

        },

        upsert=True

    )


    subject = "Your OTP Code"

    body = f"Your OTP is {otp}"


    send_email(

        email,

        subject,

        body

    )


    return {

        "status": True,

        "message": "OTP Sent"

    }


# ============================================
# VERIFY OTP
# ============================================

def verify_otp(email, otp):

    data = otp_collection.find_one({

        "email": email

    })


    if not data:

        return {

            "status": False,

            "message": "OTP not found"

        }


    if data["otp"] != otp:

        return {

            "status": False,

            "message": "Invalid OTP"

        }


    if datetime.utcnow() > data["expiry"]:

        return {

            "status": False,

            "message": "OTP expired"

        }


    return {

        "status": True,

        "message": "OTP Verified"

    }

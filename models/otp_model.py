from database.db import get_db
from datetime import datetime, timedelta




def get_otp_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["otp"]



def save_otp(email, otp):

    otp_collection.update_one(

        {"email": email},

        {
            "$set": {

                "email": email,
                "otp": otp,
                "expiry": datetime.utcnow() + timedelta(minutes=5)

            }

        },

        upsert=True

    )


def verify_otp(email, otp):

    data = otp_collection.find_one({"email": email})

    if not data:

        return False

    if data["otp"] != otp:

        return False

    if datetime.utcnow() > data["expiry"]:

        return False

    return True

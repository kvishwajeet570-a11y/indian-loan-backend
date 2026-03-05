from database.db import get_db
from datetime import datetime
import random




def get_referral_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["referrals"]



def generate_referral_code():

    code = "REF" + str(random.randint(10000, 99999))

    return code


def create_referral(email):

    code = generate_referral_code()

    referral_collection.insert_one({

        "email": email,
        "code": code,
        "team": [],
        "date": datetime.utcnow()

    })

    return code


def get_referral(email):

    return referral_collection.find_one(

        {"email": email},

        {"_id": 0}

    )


def add_team(ref_code, new_email):

    referral_collection.update_one(

        {"code": ref_code},

        {"$push": {"team": new_email}}

    )


def get_team(email):

    data = get_referral(email)

    if data:

        return data["team"]

    return []

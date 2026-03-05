from database.db import get_db
from datetime import datetime
from database.db import get_db

db = get_db()

commission_collection = db["commissions"]



def get_commission_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["commissions"]



# SAVE COMMISSION

def create_commission_model(data):

    """
    data = {
        email,
        amount,
        commission,
        source
    }
    """

    commission_collection.insert_one({

        "email": data["email"],

        "amount": data["amount"],

        "commission": data["commission"],

        "source": data["source"],

        "date": datetime.utcnow()

    })


# USER COMMISSION HISTORY

def get_user_commission_model(email):

    return list(

        commission_collection.find(

            {"email": email},

            {"_id": 0}

        ).sort("date", -1)

    )


# ADMIN ALL COMMISSION

def get_all_commission_model():

    return list(

        commission_collection.find(

            {},

            {"_id": 0}

        ).sort("date", -1)

    )


# TOTAL USER COMMISSION

def get_total_commission_model(email):

    data = commission_collection.aggregate([

        {

            "$match": {

                "email": email

            }

        },

        {

            "$group": {

                "_id": None,

                "total": {

                    "$sum": "$commission"

                }

            }

        }

    ])

    result = list(data)

    if result:

        return result[0]["total"]

    return 0


# DELETE COMMISSION (Admin)

def delete_commission_model(email):

    commission_collection.delete_many({

        "email": email

    })

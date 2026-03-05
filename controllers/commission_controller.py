from database.db import get_db
from flask_jwt_extended import get_jwt_identity




def get_commission_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["commissions"]



# USER COMMISSION

def my_commission_controller():

    email = get_jwt_identity()

    data = list(

        commission_collection.find(

            {"email": email},

            {"_id": 0}

        )

    )

    return {

        "status": True,
        "data": data

    }


# ADMIN ALL COMMISSION

def all_commission_controller():

    data = list(

        commission_collection.find(

            {},

            {"_id": 0}

        )

    )

    return {

        "status": True,
        "data": data

    }

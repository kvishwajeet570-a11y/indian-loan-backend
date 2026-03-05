from flask import request
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

from database.db import get_db
from datetime import datetime
from database.db import get_db

db = get_db()

device_collection = db["devices"]




def get_device_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["device_logs"]



# ===============================
# GET DEVICE INFO
# ===============================

def get_device_info():

    return {

        "ip": request.remote_addr,

        "user_agent": request.headers.get("User-Agent"),

        "device": request.user_agent.platform,

        "browser": request.user_agent.browser,

        "version": request.user_agent.version,

        "date": datetime.utcnow()

    }


# ===============================
# SAVE DEVICE
# ===============================

def save_device(email):

    device = get_device_info()


    existing = device_collection.find_one({

        "email": email,

        "ip": device["ip"],

        "user_agent": device["user_agent"]

    })


    if not existing:

        device["email"] = email

        device["status"] = "Active"

        device_collection.insert_one(device)


# ===============================
# TRACK DEVICE MIDDLEWARE
# ===============================

def track_device():

    try:

        verify_jwt_in_request()

        email = get_jwt_identity()

        save_device(email)

    except:

        pass


# ===============================
# GET USER DEVICES
# ===============================

def get_user_devices(email):

    return list(

        device_collection.find(

            {"email": email},

            {"_id": 0}

        )

    )


# ===============================
# BLOCK DEVICE
# ===============================

def block_device(ip):

    device_collection.update_one(

        {"ip": ip},

        {

            "$set": {

                "status": "Blocked"

            }

        }

    )


# ===============================
# CHECK BLOCKED DEVICE
# ===============================

def is_blocked_device():

    ip = request.remote_addr


    device = device_collection.find_one({

        "ip": ip,

        "status": "Blocked"

    })


    if device:

        return True


    return False

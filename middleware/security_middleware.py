from flask import request, jsonify

from database.security_log import save_security_log

from database.db import get_db
from database.db import get_db

db = get_db()




# CHECK BLOCKED USER

def check_blocked_user(email):

    user = db["users"].find_one({

        "email": email,

        "blocked": True

    })

    if user:

        return True

    return False


# INJECTION PROTECTION

def detect_injection(data):

    keywords = [

        "$",

        "{",

        "}",

        "delete",

        "drop",

        "remove"

    ]

    for key in keywords:

        if key in str(data):

            return True

    return False


# MAIN SECURITY CHECK

def security_check():

    ip = request.remote_addr

    data = request.json


    if data:

        if detect_injection(data):

            save_security_log(

                "Injection Attempt",

                "Unknown",

                ip

            )

            return jsonify({

                "status": False,

                "message": "Security Threat Detected"

            }), 403


    return None

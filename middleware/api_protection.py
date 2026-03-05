from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request
from database.security_log import save_security_log

import time


# ===============================
# BLOCKED IPS
# ===============================

BLOCKED_IPS = []


# ===============================
# REQUEST LIMIT SYSTEM
# ===============================

REQUEST_LOG = {}

MAX_REQUEST = 100

TIME_WINDOW = 60   # seconds


# ===============================
# CHECK RATE LIMIT
# ===============================

def rate_limit_check(ip):

    current_time = time.time()


    if ip not in REQUEST_LOG:

        REQUEST_LOG[ip] = []


    # Remove old requests

    REQUEST_LOG[ip] = [

        t for t in REQUEST_LOG[ip]

        if current_time - t < TIME_WINDOW

    ]


    if len(REQUEST_LOG[ip]) >= MAX_REQUEST:

        return False


    REQUEST_LOG[ip].append(current_time)

    return True


# ===============================
# MAIN API PROTECTION
# ===============================

def api_protection():

    ip = request.remote_addr


    # BLOCK IP

    if ip in BLOCKED_IPS:

        return jsonify({

            "status": False,

            "message": "IP Blocked"

        }), 403


    # RATE LIMIT

    if not rate_limit_check(ip):

        save_security_log(

            "Rate Limit Exceeded",

            "Unknown",

            ip

        )

        return jsonify({

            "status": False,

            "message": "Too many requests"

        }), 429


    # JWT CHECK FOR PROTECTED ROUTES

    if request.path.startswith("/api"):

        if request.path not in [

            "/api/login",

            "/api/register"

        ]:

            try:

                verify_jwt_in_request()

            except:

                save_security_log(

                    "Unauthorized Access",

                    "Unknown",

                    ip

                )

                return jsonify({

                    "status": False,

                    "message": "Unauthorized"

                }), 401


    return None

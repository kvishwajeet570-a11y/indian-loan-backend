from flask import request, jsonify
import time

# IP based request log

REQUESTS = {}

MAX_REQUESTS = 100

WINDOW_TIME = 60   # seconds


def rate_limit():

    ip = request.remote_addr

    current_time = time.time()


    if ip not in REQUESTS:

        REQUESTS[ip] = []


    # remove old requests

    REQUESTS[ip] = [

        t for t in REQUESTS[ip]

        if current_time - t < WINDOW_TIME

    ]


    if len(REQUESTS[ip]) >= MAX_REQUESTS:

        return jsonify({

            "status": False,

            "message": "Too many requests"

        }), 429


    REQUESTS[ip].append(current_time)


    return None

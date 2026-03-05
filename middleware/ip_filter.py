from flask import request, jsonify


BLOCKED_IPS = [

    "192.168.1.10"

]


def ip_filter():

    ip = request.remote_addr


    if ip in BLOCKED_IPS:

        return jsonify({

            "status": False,

            "message": "IP Blocked"

        }), 403


    return None

from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request

from utils.token_blacklist import is_blacklisted


# Protect API

def token_required():

    verify_jwt_in_request()

    token = request.headers.get("Authorization")

    if token:

        token = token.split(" ")[1]

        if is_blacklisted(token):

            return jsonify({

                "status": False,
                "message": "Token Blocked"

            }), 401

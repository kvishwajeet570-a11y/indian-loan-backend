from flask import request, jsonify


# dangerous keywords

BLOCKED = [

    "$",

    "{",

    "}",

    "drop",

    "delete",

    "remove",

    "update"

]


def validate_request():

    data = request.json


    if not data:

        return None


    for word in BLOCKED:

        if word in str(data):

            return jsonify({

                "status": False,

                "message": "Invalid request detected"

            }), 400


    return None

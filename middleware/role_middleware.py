from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from flask import jsonify

from database.db import get_db





# ROLE CHECK

def role_required(role):

    def wrapper(fn):

        def decorator(*args, **kwargs):

            verify_jwt_in_request()

            email = get_jwt_identity()


            user = db["users"].find_one({

                "email": email

            })


            if not user:

                return jsonify({

                    "status": False,

                    "message": "User not found"

                }), 404


            if user.get("role") != role:

                return jsonify({

                    "status": False,

                    "message": "Access denied"

                }), 403


            return fn(*args, **kwargs)


        decorator.__name__ = fn.__name__

        return decorator

    return wrapper

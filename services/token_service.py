from utils.token_blacklist import blacklist_token


# Logout Service

def logout_service(token):

    blacklist_token(token)

    return {

        "status": True,
        "message": "Logout Success"

    }

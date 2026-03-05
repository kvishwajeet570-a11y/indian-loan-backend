from models.token_model import (
    save_token_model,
    check_token_model
)


# Add blacklist

def blacklist_token(token):

    save_token_model(token)


# Check blacklist

def is_blacklisted(token):

    return check_token_model(token)

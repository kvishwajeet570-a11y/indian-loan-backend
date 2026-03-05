from database.db import get_db
from datetime import datetime
from database.db import get_db

db = get_db()

token_collection = db["tokens"]




def get_token_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["token_blacklist"]



# Save Blacklist Token

def save_token_model(token):

    token_collection.insert_one({

        "token": token,
        "date": datetime.utcnow()

    })


# Check Token

def check_token_model(token):

    data = token_collection.find_one({

        "token": token

    })

    return data is not None


# Delete Old Token

def delete_old_token_model(old_date):

    token_collection.delete_many({

        "date": {"$lt": old_date}

    })

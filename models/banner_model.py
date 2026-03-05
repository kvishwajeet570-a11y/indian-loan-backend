from database.db import get_db
from datetime import datetime
from database.db import get_db

db = get_db()

banner_collection = db["banners"]



def get_banner_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["banners"]



def create_banner(data):

    banner = {

        "title": data["title"],
        "image": data["image"],
        "status": True,
        "date": datetime.utcnow()

    }

    banner_collection.insert_one(banner)


def get_active_banner():

    banner = banner_collection.find_one(

        {"status": True},

        {"_id": 0}

    )

    return banner


def get_all_banners():

    return list(

        banner_collection.find(

            {},

            {"_id": 0}

        )

    )

from database.db import get_db
from datetime import datetime

from database.db import get_db

db = get_db()

training_collection = db["training"]


def get_training_collection():
    from database.db import get_db
    db = get_db()
    db = get_db()
    return db["training_videos"]



# Add video

def add_video_model(data):

    training_collection.insert_one({

        "title": data["title"],
        "description": data["description"],
        "video": data["video"],
        "thumbnail": data["thumbnail"],
        "status": True,
        "date": datetime.utcnow()

    })


# Get all videos

def get_all_videos_model():

    return list(

        training_collection.find(

            {"status": True},

            {"_id": 0}

        )

    )


# Delete video

def delete_video_model(title):

    training_collection.delete_one(

        {"title": title}

    )

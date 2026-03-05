from database.db import get_db
from datetime import datetime

db = get_db()
training_collection = db["training_videos"]


def add_video_model(data):

    training_collection.insert_one({
        "title": data["title"],
        "description": data["description"],
        "video": data["video"],
        "thumbnail": data["thumbnail"],
        "status": True,
        "date": datetime.utcnow()
    })


def get_all_videos_model():

    return list(
        training_collection.find(
            {"status": True},
            {"_id": 0}
        )
    )


def delete_video_model(title):

    training_collection.delete_one(
        {"title": title}
    )
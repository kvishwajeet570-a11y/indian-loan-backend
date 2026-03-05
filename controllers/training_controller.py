from models.training_model import add_video_model, get_all_videos_model, delete_video_model


# Add video

def add_training_controller(data):

    add_video_model(data)

    return {

        "status": True,
        "message": "Training Video Added"

    }


# Get videos

def get_training_controller():

    videos = get_all_videos_model()

    return {

        "status": True,
        "data": videos

    }


# Delete video

def delete_training_controller(data):

    delete_video_model(data["title"])

    return {

        "status": True,
        "message": "Video Deleted"

    }

import os

VIDEO_FOLDER = "training/videos"

THUMB_FOLDER = "training/thumbnails"


# Save video

def save_video(file):

    filename = file.filename

    path = os.path.join(VIDEO_FOLDER, filename)

    file.save(path)

    return filename


# Save thumbnail

def save_thumbnail(file):

    filename = file.filename

    path = os.path.join(THUMB_FOLDER, filename)

    file.save(path)

    return filename

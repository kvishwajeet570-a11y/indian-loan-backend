import os

UPLOAD_FOLDER = "static/banners"


def save_banner(file):

    filename = file.filename

    path = os.path.join(UPLOAD_FOLDER, filename)

    file.save(path)

    return filename

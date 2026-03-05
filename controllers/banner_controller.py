from models.banner_model import create_banner, get_active_banner, get_all_banners


def add_banner(data):

    create_banner(data)

    return {

        "status": True,
        "message": "Banner Added"

    }


def get_banner():

    banner = get_active_banner()

    return {

        "status": True,
        "data": banner

    }


def all_banners():

    banners = get_all_banners()

    return {

        "status": True,
        "data": banners

    }

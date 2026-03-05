import logging
import os


LOG_FOLDER = "logs"


# ============================================
# CREATE LOG FOLDER
# ============================================

if not os.path.exists(LOG_FOLDER):

    os.mkdir(LOG_FOLDER)


# ============================================
# LOGGER CONFIG
# ============================================

logging.basicConfig(

    filename=f"{LOG_FOLDER}/app.log",

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)


# ============================================
# LOG FUNCTIONS
# ============================================

def log_info(message):

    logging.info(message)


def log_warning(message):

    logging.warning(message)


def log_error(message):

    logging.error(message)


def log_security(message):

    logging.critical(message)

from utils.backup import create_backup
from database.backup_log import save_backup_log, get_backup_logs


# CREATE BACKUP

def backup_service():

    filename = create_backup()

    save_backup_log(filename)


    return {

        "status": True,

        "message": "Backup Created",

        "file": filename

    }


# GET LOGS

def backup_logs_service():

    logs = get_backup_logs()


    return {

        "status": True,

        "data": logs

    }

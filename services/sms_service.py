import requests
from utils.sms_config import FAST2SMS_API_KEY


def send_sms(mobile, message):

    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = {

        "sender_id": "FSTSMS",
        "message": message,
        "language": "english",
        "route": "q",
        "numbers": mobile

    }

    headers = {

        "authorization": FAST2SMS_API_KEY,
        "Content-Type": "application/json"

    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()

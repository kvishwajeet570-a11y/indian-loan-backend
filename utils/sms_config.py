import requests
from config import Config


SMS_API_KEY = Config.SMS_API_KEY


# ============================================
# SEND SMS FUNCTION
# ============================================

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

        "authorization": SMS_API_KEY,

        "Content-Type": "application/json"

    }

    try:

        response = requests.post(

            url,

            json=payload,

            headers=headers

        )

        return response.json()

    except Exception as e:

        print("SMS Error:", e)

        return None

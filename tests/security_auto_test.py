import requests
import time

BASE_URL = "http://127.0.0.1:5000"


# ==========================================
# LOGIN TEST
# ==========================================

def login():

    url = f"{BASE_URL}/api/login"

    data = {

        "email": "pritam@gmail.com",

        "password": "123456"

    }

    res = requests.post(url, json=data)

    print("\nLogin Response:", res.json())

    if res.status_code == 200:

        return res.json().get("token")

    return None


# ==========================================
# UNAUTHORIZED TEST
# ==========================================

def unauthorized_test():

    url = f"{BASE_URL}/api/wallet/balance"

    res = requests.get(url)

    print("\nUnauthorized Test:")

    print(res.status_code, res.text)


# ==========================================
# AUTHORIZED TEST
# ==========================================

def authorized_test(token):

    url = f"{BASE_URL}/api/wallet/balance"

    headers = {

        "Authorization": f"Bearer {token}"

    }

    res = requests.get(url, headers=headers)

    print("\nAuthorized Test:")

    print(res.status_code, res.text)


# ==========================================
# BRUTE FORCE TEST
# ==========================================

def brute_force_test():

    print("\nBrute Force Test Started...")

    url = f"{BASE_URL}/api/login"

    for i in range(10):

        data = {

            "email": "pritam@gmail.com",

            "password": "wrongpassword"

        }

        res = requests.post(url, json=data)

        print(f"Attempt {i+1}:", res.status_code)

        time.sleep(0.5)


# ==========================================
# RATE LIMIT TEST
# ==========================================

def rate_limit_test(token):

    print("\nRate Limit Test Started...")

    url = f"{BASE_URL}/api/security/logs"

    headers = {

        "Authorization": f"Bearer {token}"

    }

    for i in range(120):

        res = requests.get(url, headers=headers)

        print(f"Request {i+1}: {res.status_code}")

        if res.status_code == 429:

            print("Rate limit working!")

            break


# ==========================================
# VULNERABILITY TEST
# ==========================================

def injection_test(token):

    print("\nInjection Test Started...")

    url = f"{BASE_URL}/api/recharge"

    headers = {

        "Authorization": f"Bearer {token}"

    }

    data = {

        "email": "test@gmail.com",

        "amount": {"$gt": ""}

    }

    res = requests.post(url, json=data, headers=headers)

    print(res.status_code, res.text)


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    unauthorized_test()

    token = login()

    if token:

        authorized_test(token)

        brute_force_test()

        rate_limit_test(token)

        injection_test(token)

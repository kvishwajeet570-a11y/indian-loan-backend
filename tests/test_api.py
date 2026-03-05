import requests


BASE_URL = "http://127.0.0.1:5000"


TOKEN = "PASTE_TOKEN_HERE"


headers = {

    "Authorization": f"Bearer {TOKEN}"

}


# ======================================
# WALLET TEST
# ======================================

def wallet_test():

    url = f"{BASE_URL}/api/wallet/balance"

    r = requests.get(

        url,

        headers=headers

    )

    print("\nWallet Test")

    print(r.json())


# ======================================
# LOAN TEST
# ======================================

def loan_test():

    url = f"{BASE_URL}/api/loan/history"

    r = requests.get(

        url,

        headers=headers

    )

    print("\nLoan Test")

    print(r.json())


# ======================================
# RUN
# ======================================

wallet_test()

loan_test()

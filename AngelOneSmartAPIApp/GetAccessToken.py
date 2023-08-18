import os
from kiteconnect import KiteConnect
import time, json, datetime, sys
import xlwings as xw
import pandas as pd

def get_access_token():
    global access_token

    def login():
        global login_credential
        print("Trying Log In...")
        kite = KiteConnect(api_key=login_credential["api_key"])
        print("Login url : ", kite.login_url())
        request_tkn = input("Login and enter your request token here : ")
        try:
            access_token = kite.generate_session(request_token=request_tkn, api_secret=login_credential["api_secret"])[
                'access _token']
            os.makedirs(f"AccessToken", exist_ok=True)
            with open(f"AccessToken/{datetime.datetime.now().date()}. json", "w") as f:
                json.dump(access_token, f)
            print("Login successful...")
        except Exception as e:
            print(f"Login Failed {{{e}}}")

    print("Loading access token...")
    while True:
        if os.path.exists(f"AccessToken/{datetime.datetime.now().date()}.json"):
            with open(f"AccessToken/{datetime.datetime.now().date()}.json", "r") as f:
                access_token = json.load(f)
            break
        else:
            login()
    return access_token
import os
import time, json, datetime, sys
from GetLoginCredential import *
import xlwings as xw
import pandas as pd
from SmartApi import SmartConnect #or from SmartApi.smartConnect import SmartConnect
import pyotp

access_token = ""


def get_access_token():
    global access_token

    def login():
        get_api_key = get_login_credentials()
        print("Trying Log In...")
        kite = KiteConnect(api_key=get_api_key["api_key"])
        print("Login url : ", kite.login_url())
        request_tkn = input("Login and enter your request token here : ")
        try:
            access_token = kite.generate_session(request_token=request_tkn, api_secret=login_credential["api_secret"])[
                'access_token']
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

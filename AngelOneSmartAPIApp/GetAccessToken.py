import os
import time, json, datetime, sys
from AngelOneSmartAPIApp.GetLoginCredential import *
import xlwings as xw
import pandas as pd
from SmartApi import SmartConnect  # or from SmartApi.smartConnect import SmartConnect
import pyotp

access_token = ""


def get_access_token():
    global access_token

    api_key = get_login_credentials()["api_key"]
    clientId = get_login_credentials()["clientId"]
    pwd = get_login_credentials()["pwd"]
    token = get_login_credentials()["token"]
    smartApi = SmartConnect(api_key)
    totp = pyotp.TOTP(token).now()
    correlation_id = "abc123"
    data = smartApi.generateSession(clientId, pwd, totp)

    def login():
        global access_token
        try:
            print("Trying Log In...")
            access_token = {"authToken": data['data']['jwtToken'],
                            "refreshToken": data['data']['refreshToken'],
                            "feedToken": smartApi.getfeedToken(),
                            }
            os.makedirs(f"AccessToken", exist_ok=True)

            with open(f"AccessToken/{datetime.datetime.now().date()}.json", "w") as g:
                json.dump(access_token, g)
            print("Login successful...")
        except Exception as e:
            print(f"Login Failed {{{e}}}")

    while True:
        if os.path.exists(f"AccessToken/{datetime.datetime.now().date()}.json"):
            with open(f"AccessToken/{datetime.datetime.now().date()}.json", "r") as f:
                access_token = json.load(f)
            break
        else:
            login()
    return smartApi, access_token

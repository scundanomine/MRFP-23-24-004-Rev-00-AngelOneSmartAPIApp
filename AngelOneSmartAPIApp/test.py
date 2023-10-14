import os
import time, json, datetime, sys
from AngelOneSmartAPIApp.GetLoginCredential import *
import xlwings as xw
import pandas as pd
from SmartApi import SmartConnect  # or from SmartApi.smartConnect import SmartConnect
import pyotp
from GetLiveData import *


def getAccessTokenOne(apiKey):
    accessToken = []
    api_key = apiKey
    clientId = "J52460798"
    pwd = "4235"
    token = "4AGGACU2HEUMO2T2UV5YZHNG7M"
    smartApi = SmartConnect(api_key)
    totp = pyotp.TOTP(token).now()
    correlation_id = "abc123"
    data = smartApi.generateSession(clientId, pwd, totp)
    while True:
        try:
            print("Trying Log In...")
            accessToken = {"authToken": data['data']['jwtToken'],
                           "refreshToken": data['data']['refreshToken'],
                           "feedToken": smartApi.getfeedToken(),
                           }
            break
        except:
            pass
    print("boom!!!!")
    return smartApi, accessToken


objOne, accessTokenOne = getAccessTokenOne("h7mCIfdW")
time.sleep(1)
objTwo, accessTokenTwo = getAccessTokenOne("jOagziES")
print(getLiveData(objOne, "RELIANCE-EQ", "2885"))
print(getLiveData(objTwo, "JINDALSTEL-EQ", "6733"))
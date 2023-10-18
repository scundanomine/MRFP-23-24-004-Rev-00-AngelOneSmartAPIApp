import os
import time, json, datetime, sys
from AngelOneSmartAPIApp.GetLoginCredential import *
import xlwings as xw
import pandas as pd
from SmartApi import SmartConnect  # or from SmartApi.smartConnect import SmartConnect
import pyotp
from concurrent.futures import ProcessPoolExecutor
from niftytokens_cap_and_filters.GetTraditionalPivotsForSpecificNifty import *


def getAccessTokenOne(apiKey, clientIdOne, passW, tok):
    accessToken = []
    api_key = apiKey
    clientId = clientIdOne
    pwd = passW
    token = tok
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


# objOne, accessTokenOne = getAccessTokenOne("h7mCIfdW", "J52460798", "4235", "4AGGACU2HEUMO2T2UV5YZHNG7M")
# time.sleep(1)
# objTwo, accessTokenTwo = getAccessTokenOne("F5SzrULj", "S53761277", "8813", "2NF7QBQP7R3NEDXC4VN6UNWYWM")
# # getTraditionalPivotsForSpecificNiftyFile("nifty500", 2, 50, objOne)
# # getTraditionalPivotsForSpecificNiftyFile("nifty500", 52, 100, objTwo)
# # print(getLiveData(objOne, "RELIANCE-EQ", "2885"))
# # print(getLiveData(objTwo, "JINDALSTEL-EQ", "6733"))
# if __name__ == '__main__':
#     with ProcessPoolExecutor() as executor:
#         sheetList = ["nifty500", "nifty500"]
#         lList = [2, 52]
#         uList = [50, 100]
#         objList = [objOne, objOne]
#         wList = [1, 50]
#         p = executor.map(getTraditionalPivotsForSpecificNiftyFile, sheetList, lList, uList, objList, wList)

# import os
# import time, json, datetime, sys
# from GetLoginCredential import *
import xlwings as xw
from GetAccessToken import *
# import pandas as pd
# from SmartApi import SmartConnect  # or from SmartApi.smartConnect import SmartConnect
# import pyotp


def getLiveData(instruments):
    # global kite, live_data
    obj, toc = get_access_token()
    exchange = "NSE"
    sheet = xw.Book(
        "E:/WebDevelopment/2023-2024/MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp/AngelOneSmartAPIApp/TA_Python.xlsm").sheets[
        0]
    scriptList = {
        'AAKASH-EQ': '235'
    }
    sheet.range("A1").value = "35"

    ltp = obj.ltpData("NSE", "SBIN-EQ", "3045")
    print("Ltp Data :", ltp)
    ltp = obj.ltpData("NSE", "MOL-EQ", "5394")
    print("Ltp Data :", ltp)

    # ltp = obj.ltpData("NSE", "AAKASH-EQ", "235")
    # print("Ltp Data :", ltp)
    # ltp = obj.ltpData("NSE", "SBIN-EQ", "3045")
    # print("Ltp Data :", ltp)
    # sheet.range("A1").value = LTP['data']['high']
    # sheet.range("A2").value = LTP['data']['low']
    # sheet.range("A3").value = LTP['data']['open']
    # try:
    #     live_data
    # except:
    #     live_data = {}
    # try:
    #     live_data = kite.quote(instruments)
    # except Exception as e:
    #     # print(f'Get live_data Failed {{{e}}}")
    #     pass
    # return live_datakis Please


getLiveData(25)

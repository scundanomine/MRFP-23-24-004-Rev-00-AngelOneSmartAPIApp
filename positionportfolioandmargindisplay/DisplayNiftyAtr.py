import pandas as pd
import xlwings as xw


def displayNiftyAtr(atr):
    while True:
        try:
            # getting data from the sheet
            wb = xw.Book(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            dt = wb.sheets("MAndP")
            # df = getterMarketStructureDf()

            dt["M2"].value = atr
            break
        except Exception as e:
            print(f"The exception while displayNiftyAtr is {e}")


# cvp = getterTimeDelta()
# displayNiftyAtr(atr)

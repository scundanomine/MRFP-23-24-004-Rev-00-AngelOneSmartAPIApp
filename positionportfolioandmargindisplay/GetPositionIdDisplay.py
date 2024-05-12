import xlwings as xw
from portfolio.GetterFixedPortfolio import getterFixedPortfolio
from position.GetterPositionIdForSpecificDate import getterPositionIdForSpecificDate
from position.GetterPositionList import getterPositionList


def getPositionIdDisplay(rDate):
    pid = getterPositionIdForSpecificDate(rDate)
    while True:
        try:
            wb = xw.Book(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            dt['O2'].value = pid
            break
        except Exception as e:
            print(f"Exception while getPositionIdDisplay is {e}")

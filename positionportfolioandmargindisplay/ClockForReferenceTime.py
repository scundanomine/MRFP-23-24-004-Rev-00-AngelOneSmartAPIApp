import datetime

import xlwings as xw
import pandas as pd
from margin.GetterAvailableMargin import getterAvailableMargin


def  clockForReferenceTime(cv):
    while True:
        try:
            wb = xw.Book(
                "F:\\AT\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            pt = datetime.datetime.now() - cv
            dt['S2'].value = pt.strftime("%H:%M:%S")
            break
        except Exception as e:
            print(f"Exception while getMarginDisplay is {e}")

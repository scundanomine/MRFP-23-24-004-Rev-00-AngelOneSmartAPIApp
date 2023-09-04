from PivotLevelFinding import *
import xlwings as xw
import pandas as pd

wb = xw.Book("../AngelOneSmartAPIApp/TA_Python.xlsm")
dt = wb.sheets("Exchange")

reqD = getPivot()
dt.range("E1:l202").options(pd.DataFrame, index=False).value = reqD[
    ["ltp", "sr1", "sr2", "sr3", "sr4", "sr5", "sr6", "sr7"]]

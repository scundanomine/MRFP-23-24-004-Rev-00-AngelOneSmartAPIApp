from PivotLevelFinding import *
import xlwings as xw
import pandas as pd
import time


start_time = time.time()
wb = xw.Book("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
dt = wb.sheets("Exchange")

reqD = getPivot()
dt.range("f1:m202").options(pd.DataFrame, index=False).value = reqD[
    ["ltp", "sr1", "sr2", "sr3", "sr4", "sr5", "sr6", "sr7"]]
print("--- %s seconds ---" % (time.time() - start_time))

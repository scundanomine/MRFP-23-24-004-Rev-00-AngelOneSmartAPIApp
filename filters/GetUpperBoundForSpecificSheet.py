import xlwings as xw
from concurrent.futures import ThreadPoolExecutor
import time


def getUpperBoundForSpecificSheet(sheetName):
    startTime = time.time()
    wb = xw.Book(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
    dt = wb.sheets(sheetName)

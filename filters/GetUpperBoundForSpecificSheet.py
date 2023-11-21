import xlwings as xw
from concurrent.futures import ThreadPoolExecutor
import time
import math

dataList = []
n = 0
mn = 0


def getUpperBoundForSpecificSheet(sheetName, ect=2):
    global dataList, n, mn
    startTime = time.time()
    wb = xw.Book(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
    dt = wb.sheets(sheetName)
    dataList = dt.range(f"a{ect}:a503").value
    # print(dataList)
    # magic no.
    n = len(dataList)
    mn = math.floor(pow(len(dataList), 0.5))
    upperBound = 0

    def getUpperBound(r):
        global dataList, n, mn
        ubL = 0
        for i in range(r - mn, r):
            if i < n:
                if dataList[i] is None:
                    ubL = i + ect - 1
                    return ubL
            else:
                return 0
        return ubL

    with ThreadPoolExecutor() as executor:
        lt = list(range(mn, mn * mn + 3 * mn, mn))
        # print(lt)
        results = executor.map(getUpperBound, lt)
        for result in results:
            if result != 0:
                upperBound = result
                break
    print(f"time of execution is {time.time() - startTime}")

    return upperBound


print(getUpperBoundForSpecificSheet("BlackList"))

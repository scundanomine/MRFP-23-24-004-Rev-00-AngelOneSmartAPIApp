import pandas as pd
import time
import xlwings as xw
from concurrent.futures import ThreadPoolExecutor
from filters.GetUpperBoundForSpecificSheet import *
from filters.GetDfForFilter import *


def getDesiredFilterResults(source, target, sectorList):
    startTime = time.time()
    ub = getUpperBoundForSpecificSheet(source)

    # get df
    df = getDfForFilter(source, ub)

    print(df["id"])

    # storing filter results in target df
    tdf = pd.DataFrame(columns=df.columns)
    for lstItem in sectorList:
        ldf = tdf.merge(df.loc[df['sector'] == lstItem], how='right')
        tdf = pd.concat([tdf, ldf])
    print(tdf)

    # save results in target sheet
    wb = xw.Book(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
    dt = wb.sheets(target)
    dt.range(f"a1:u{ub}").options(pd.DataFrame, index=False).value = tdf

    # load results in the .csv file
    tdf.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\filters\\filter_state\\filter.csv", index=False)
    print(f"time of execution is {time.time() - startTime}")


getDesiredFilterResults("nifty500", "Exchange", ["Oil Gas & Consumable Fuels", "Financial Services"])

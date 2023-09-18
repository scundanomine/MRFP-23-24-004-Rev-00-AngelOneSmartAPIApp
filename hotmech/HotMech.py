import pandas as pd
import xlwings as xw
from hotmech.GetHotMechLIst import *
from hotmech.GetHotelRoomKey import *
import time

global htR


def hotMech(uid, desc, symbol, sector, token, ltp, rft, typ):
    start_time = time.time()
    global htR
    htR = getHotMechList()
    roomKey = getHotelRoomKey()

    # print(roomKey)
    if roomKey != 0:
        index = roomKey - 1
        htR.loc[index, "rft"] = rft
        htR.loc[index, "id"] = uid
        htR.loc[index, "desc"] = desc
        htR.loc[index, "sector"] = sector
        htR.loc[index, "symbol"] = symbol
        htR.loc[index, "token"] = token
        htR.loc[index, "ltp"] = ltp
        htR.loc[index, "typ"] = typ

    # loading csv file
    htR.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\hotmech\\HotMechLst.csv",
               index=False)

    # loading the excel
    wb = xw.Book("../AngelOneSmartAPIApp/TA_Python.xlsm")
    dt = wb.sheets("Vitals")
    dt.range("a5:i105").options(pd.DataFrame, index=False).value = htR
    print("--- %s seconds ---" % (time.time() - start_time))


hotMech(23, "dhkjh", "dsmjdklsh", "bankpo", "jhdkfjgh", 1234, 145544, "S")

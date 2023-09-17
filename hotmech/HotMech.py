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

    print("--- %s seconds ---" % (time.time() - start_time))
    print(roomKey)


hotMech(23, "dhkjh", "dsmjdklsh", "bankpo", "token", 1234, 145544, "S")
# for rows in htR.iterrows():
#     if rows["id"] == 0:
#         index = rows["slot"]
#         htR.loc[index - 1, "rft"] = rft
#         htR.loc[index - 1, "id"] = uid
#         htR.loc[index - 1, "desc"] = desc
#         htR.loc[index - 1, "sector"] = sector
#         htR.loc[index - 1, "symbol"] = symbol
#         htR.loc[index - 1, "token"] = token
#         htR.loc[index - 1, "ltp"] = ltp
#         htR.loc[index - 1, "typ"] = typ
#         break

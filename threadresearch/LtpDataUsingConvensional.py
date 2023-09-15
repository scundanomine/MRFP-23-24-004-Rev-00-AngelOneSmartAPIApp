from pivotalarm.GetSAndR import *
import time
from AngelOneSmartAPIApp.GetAccessToken import *
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait


def getLtpFromConventional():
    startTime = time.perf_counter()
    obj, toc = get_access_token()
    exchange = "NSE"
    mat = getSRData()
    mat["ltp"] = 0
    print(mat)
    print("--- %s seconds ---" % (time.perf_counter() - startTime))
    for index, rows in mat.iterrows():
        uid = rows["id"]
        ltp = obj.ltpData(exchange, rows["symbol"], str(rows["token"]))
        # rows["ltp"] = ltp['data']['ltp']
        mat.loc[uid-1, "ltp"] = ltp['data']['ltp']
    print(mat['ltp'])
    print("--- %s seconds ---" % (time.perf_counter() - startTime))


getLtpFromConventional()

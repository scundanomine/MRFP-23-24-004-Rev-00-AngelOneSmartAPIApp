import time
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from commonudm.GetNiftyDetailedListWithPivots import getNiftyDetailedListWithPivots
from universalanticipatedorderlist.CondenseGSTData import condenseGSTData


def getUniversalList(niftySize=300):
    startTime = time.time()

    # nifty detailed list
    ndf = getNiftyDetailedListWithPivots(niftySize)
    ndf = ndf.loc[:, ['id', 'sector', 'symbol', 'token', 'C']]
    ndf.rename(columns={'C': 'PC'}, inplace=True)
    # print(ndf)

    # dcs and dcs list
    dcs = pd.read_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\traditionalpivotalarm\\pivotstate\\LiveCandleData.csv")
    dcs = dcs.loc[:, ['alarmTimer', 'srT', 'srV', 'nSR']]
    # print(dcs)

    # creation of df three
    dfThree = pd.DataFrame(
        columns=['CC', 'V', 'atr', 'atrPer', 'g', 's', 't', 'bulRP', 'berRP', 'atrV', 'vs', 'roc', 'rsi'])

    # define sub function
    def getULData(uid):
        # time.sleep(0.2)
        symbol = ndf["symbol"][uid]
        return condenseGSTData(uid, symbol)

    with ThreadPoolExecutor() as executor:
        ltc = list(range(niftySize))
        results = executor.map(getULData, ltc)
        ck = 0
        for result in results:
            dfThree.loc[ck] = result
            ck = ck + 1

    # join of three df
    dfm = pd.merge(ndf, dfThree, left_index=True, right_index=True, how='outer')
    dfU = pd.merge(dfm, dcs, left_index=True, right_index=True, how='outer')

    # save the list
    dfU.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\universalanticipatedorderlist\\liststate\\UniversalList.csv",
        index=False)
    print(dfU)

    print(f"execution time is {time.time() - startTime}")


for k in range(1):
    getUniversalList()

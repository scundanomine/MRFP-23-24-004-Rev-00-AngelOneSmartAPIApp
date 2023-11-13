import pandas as pd
import xlwings as xw
import time
from AIlist.GetterAIStateList import getterAIStateList
from AIlist.GetterAndSetterAIList import getterAIList
from universallist.GetterUniversalList import getterUniversalList
from concurrent.futures import ThreadPoolExecutor


def getAIList(niftySize=300):
    startTime = time.time()

    # get current AI list
    aiDf = getterAIList()

    # get the state list
    sDf = getterAIStateList(niftySize)

    # get universal list
    uDf = getterUniversalList()

    # combine state list and universal list
    cUDf = pd.merge(uDf, sDf, left_index=True, right_index=True, how='outer')
    # print(cUDf)

    # updation of AI list
    def updateAIList(r):
        uid = aiDf["id"][r]
        aiDf.iloc[r] = uDf.iloc[uid+1]
    with ThreadPoolExecutor() as executor:
        ltc = list(range(len(aiDf)))
        executor.map(updateAIList, ltc)

    print(f"execution time is {time.time() - startTime}")


getAIList()

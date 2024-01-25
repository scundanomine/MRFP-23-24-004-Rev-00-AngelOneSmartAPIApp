import multiprocessing
import time
from commonudm.GetterPreExitTime import getterPreExitTime
from commonudm.GetterPreReferenceTime import getterPreReferenceTime
from commonudm.GetterStockQtn import getterStockQtn
from commonudm.SetterReferenceDateConstant import setterReferenceDateConstant
from smartwebsocketdata.CleaningAllCandlesDataFromWebSocket import cleaningAllCandlesDataFromWebSocket
from smartwebsocketdata.GetPreTokenWiseCandleData import getPreTokenWiseCandleData
from smartwebsocketdata.SetPartlyAndWholeCandleData import setPartlyAndWholeCandleData
from smartwebsocketdata.SmartApiWebSocketOne import smartApiWebSocketOne
from smartwebsocketdata.SmartApiWebSocketTwo import smartApiWebSocketTwo


def candlesDataAllITREventOne(lock):
    print("Multiprocess One has been started")
    smartApiWebSocketOne(lock)


def candlesDataAllITREventTwo(lock):
    print("Multiprocess two has been started")
    smartApiWebSocketTwo(lock)


def processCandleDataFromWebSocketOne(r, lock):
    print("Multiprocess three has been started")
    setPartlyAndWholeCandleData(r, lock)


def processCandleDataFromWebSocketTwo(r, lock):
    print("Multiprocess four has been started")
    setPartlyAndWholeCandleData(r, lock)


def processCandleDataFromWebSocketThree(r, lock):
    print("Multiprocess five has been started")
    setPartlyAndWholeCandleData(r, lock)


def processCandleDataFromWebSocketFour(r, lock):
    setPartlyAndWholeCandleData(r, lock)


# def eventLoop():
# four multiple process
if __name__ == "__main__":
    startTimeEventLoop = time.time()
    print("Running live for first time")

    # cleaning data for candles
    cleaningAllCandlesDataFromWebSocket(True)

    # getter and setter Pre data
    m = getterStockQtn()

    # setting pre data for candles
    getPreTokenWiseCandleData("tokenwisefreshcandledata", m)
    getPreTokenWiseCandleData("tokenwisepartlycandledata", m)
    getPreTokenWiseCandleData('tokenwisewholecandledata', m)

    # getter pre exit time
    getterPreExitTime()

    getterPreReferenceTime()

    # setter reference time for trading
    setterReferenceDateConstant()

    lockA = multiprocessing.Lock()

    # starting first part 1 process of getting current and future candle data
    pOne = multiprocessing.Process(target=candlesDataAllITREventOne, args=[lockA])

    # starting second process of getting present candles data property
    pTwo = multiprocessing.Process(target=candlesDataAllITREventTwo, args=[lockA])

    # starting Third process of getting pivot alarm
    pThree = multiprocessing.Process(target=processCandleDataFromWebSocketOne, args=[30, lockA])

    # starting Fourth process of getting Universal list
    pFour = multiprocessing.Process(target=processCandleDataFromWebSocketTwo, args=[60, lockA])

    # starting Fifth process of getting AI list
    pFive = multiprocessing.Process(target=processCandleDataFromWebSocketThree, args=[90, lockA])

    # starting sixth process of getting Entry triggered list
    pSix = multiprocessing.Process(target=processCandleDataFromWebSocketFour, args=[120, lockA])

    pOne.start()
    pTwo.start()
    pThree.start()
    pFour.start()
    pFive.start()
    pSix.start()

    pOne.join()
    pTwo.join()
    pThree.join()
    pFour.join()
    pFive.join()
    pSix.join()

    print("Multiprocess have been finished")
    print(f"execution time is {time.time() - startTimeEventLoop}")

# eventLoop()

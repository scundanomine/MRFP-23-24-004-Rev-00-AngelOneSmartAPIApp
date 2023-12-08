import multiprocessing
from commonudm.SetterReferenceDateConstant import setterReferenceDateConstant
from eventloop.EventLoopForFirstITRCandlestickProperties import eventLoopForFirstITRCandlestickProperties
from ohlcdata.GetTestCandlestickData import getTestCandlestickData
from ohlcdata.GetTestFirstItrCandlestickData import getTestFirstItrCandlestickData
import time


# function for PivotAlarm
def pivotAlarmEvent(lock):
    print("Multiprocess One has been started")
    getTestCandlestickData(60, "")


def pivotAlarmEventTwo(lock):
    print("Multiprocess two has been started")
    # getAccessTokenWithThread(200, "ltpTwo.csv", lock)


def ltpDataEventThree(lock):
    print("Multiprocess three has been started")
    # getLtpFromThread(objE)
    # getAccessTokenWithThread(300, "ltpThree.csv", lock)


def readRecordEventFour(lock):
    print("Multiprocess four has been started")
    # getLtpFromThread(objE)
    # getAccessTokenWithThread(400, "ltpFour.csv", lock)


def readRecordEventFive(lock):
    print("Multiprocess five has been started")
    # getLtpFromThread(objE)
    # getAccessTokenWithThread(500, "ltpFive.csv", lock)


def eventLoop():
    startTime = time.time()
    # four multiple process
    if __name__ == "__main__":
        setterReferenceDateConstant()
        getTestFirstItrCandlestickData(60, "")
        eventLoopForFirstITRCandlestickProperties()
        lock = multiprocessing.Lock()
        pOne = multiprocessing.Process(target=pivotAlarmEvent, args=[lock])

        pOne.start()

        pOne.join()

        print("Multiprocess have been finished")
        print(f"execution time is {time.time() - startTime}")


eventLoop()

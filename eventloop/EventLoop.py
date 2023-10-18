from concurrent.futures import ProcessPoolExecutor
import time
from AngelOneSmartAPIApp.GetAccessToken import *
import multiprocessing
from niftytokens_cap_and_filters.GetTraditionalPivotsForSpecificNifty import *
from candlestickdata.CandleStickDataWithThread import *
from threadresearch.LtpDataUsingThreads import *
from eventloop.GetMultipleLtpDataWithMultiProcessing import *


# function for PivotAlarm
def pivotAlarmEvent(lock):
    print("Multiprocess One has been started")
    getAccessTokenWithThread(100, lock)


def pivotAlarmEventTwo(lock):
    print("Multiprocess two has been started")
    getAccessTokenWithThread(200, lock)


def ltpDataEventThree(lock):
    print("Multiprocess three has been started")
    # getLtpFromThread(objE)
    getAccessTokenWithThread(300, lock)


def readRecordEventFour(lock):
    print("Multiprocess four has been started")
    # getLtpFromThread(objE)
    getAccessTokenWithThread(400, lock)


def readRecordEventFive(lock):
    print("Multiprocess five has been started")
    # getLtpFromThread(objE)
    getAccessTokenWithThread(500, lock)


def eventLoop():
    startTime = time.time()
    # four multiple process
    if __name__ == "__main__":
        lock = multiprocessing.Lock()
        pOne = multiprocessing.Process(target=pivotAlarmEvent, args=[lock])
        pTwo = multiprocessing.Process(target=pivotAlarmEventTwo, args=[lock])
        pThree = multiprocessing.Process(target=ltpDataEventThree, args=[lock])
        pFour = multiprocessing.Process(target=readRecordEventFour, args=[lock])
        pFive = multiprocessing.Process(target=readRecordEventFive, args=[lock])
        pOne.start()
        pTwo.start()
        pThree.start()
        pFour.start()
        pFive.start()
        pOne.join()
        pTwo.join()
        pThree.join()
        pFour.join()
        pFive.join()
        print("Multiprocess have been finished")
        print(f"execution time is {time.time() - startTime}")


eventLoop()

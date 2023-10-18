from concurrent.futures import ProcessPoolExecutor
import time
from AngelOneSmartAPIApp.GetAccessToken import *
import multiprocessing
from niftytokens_cap_and_filters.GetTraditionalPivotsForSpecificNifty import *
from candlestickdata.CandleStickDataWithThread import *
from threadresearch.LtpDataUsingThreads import *

objE = []
if __name__ == "__main__":
    # get object for angel one
    while True:
        try:
            objE, accessToken = get_access_token()
            break
        except Exception as e:
            print(f"Not getting accessToken due to {e}")
            time.sleep(1)


# function for PivotAlarm
def pivotAlarmEvent():
    global objE
    print("Multiprocess One has been started")
    getTraditionalPivotsForSpecificNiftyFile("nifty500", "400", objE)


def pivotAlarmEventTwo():
    global objE
    print("Multiprocess two has been started")
    getTraditionalPivotsForSpecificNiftyFile("nifty500", "400", objE)


def ltpDataEventThree():
    global objE
    print("Multiprocess three has been started")
    # getLtpFromThread(objE)
    getTraditionalPivotsForSpecificNiftyFile("nifty500", "500", objE)


def readRecordEventFour():
    global objE
    print("Multiprocess four has been started")
    # getLtpFromThread(objE)
    getTraditionalPivotsForSpecificNiftyFile("nifty500", "400", objE)


def eventLoop():
    global objE

    # four multiple process
    if __name__ == "__main__":
        pOne = multiprocessing.Process(target=pivotAlarmEvent, args=[])
        pTwo = multiprocessing.Process(target=pivotAlarmEventTwo, args=[])
        pThree = multiprocessing.Process(target=ltpDataEventThree, args=[])
        pFour = multiprocessing.Process(target=readRecordEventFour, args=[])
        pOne.start()
        pTwo.start()
        pThree.start()
        pFour.start()
        pOne.join()
        pTwo.join()
        pThree.join()
        pFour.join()
        print("Multiprocess have been finished")


eventLoop()

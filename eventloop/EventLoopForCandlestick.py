from concurrent.futures import ProcessPoolExecutor
import time
from eventloop.GetCandleDataWithMultiProcessing import *


def processForCandleStick(r):
    getCandlestickDataWithMultiProcessing(r, "")


def eventLoopForCandlestick():
    startTimeOne = time.time()
    # four multiple process
    if __name__ == "__main__":
        with ProcessPoolExecutor() as processorC:
            lt = list(range(60, 9 * 60, 60))
            print(lt)
            processorC.map(processForCandleStick, lt)
        print(f"execution time is {time.time() - startTimeOne}")


eventLoopForCandlestick()

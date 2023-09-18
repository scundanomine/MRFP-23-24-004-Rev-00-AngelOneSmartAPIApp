from concurrent.futures import ThreadPoolExecutor
from hotmech.GetHotMechLIst import *
import time

global htRo


def getHotelRoomKey():
    # start_time = time.time()
    global htRo
    htRo = getHotMechList()
    results = []
    keyW = 0

    def getKey(r):
        global htRo
        keyP = 0
        for i in range(r - 10, r):
            if htRo["id"][i] == 0:
                keyP = htRo["slot"][i]
                break
        return keyP

    with ThreadPoolExecutor() as executor:
        lt = list(range(10, 110, 10))
        # print(lt)
        results = executor.map(getKey, lt)
        for result in results:
            if result != 0:
                keyW = result
                break
    # print("--- %s seconds ---" % (time.time() - start_time))
    return keyW


# print(getHotelRoomKey())

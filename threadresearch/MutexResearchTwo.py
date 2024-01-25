import multiprocessing
import time
import pandas as pd


def processOne(lock, startTime):
    # print("Multiprocess one has been started")
    for i in range(60):
        # with lock:
        time.sleep(1)
        # print('I have waited for process one!!!!!!!!!')
        # df = pd.DataFrame([[0, 0, 0], [0, 0, 0]])
        # df.to_csv('E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\threadresearch\\mat2.csv', index=False)
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\threadresearch\\mat2.csv")
        print(f"time of execution for processOne!!!!!!!!! is {time.time() - startTime}")


def processTwo(lock, startTime):
    # print("Multiprocess two has been started")
    for i in range(60):
        # with lock:
        time.sleep(1)
        # print('I have waited for process two@@@@@@@@@@@@@@@@')
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\threadresearch\\mat2.csv")
        # while True:
        #     try:
        #         df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\threadresearch\\mat2.csv")
        #         break
        #     except Exception as e:
        #         print(f"Exception while getting df is +++++++++++++++++++++++++++++++++++ {e}")
        print(f"time of execution for processTwo@@@@@@@ is {time.time()-startTime}")


def processThree(lock, startTime):
    # print("Multiprocess three has been started")
    for i in range(60):
        # with lock:
        time.sleep(1)
        # print('I have waited for process three############')
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\threadresearch\\mat2.csv")
        # df = pd.DataFrame([[2, 2, 2], [2, 2, 2]])
        # df.to_csv('E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\threadresearch\\mat2.csv',
        #           index=False)
        print(f"time of execution for processThree######## is {time.time() - startTime}")


# four multiple process
if __name__ == "__main__":
    lockA = multiprocessing.Lock()
    startT = time.time()

    # starting first part 1 process of getting current and future candle data
    pOne = multiprocessing.Process(target=processOne, args=[lockA, startT])

    # starting first part 2 process of getting current and future candle data
    pTwo = multiprocessing.Process(target=processTwo, args=[lockA, startT])

    # starting second process of getting present candles data property
    pThree = multiprocessing.Process(target=processThree, args=[lockA, startT])

    pOne.start()
    pTwo.start()
    pThree.start()

    pOne.join()
    pTwo.join()
    pThree.join()

    print("Multiprocess have been finished")

# eventLoop()

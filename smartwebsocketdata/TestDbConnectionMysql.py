import time
import pymysql as mq
from commonudm.GetSymbolAndToken import getSymbolAndToken


def testDbConnection():
    startTime = time.time()
    myObj = mq.connect(host='localhost', user='root', password='', database='securitydb')
    print(myObj)
    c = myObj.cursor()
    tDf = getSymbolAndToken()
    # lst = tDf.values.tolist()
    print(tDf)
    tbl = 'mongodb'
    q = "CREATE TABLE `sam` (`SNo` INT, `time` VARCHAR(50))"
    c.execute(q)
    # for index, row in tDf.iterrows():
    #     c.execute(
    #         f"CREATE TABLE IF NOT EXISTS sam (SNo INT AUTO_INCREMENT, time VARCHAR, ltp FLOAT, volume FLOAT, PRIMARY KEY (SNo))")
    print(f"The time of execution is {time.time() - startTime}")


testDbConnection()

import sqlite3
import time
from commonudm.GetSymbolAndToken import getSymbolAndToken


def testDbConnection():
    startTime = time.time()
    db = sqlite3.connect('realtime.db', check_same_thread=False)
    c = db.cursor()
    tDf = getSymbolAndToken()
    tDf = tDf.drop(labels=range(40, len(tDf)), axis=0)
    # print(tDf)
    for index, row in tDf.iterrows():
        c.execute(
            '''CREATE TABLE IF NOT EXISTS {}(time datetime, cT VARCHAR(70), ltp FLOAT, volume FLOAT)'''.format(f"`{row['token']}`"))
        db.commit()
        # except:
        #     break
    db.close()
    print(f"The time of execution is {time.time() - startTime}")


testDbConnection()

import time

import pandas as pd

from entrytriggeredlist.GetterEntryTriggeredList import getterEntryTriggeredList


def getStackedETList():
    try:
        df = getterEntryTriggeredList()
        df['srV'] = time.time() - df['srT']
        df = df.sort_values(by='srV')
    except:
        # print(f"The exception while getterEntryList is {e}")
        df = getStackedETList()
    return df


# getterEntryList()

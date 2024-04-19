import time

import pandas as pd

from entrytriggeredlist.GetterEntryTriggeredList import getterEntryTriggeredList


def getStackedETList():
    try:
        df = getterEntryTriggeredList()
        if len(df) != 0:
            df['srV'] = time.time() - df['srT']
            df = df.sort_values(by='srV')
    except Exception as e:
        print(f"The exception while getStackedETList is {e}")
        df = getStackedETList()
    return df


# getterEntryList()

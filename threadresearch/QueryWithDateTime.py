import datetime
from commonudm.GetterPreReferenceTime import getterPreReferenceTime
from commonudm.GetterTimeDelta import getterTimeDelta
from commonudm.SetterReferenceDateConstant import setterReferenceDateConstant
import time
import pandas as pd


def queryWithDateTime(fromDate="", toDate="", uid=""):
    # getterPreExitTime()
    getterPreReferenceTime()
    # setter reference time for trading
    setterReferenceDateConstant()
    cv = getterTimeDelta()
    startTime = time.time()
    df = pd.read_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\threadresearch\\mat.csv")
    df = df.set_index('time')
    df.index = pd.to_datetime(df.index)
    ct = datetime.datetime.now() - cv
    ct = ct.strftime("%Y-%m-%d %H:%M")
    pt = datetime.datetime.now() - cv - datetime.timedelta(minutes=9)
    pt = pt.strftime("%Y-%m-%d %H:%M")
    print(df.loc[pt:ct].to_dict('records'))
    print(time.time() - startTime)


queryWithDateTime()

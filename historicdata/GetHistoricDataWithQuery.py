import datetime
from commonudm.GetterPreReferenceTime import getterPreReferenceTime
from commonudm.GetterTimeDelta import getterTimeDelta
from commonudm.SetterReferenceDateConstant import setterReferenceDateConstant
import time
import pandas as pd

from historicdata.GetterSpecificHistoricData import getterSpecificHistoricData


def getHistoricDataWithQuery(fromDate, toDate, uid, date):
    df = getterSpecificHistoricData(date, uid)
    fromDate = fromDate.strftime("%Y-%m-%d %H:%M")
    toDate = toDate.strftime("%Y-%m-%d %H:%M")
    return df.loc[fromDate:toDate].to_dict('records')
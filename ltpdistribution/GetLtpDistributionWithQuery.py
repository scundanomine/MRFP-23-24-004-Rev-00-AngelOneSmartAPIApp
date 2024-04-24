import datetime
from commonudm.GetterPreReferenceTime import getterPreReferenceTime
from commonudm.GetterTimeDelta import getterTimeDelta
from commonudm.SetterReferenceDateConstant import setterReferenceDateConstant
import time
import pandas as pd

from historicdata.GetterSpecificHistoricData import getterSpecificHistoricData
from ltpdistribution.GetterSpecificLtpDistributionWithTimeIndex import getterSpecificLtpDistributionWithTimeIndex


def getLtpDistributionWithQuery(fromDate, toDate, uid, date):
    df = getterSpecificLtpDistributionWithTimeIndex(date, uid)
    fromDate = fromDate.strftime("%Y-%m-%d %H:%M")
    toDate = toDate.strftime("%Y-%m-%d %H:%M")
    return df.loc[fromDate:toDate]
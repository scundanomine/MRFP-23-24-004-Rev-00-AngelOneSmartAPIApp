import datetime
import xlwings as xw
from commonudm.GetterPreReferenceTime import getterPreReferenceTime
from commonudm.GetterReferenceTime import getterReferenceTime


def setterReferenceDateConstant():
    getterPreReferenceTime()
    dateR = getterReferenceTime()
    refDate = datetime.datetime.strptime(dateR, "%d %b %Y %H:%M:%S.%f")
    c = datetime.datetime.now() - refDate
    # setter to excell and df
    wb = xw.Book("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
    # MAndP is margin and portfolio list
    dt = wb.sheets("MAndP")
    dt.range("i2:i2").value = str(c)


# setterReferenceDateConstant()

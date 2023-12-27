import pandas as pd
import multiprocessing
import xlwings as xw


def setterPrePositionList(lock=multiprocessing.Lock()):
    # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
    # mr is margin required, lp is limit price, q is the quantity, sl is the stop loss
    # gol is gain or loss, tOEP is reference time of entry placed, tOP is time of position taken and tOEx is time of exit
    df = pd.DataFrame(columns=['id', 'sector', 'symbol', 'token', "ot", "ltp", "lp", "q", "sl", "target", "mr", "po", "slo", "to", "gol", "tOEP", "tOP", "tOEx", 'ltpP', 'eFlag', 'rFlag'])
    lock.acquire()
    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv",
        index=False)
    lock.release()
    # getting data from the sheet
    wb = xw.Book("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
    dt = wb.sheets("Position")

    n = len(df)
    # clear the sheet
    lock.acquire()
    dt.range(f"a2:u{n + 100}").clear_contents()
    lock.release()
    return df


# setterPrePositionList()

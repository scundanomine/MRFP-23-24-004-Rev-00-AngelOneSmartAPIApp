import pandas as pd
import xlwings as xw


def getterPositionList(lock):
    # getting data from the sheet
    wb = xw.Book("../AngelOneSmartAPIApp/TA_Python.xlsm")
    dt = wb.sheets("Position")
    try:
        lock.acquire()
        dfC = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv")
        lock.release()
        n = len(dfC)
        df = pd.DataFrame(dt.range(f"a1:u{n+2}").value)
        df.columns = df.iloc[0]
        df = df[1:]
        df.drop(n)
    except Exception as e:
        print(f"The exception while getter Entry list is {e}")
        # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
        # mr is margin required, lp is limit price, q is the quantity, sl is the stop loss
        # gol is gain or loss, tOEP is reference time of entry placed, tOP is time of position taken and tOEx is time of exit
        df = pd.DataFrame(columns=['id', 'sector', 'symbol', 'token', "ot", "ltp", "lp", "q", "sl", "target", "mr", "po", "slo", "to", "gol", "tOEP", "tOP", "tOEx", 'ltpP', 'eFlag', 'rFlag'])
        dt.range(f"a1:u1").options(pd.DataFrame, index=False).value = df
        lock.acquire()
        df.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv",
            index=False)
        lock.release()
    return df


print(getterPositionList())

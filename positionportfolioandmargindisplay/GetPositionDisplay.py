import pandas as pd
import xlwings as xw
import multiprocessing


def getPositionDisplay(lock=multiprocessing.Lock()):
    while True:
        try:
            # getting data from the sheet
            wb = xw.Book(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            dt = wb.sheets("MAndP")
            lock.acquire()
            dfC = pd.read_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv")
            lock.release()
            dfCL = dfC.values.tolist()
            m = len(dfC)
            i = 6
            for index, row in dfC.iterrows():
                lock.acquire()
                uidEx = dt[f"A{i}"].value
                lock.release()
                if uidEx == row['id']:
                    lock.acquire()
                    dt[f"f{i}"].value = row['ltp']
                    dt[f"o{i}"].value = row['gol']
                    dt[f"t{i}"].value = row['eFlag']
                    dt[f"u{i}"].value = row['rFlag']
                    lock.release()
                elif uidEx is None:
                    lock.acquire()
                    dt.range(f"a{i}:u{i}").value = dfCL[index]
                    dt.range(f"a{i + 1}:u{i + 4}").clear_contents()
                    lock.release()
                else:
                    lock.acquire()
                    dt.range(f"a6:u{6 + m + 4}").clear_contents()
                    dt.range(f"a5:u{5 + m + 1}").options(pd.DataFrame, index=False).value = dfC
                    lock.release()
                    break
                i = i + 1
            break
        except Exception as e:
            print(f"The exception while getPositionDisplay is {e}")


# getPositionDisplay()

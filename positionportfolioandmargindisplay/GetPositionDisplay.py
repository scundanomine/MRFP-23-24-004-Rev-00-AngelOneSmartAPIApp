import pandas as pd
import xlwings as xw
import multiprocessing


def getPositionDisplay(lock=multiprocessing.Lock()):
    while True:
        try:
            with lock:
                # getting data from the sheet
                wb = xw.Book(
                    "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AngelOneSmartAPIApp\\TA_Python.xlsm")
                dt = wb.sheets("MAndP")
                dfC = pd.read_csv(
                    "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv")
            dfCL = dfC.values.tolist()
            m = len(dfC)
            with lock:
                dt.range(f"a{6+m}:v{6 + m + 20}").clear_contents()
            i = 6
            for index, row in dfC.iterrows():
                with lock:
                    uidEx = dt[f"A{i}"].value
                if uidEx == row['id']:
                    with lock:
                        dt[f"f{i}"].value = row['ltp']
                        dt[f"o{i}"].value = row['gol']
                        dt[f"t{i}"].value = row['rFlag']
                        dt[f"u{i}"].value = row['eFlag']
                elif uidEx is None:
                    with lock:
                        dt.range(f"a{i}:v{i}").value = dfCL[index]
                else:
                    with lock:
                        dt.range(f"a5:v{5 + m + 1}").options(pd.DataFrame, index=False).value = dfC
                    break
                i = i + 1
            break
        except Exception as e:
            print(f"The exception while getPositionDisplay is {e}")


# getPositionDisplay()

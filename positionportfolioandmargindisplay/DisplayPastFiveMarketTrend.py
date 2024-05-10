import pandas as pd
import xlwings as xw


def displayPastFiveMarketTrend(df=pd.DataFrame()):
    while True:
        try:
            # getting data from the sheet
            wb = xw.Book(
                "F:\\AT\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            dt = wb.sheets("MAndP")
            # df = getterMarketStructureDf()

            dt["A3"].value = df.loc[5, 'mTyp']
            dt["B3"].value = df.loc[6, 'mTyp']
            dt["C3"].value = df.loc[7, 'mTyp']
            dt["D3"].value = df.loc[8, 'mTyp']
            dt["E3"].value = df.loc[9, 'mTyp']
            break
        except Exception as e:
            print(f"The exception while getPositionDisplay is {e}")


# cvp = getterTimeDelta()
# displayPastFiveMarketTrend(cvp)

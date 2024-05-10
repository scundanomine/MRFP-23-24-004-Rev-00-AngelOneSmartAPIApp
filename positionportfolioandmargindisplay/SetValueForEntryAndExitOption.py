import xlwings as xw


def setValueForEntryAndExitOption(optionEntry="Default", optionExit="Default", warningMsg=""):
    while True:
        try:
            wb = xw.Book(
                "F:\\AT\\AngelOneSmartAPIApp\\TA_Python.xlsm")
            # MAndP is margin and portfolio list
            dt = wb.sheets("MAndP")
            # creating the df
            # dt.range("a1:a2").options(pd.DataFrame, index=False).value = df
            # dt['N2'].value = optionEntry
            # dt['P2'].value = optionExit
            dt['I3'].value = warningMsg
            break
        except Exception as e:
            print(f"Exception while setValueForEntryAndExitOption is {e}")


# setValueForEntryAndExitOption("All", "All")

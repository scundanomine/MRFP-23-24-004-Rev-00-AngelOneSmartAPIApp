import pandas as pd


def getterPositionList():
    try:
        df = pd.read_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv")
    except Exception as e:
        print(f"The exception while getter Entry list is {e}")
        # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
        # mr is margin required, lp is limit price, q is the quantity, sl is the stop loss
        # gol is gain or loss, tOEP is reference time of entry placed, tOP is time of position taken and tOEx is time of exit
        df = pd.DataFrame(columns=["id", "ot", "ltp", "lp", "q", "sl", "target", "mr", "po", "slo", "to", "gol", "tOEP", "tOP", "tOEx"])
        df.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\position\\positionstate\\PositionList.csv",
            index=False)
    return df


getterPositionList()

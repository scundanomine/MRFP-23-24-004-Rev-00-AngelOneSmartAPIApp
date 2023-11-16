import pandas as pd


def getterAIList():
    while True:
        try:
            aiDf = pd.read_csv(
                "/entrytriggeredlist\\AIstate\\AIList.csv")
            break
        except Exception as e:
            print(f"Exception while getting AI list is {e}")
            aiDf = pd.DataFrame(
                columns=['id', 'sector', 'symbol', 'token', 'PC', 'CC', 'V', 'atr', 'atrPer', 'g', 's', 't', 'bulRP',
                         'berRP', 'atrV', 'vs', 'roc', 'rsi', 'alarmTimer', 'srT', 'srV', 'nSR', 'GL'])
            aiDf.to_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlist\\AIstate\\AIList.csv",
                index=False)
    return aiDf

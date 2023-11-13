import pandas as pd


def getterAIStateList(niftySize):
    while True:
        try:
            sDf = pd.read_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlist\\AIstate\\AIStateList.csv")
            break
        except Exception as e:
            print(f"Exception while getting AI list is {e}")
            sDf = pd.DataFrame(index=list(range(niftySize)), columns=['AIFlag'])
            sDf['AIFlag'] = False
            sDf.to_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlist\\AIstate\\AIStateList.csv",
                index=False)
    return sDf

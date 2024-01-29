import pandas as pd


def getterDfFromSpecificRRState(source, pid):
    try:
        df = pd.read_csv(
                f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\{source}\\{pid}.csv")
    except Exception as e:
        print(f"Exception while getterDfFromSpecificRRState is {e}")
        df = pd.DataFrame()
    return df


# print(getterPECBListRR())
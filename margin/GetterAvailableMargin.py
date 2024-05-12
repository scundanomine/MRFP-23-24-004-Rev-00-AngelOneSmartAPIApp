import pandas as pd


def getterAvailableMargin():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\margin\\marginstate\\margin.csv")
    except Exception as e:
        print(f"The exception while getterAvailableMargin is {e}")
        df = getterAvailableMargin()
    # return df['margin'][0]
    return df


# print(getterAvailableMargin())

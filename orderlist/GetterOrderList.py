import pandas as pd


def getterOrderList():
    try:
        df = pd.read_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\orderlist\\olstate\\OrderList.csv")
    except Exception as e:
        print(f"The exception while getter Order list is {e}")
        df = pd.DataFrame(columns=['id', 'ol'])
        df.to_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\orderlist\\olstate\\OrderList.csv",
            index=False)
    return df

import pandas as pd


def getterUpdateAndSetterFixedPortfolio(gol, lock):
    try:
        lock.acquire()
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\portfolio\\portfoliostate\\FixedPortfolio.csv")
        lock.release()
        df.loc[0, 'portfolio'] = df.loc[0, 'portfolio'] + gol
        lock.acquire()
        df.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\portfolio\\portfoliostate\\FixedPortfolio.csv", index=False)
        lock.release()
    except Exception as e:
        print(f"The exception while getterUpdateAndSetterFixedPortfolio is {e}")



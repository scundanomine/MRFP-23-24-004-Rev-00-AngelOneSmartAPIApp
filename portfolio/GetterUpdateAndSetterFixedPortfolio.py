import pandas as pd


def getterUpdateAndSetterFixedPortfolio(gol, lock):
    with lock:
        try:
            df = pd.read_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\portfolio\\portfoliostate\\FixedPortfolio.csv")
            df.loc[0, 'portfolio'] = df.loc[0, 'portfolio'] + gol
            df.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\portfolio\\portfoliostate\\FixedPortfolio.csv", index=False)
        except Exception as e:
            print(f"The exception while getterUpdateAndSetterFixedPortfolio is {e}")
            getterUpdateAndSetterFixedPortfolio(gol, lock)



import pandas as pd


def getterUpdateAndSetterFixedPortfolioWithExpenses(mr, lock):
    with lock:
        try:
            df = pd.read_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\portfolio\\portfoliostate\\FixedPortfolio.csv")
            df.loc[0, 'portfolio'] = df.loc[0, 'portfolio'] - 88 / 50000 * mr
            df.to_csv(
                "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\portfolio\\portfoliostate\\FixedPortfolio.csv",
                index=False)
        except Exception as e:
            print(f"The exception while getterUpdateAndSetterFixedPortfolioWithExpenses is {e}")
            getterUpdateAndSetterFixedPortfolioWithExpenses(mr, lock)

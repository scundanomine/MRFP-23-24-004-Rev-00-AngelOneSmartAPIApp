import pandas as pd


def getterUpdateAndSetterFixedPortfolioWithExpenses(mr, lock):
    with lock:
        try:
            df = pd.read_csv(
                "F:\\AT\\portfolio\\portfoliostate\\FixedPortfolio.csv")
            df.loc[0, 'portfolio'] = df.loc[0, 'portfolio'] - 90 / 50000 * mr
            df.to_csv(
                "F:\\AT\\portfolio\\portfoliostate\\FixedPortfolio.csv",
                index=False)
        except Exception as e:
            print(f"The exception while getterUpdateAndSetterFixedPortfolioWithExpenses is {e}")
            getterUpdateAndSetterFixedPortfolioWithExpenses(mr, lock)

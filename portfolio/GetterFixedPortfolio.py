import pandas as pd
from portfolio.GetterPrePortfolio import getterPreFixedPortfolio


def GetterFixedPortfolio():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\portfolio\\portfoliostate\\portfolio.csv")
    except Exception as e:
        print(f"The exception while getter portfolio is {e}")
        # top is time of order placed, po is primary order, sl is stop loss order and to is target order and their values are open, executed, canceled or none.
        df = getterPreFixedPortfolio()
    # return df['margin'][0]
    return df


# print(getterAvailableMargin())

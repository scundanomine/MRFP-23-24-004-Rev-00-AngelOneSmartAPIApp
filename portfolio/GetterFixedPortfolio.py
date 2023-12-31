import pandas as pd
from portfolio.GetterPreFixedPortfolio import getterPreFixedPortfolio


def getterFixedPortfolio(lock):
    try:
        lock.acquire()
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\portfolio\\portfoliostate\\FixedPortfolio.csv")
        lock.release()
    except Exception as e:
        print(f"The exception while getter getterFixedPortfolio is {e}")
        df = getterPreFixedPortfolio()
    # return df['margin'][0]
    return df


# print(getterAvailableMargin())

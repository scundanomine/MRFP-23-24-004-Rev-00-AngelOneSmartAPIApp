import pandas as pd


def getterFixedPortfolio():
    try:
        df = pd.read_csv(
            "F:\\AT\\portfolio\\portfoliostate\\FixedPortfolio.csv")
    except Exception as e:
        print(f"The exception while getter getterFixedPortfolio is {e}")
        df = getterFixedPortfolio()
    # return df['margin'][0]
    return df


# print(getterAvailableMargin())

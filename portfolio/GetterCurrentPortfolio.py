import pandas as pd


def getterCurrentPortfolio():
    try:
        df = pd.read_csv(
            "F:\\AT\\portfolio\\portfoliostate\\CurrentPortfolio.csv")
    except Exception as e:
        print(f"The exception while getter getterCurrentPortfolio is {e}")
        df = getterCurrentPortfolio()
    # return df['margin'][0]
    return df.loc[0, 'portfolio']


# print(getterAvailableMargin())

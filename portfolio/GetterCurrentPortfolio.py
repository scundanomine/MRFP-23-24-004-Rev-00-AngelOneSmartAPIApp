import pandas as pd


def getterCurrentPortfolio():
    try:
        df = pd.read_csv(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\portfolio\\portfoliostate\\CurrentPortfolio.csv")
    except Exception as e:
        print(f"The exception while getter getterCurrentPortfolio is {e}")
        df = getterCurrentPortfolio()
    # return df['margin'][0]
    return df.loc[0, 'portfolio']


# print(getterAvailableMargin())

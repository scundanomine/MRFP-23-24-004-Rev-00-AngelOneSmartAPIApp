import pandas as pd


def getSampleDistributionDf():
    df = pd.DataFrame(columns=['time'])
    new_cols = range(60)
    df[:] = 0
    # cols_to_add = [col for col in new_cols if col not in sdf.columns]
    df.loc[:, new_cols] = 0
    df = df.set_index('time')
    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ltpdistribution\\ltpdistributionstate\\SDDf.csv")


# getSampleDistributionDf()

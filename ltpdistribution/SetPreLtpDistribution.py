from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList
from ltpdistribution.GetterSampleDistributionDf import getterSampleDistributionDf


def setPreLtpDistribution():
    gDf = getterRequiredSymbolAndTokenList()
    df = getterSampleDistributionDf()
    for index, row in gDf.iterrows():
        uid = row['id']
        df.to_csv(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\ltpdistribution\\ltpdistributionstate\\specificdistributiondf\\{uid}.csv",
            index=False)


setPreLtpDistribution()

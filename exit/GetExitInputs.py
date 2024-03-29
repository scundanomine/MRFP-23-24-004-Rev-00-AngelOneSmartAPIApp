from exit.GetCustomDfExitInputs import getCustomDfExitInputs
from exit.GetterExitInputs import getterExitInputs


def getExitInputs():
    # get custom black list dataframe
    df = getCustomDfExitInputs()

    # getter black list
    eIDf = getterExitInputs()

    for index, row in df.iterrows():
        if row["rFlag"] == 1 or row["eFlag"] == 1:
            eIDf.iloc[index] = row
    eIDf.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\exit\\exitstate\\ExitInputs.csv",
        index=False)
    return eIDf
    # print(eIDf)


# getCustomDfExitInputs()

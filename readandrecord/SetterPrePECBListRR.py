import pandas as pd
import multiprocessing

from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList


def setterPrePECBListRR():
    # flag for entry calculation
    df = pd.DataFrame(columns=['pid', 'flagCP', 'flagCE'])
    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\PECBList.csv",
        index=False)
    return df


# print(setterPrePECBListRR())

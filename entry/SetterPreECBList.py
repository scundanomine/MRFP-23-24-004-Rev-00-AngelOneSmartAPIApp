from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList


def setterPreECBList():
    df = getterRequiredSymbolAndTokenList()
    df = df.loc[:, ['id']]
    # flag for entry calculation
    df['eCBFlag'] = 0
    df = df.astype("int64")
    df.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entry\\entrystate\\ECBList.csv",
        index=False)
    return df


# print(setterPreECBList())

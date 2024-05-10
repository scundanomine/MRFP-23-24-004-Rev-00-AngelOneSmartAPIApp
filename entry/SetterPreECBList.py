from commonudm.GetterRequiredSymbolAndTokenList import getterRequiredSymbolAndTokenList


def setterPreECBList():
    df = getterRequiredSymbolAndTokenList()
    df = df.loc[:, ['id']]
    # flag for entry calculation
    df['eCBFlag'] = 0
    df = df.astype("int64")
    df.to_csv(
        "F:\\AT\\entry\\entrystate\\ECBList.csv",
        index=False)
    return df


# print(setterPreECBList())

from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData


def setterPreMarketStructureDf():
    df = getterSpecificCandleData(120, "Nifty 50")
    new_cols = ['emaOne', 'emaTwo', 'QOne', 'QTwo', 'QQOne', 'QQTwo', 'mTyp', 'st', 'trT']
    cols_to_add = [col for col in new_cols if col not in df.columns]
    df.loc[:, cols_to_add] = 0
    df.to_csv(
        f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\marketstructure\\marketstate\\MarketStructure.csv",
        index=False)


# setterPreMarketStructureDf()

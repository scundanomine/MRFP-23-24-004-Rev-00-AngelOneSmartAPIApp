from candlestickdata.GetterSpecificCandleData import getterSpecificCandleData


def setterPreMarketStructureDf():
    df = getterSpecificCandleData(120, "Nifty 100")
    new_cols = ['emaOne', 'emaTwo', 'QOne', 'QTwo', 'QQOne', 'QQTwo', 'mTyp', 'st', 'trT']
    cols_to_add = [col for col in new_cols if col not in df.columns]
    df.loc[:, cols_to_add] = 0
    df.to_csv(
        f"F:\\AT\\marketstructure\\marketstate\\MarketStructure.csv",
        index=False)


# setterPreMarketStructureDf()

def getBullishReversalCandlestickPatternWithoutThreading(tdf):
    tdf["bulRP"] = "none"
    for r in range(10):
        # condition for double candlestick pattern
        if tdf.loc[r, "t"] == "hammer" and tdf.loc[r, 's'] >= 0.75:
            tdf.loc[r, "bulRP"] = "hammer"
        # condition for double candlestick pattern
        elif r != 0:
            if tdf.loc[r-1, "g"] == "red" and tdf.loc[r, "g"] == "green" and tdf.loc[r, 's'] >= 0.75:
                # condition for tweezer bottom
                # if tdf.loc[r-1, "t"] == "tweezer_b" and tdf.loc[r, "t"] == "tweezer_b" and tdf.loc[r-1, "C"] - tdf.loc[r, "O"] <= 0.25*tdf.loc[r, "atr"]:
                #     tdf.loc[r, "bulRP"] = "tweezer_bottom"
                # # condition for Piercing Pattern
                # elif tdf.loc[r-1, "O"] > tdf.loc[r, "C"] and tdf.loc[r-1, "C"] - tdf.loc[r, "O"] <= 0.25*tdf.loc[r, "atr"]:
                #     tdf.loc[r, "bulRP"] = "Piercing"
                # condition for Bullish Engulfing Pattern
                if tdf.loc[r-1, "O"] < tdf.loc[r, "C"] and tdf.loc[r-1, "C"] - tdf.loc[r, "O"] <= tdf.loc[r, "atr"]:
                    tdf.loc[r, "bulRP"] = "Bullish_Engulfing"
            elif r != 9 and tdf.loc[r+1, 's'] >= 0.75:
                if tdf.loc[r - 1, "g"] == "red" and tdf.loc[r, "t"] == "doji" and tdf.loc[r + 1, "g"] == "green":
                    tdf.loc[r, "bulRP"] = "morning_star"
    return tdf


# GetBullishReversalCandlestickPatternWithoutThreading()

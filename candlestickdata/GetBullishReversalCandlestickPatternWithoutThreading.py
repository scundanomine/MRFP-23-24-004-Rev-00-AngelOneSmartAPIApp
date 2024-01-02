def getBullishReversalCandlestickPatternWithoutThreading(tdf):
    tdf["bulRP"] = "none"
    for r, row in tdf.iterrows():
        # condition for double candlestick pattern
        if tdf["t"][r] == "hammer":
            tdf.loc[r, "bulRP"] = "hammer"
        # condition for double candlestick pattern
        elif r != 0:
            if tdf["g"][r - 1] == "red" and tdf["g"][r] == "green":
                # condition for tweezer bottom
                if tdf["t"][r - 1] == "tweezer_b" and tdf["t"][r] == "tweezer_b" and tdf["C"][r-1] - tdf["O"][r] <= 0.25*tdf["atr"][r]:
                    tdf.loc[r, "bulRP"] = "tweezer_bottom"
                # condition for Piercing Pattern
                elif tdf["O"][r - 1] > tdf["C"][r] and tdf["C"][r-1] - tdf["O"][r] <= 0.25*tdf["atr"][r]:
                    tdf.loc[r, "bulRP"] = "Piercing"
                    # condition for Bullish Engulfing Pattern
                elif tdf["O"][r - 1] < tdf["C"][r] and tdf["C"][r-1] - tdf["O"][r] <= 0.25*tdf["atr"][r]:
                    tdf.loc[r, "bulRP"] = "Bullish_Engulfing"
            elif r != 9:
                if tdf["g"][r-1] == "red" and tdf["t"][r] == "doji" and tdf["g"][r+1] == "green":
                    tdf.loc[r, "bulRP"] = "morning_star"
    return tdf


# GetBullishReversalCandlestickPatternWithoutThreading()

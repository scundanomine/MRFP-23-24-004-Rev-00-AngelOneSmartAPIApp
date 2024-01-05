def getBearishReversalCandlestickPatternWithoutThreading(tdf):
    tdf["berRP"] = "none"
    for r in range(10):
        # condition for double candlestick pattern
        if tdf["t"][r] == "shooting_star" and tdf.loc[r, 's'] >= 0.5:
            tdf.loc[r, "berRP"] = "shooting_star"
        # condition for double candlestick pattern
        elif r != 0:
            if tdf.loc[r - 1, "g"] == "green" and tdf.loc[r, "g"] == "red" and tdf.loc[r, 's'] >= 0.5:
                # condition for tweezer bottom
                if tdf.loc[r - 1, "t"] == "tweezer_t" and tdf.loc[r, "t"] == "tweezer_t" and (tdf.loc[r, "O"] - tdf.loc[r - 1, "C"]) <= 0.25 * tdf.loc[r, "atr"]:
                    tdf.loc[r, "berRP"] = "tweezer_top"
                # condition for Dark Cloud Cover Pattern
                elif tdf.loc[r - 1, "O"] < tdf.loc[r, "C"] and (tdf.loc[r, "O"] - tdf.loc[r - 1, "C"]) <= 0.25 * tdf.loc[r, "atr"]:
                    tdf.loc[r, "berRP"] = "dark_cloud_cover"
                    # condition for Bearish Engulfing Pattern
                elif tdf.loc[r - 1, "O"] > tdf.loc[r, "C"] and (tdf.loc[r, "O"] - tdf.loc[r - 1, "C"]) <= 0.25 * tdf.loc[r, "atr"]:
                    tdf.loc[r, "berRP"] = "Bearish_Engulfing"
            if r != 9 and  tdf.loc[r+1, 's'] >= 0.5:
                if tdf.loc[r - 1, "g"] == "green" and tdf.loc[r, "t"] == "doji" and tdf.loc[r + 1, "g"] == "red":
                    tdf.loc[r, "berRP"] = "evening_star"
    return tdf


# getBearishReversalCandlestickPatternWithoutThreading()

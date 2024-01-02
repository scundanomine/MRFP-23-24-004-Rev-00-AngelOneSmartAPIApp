def getAllItrBearishReversalCandlestickPatternWithoutThreading(tdg):
    for r in range(8, 10):
        # condition for double candlestick pattern
        if tdg["t"][r] == "shooting_star":
            tdg.loc[r, "berRP"] = "shooting_star"
        # condition for double candlestick pattern
        elif tdg["g"][r - 1] == "green" and tdg["g"][r] == "red":
            # condition for tweezer bottom
            if tdg["t"][r - 1] == "tweezer_t" and tdg["t"][r] == "tweezer_t" and (tdg["O"][r]-tdg["C"][r-1]) <= 0.25*tdg["atr"][r]:
                tdg.loc[r, "berRP"] = "tweezer_top"
            # condition for Dark Cloud Cover Pattern
            elif tdg["O"][r - 1] < tdg["C"][r] and (tdg["O"][r]-tdg["C"][r-1]) <= 0.25*tdg["atr"][r]:
                tdg.loc[r, "berRP"] = "dark_cloud_cover"
                # condition for Bearish Engulfing Pattern
            elif tdg["O"][r - 1] > tdg["C"][r] and (tdg["O"][r]-tdg["C"][r-1]) <= 0.25*tdg["atr"][r]:
                tdg.loc[r, "berRP"] = "Bearish_Engulfing"
        # condition for triple candlestick pattern
        elif r != 9:
            if tdg["g"][r - 1] == "green" and tdg["t"][r] == "doji" and tdg["g"][r + 1] == "red":
                tdg.loc[r, "berRP"] = "evening_star"
    return tdg


# getAllItrBearishReversalCandlestickPatternWithoutThreading()

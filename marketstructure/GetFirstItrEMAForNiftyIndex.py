from marketstructure.GetterMarketStructureDf import getterMarketStructureDf


def getFirstItrEMAForNiftyIndex():
    cdf = getterMarketStructureDf()
    # calculation for EMAs
    for index, row in cdf.iterrows():
        # EMAs are same for all candles
        if index < 5:
            sumA = 0
            ctr = 0
            for i in range(index + 1):
                if cdf.loc[i, 'C'] != 0:
                    sumA = sumA + cdf.loc[i, 'C']
                    ctr = ctr + 1
            if ctr != 0:
                avgA = sumA / ctr
                cdf.loc[index, 'emaOne'] = avgA
                cdf.loc[index, 'emaTwo'] = avgA

        # ema One and two are not same
        else:
            # emaOne calculation
            sumA = 0
            ctr = 0
            for i in range(index + 1 - 5, index + 1):
                if cdf.loc[i, 'C'] != 0:
                    sumA = sumA + cdf.loc[i, 'C']
                    ctr = ctr + 1
            if ctr != 0:
                avgA = sumA / ctr
                cdf.loc[index, 'emaOne'] = avgA
            # emaTow calculation
            if index == 9:
                sumA = 0
                ctr = 0
                for i in range(index + 1 - 9, index + 1):
                    if cdf.loc[i, 'C'] != 0:
                        sumA = sumA + cdf.loc[i, 'C']
                        ctr = ctr + 1
                if ctr != 0:
                    avgA = sumA / ctr
                    cdf.loc[index, 'emaTwo'] = avgA
            else:
                sumA = 0
                ctr = 0
                for i in range(index + 1):
                    if cdf.loc[i, 'C'] != 0:
                        sumA = sumA + cdf.loc[i, 'C']
                        ctr = ctr + 1
                if ctr != 0:
                    avgA = sumA / ctr
                    cdf.loc[index, 'emaTwo'] = avgA

    cdf.to_csv(
        f"F:\\AT\\marketstructure\\marketstate\\MarketStructure.csv",
        index=False)


# print(getFirstItrEMAForNiftyIndex())

def getFirstItrSMAForNiftyIndex(cdf):
    # ATR for volume
    for index, row in cdf.iterrows():
        sumA = 0
        ctr = 0
        for i in range(index+1):
            if cdf.loc[i, 'C'] != 0:
                sumA = sumA + cdf.loc[i, 'C']
                ctr = ctr + 1
        if ctr != 0:
            cdf.loc[index, 'sma'] = sumA / ctr

    return cdf

# getATRForVolume()

def getAllItrATRForVolume(cdf):
    # ATR for volume
    pAtrV = cdf.loc[8, 'atrV']
    v = cdf.loc[9, "V"]
    atrV = (v - pAtrV)*2/11 + pAtrV

    return atrV

# getATRForVolume()

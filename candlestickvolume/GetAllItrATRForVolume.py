def getAllItrATRForVolume(cdf):
    # ATR for volume
    atrV = (cdf['atrV'][8] * 9 + cdf['atrV'][9]) / 10

    return atrV

# getATRForVolume()

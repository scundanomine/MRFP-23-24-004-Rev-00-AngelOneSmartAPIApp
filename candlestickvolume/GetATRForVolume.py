
def getATRForVolume(cdf):
    # get df
    df = cdf

    # ATR for volume
    atrV = df['V'].sum()/10

    # data in the df
    # df['atrV'] = atrV

    return atrV


# getATRForVolume()

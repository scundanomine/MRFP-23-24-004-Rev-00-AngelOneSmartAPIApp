from commonudm.GetCandlestickTenMinuteData import *
from statistics import mean
import pandas as pd


def getATRForVolume():
    # get df
    df = getCandlestickTenMinuteData()

    # ATR for volume
    atrV = df['V'].sum()/10

    # data in the df
    df['atrV'] = atrV
    # print(df)
    # load data in the .csv
    saveCandlestickTenMinuteData(df)

    return atrV


# getATRForVolume()

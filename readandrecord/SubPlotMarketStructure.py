import mplfinance as mpf
import pandas as pd


def subplotMarketStructure(filePath, df=pd.DataFrame()):
    ap = [mpf.make_addplot(df['emaOne'], color='g', label='EmaOne'),
          mpf.make_addplot(df['emaTwo'], color='b', label='EmaTwo'),
          mpf.make_addplot(df['QOne'], color='g', label='QOne', panel=1),
          mpf.make_addplot(df['QTwo'], color='b', label='QTwo', panel=1),
          mpf.make_addplot(df['QQOne'], color='g', label='QQOne', panel=2),
          mpf.make_addplot(df['QQTwo'], color='b', label='QQTwo', panel=2)]

    mpf.plot(df, type='candle', addplot=ap, style='yahoo', savefig=filePath)



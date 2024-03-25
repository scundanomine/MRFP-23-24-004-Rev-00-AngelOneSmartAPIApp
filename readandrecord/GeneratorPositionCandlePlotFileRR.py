import mplfinance as mpf
from commonudm.GetterReportDateForRR import getterReportDateForRR
from readandrecord.GetterDfFromSpecificRRState import getterDfFromSpecificRRState
from readandrecord.GetterPECBListRR import getterPECBListRR
from readandrecord.ProcessDerivativesDfForMplFinance import processDerivativesDfForMplFinance
from readandrecord.ProcessDfForMplFinance import processDfForMplFinance
import matplotlib.pyplot as plt

from readandrecord.SubPlotMarketStructure import subplotMarketStructure


def generatorPositionCandlePlotFileRR():
    reportDate = getterReportDateForRR()
    # getter position chart black list
    pEDf = getterPECBListRR()
    for index, row in pEDf.iterrows():
        pid = row['pid']
        if row['flagCP'] == 1:
            continue
        else:
            # get position candle for specific pid
            pCDf = getterDfFromSpecificRRState("positioncandles", pid)
            mCDf = getterDfFromSpecificRRState("positionmcandles", pid)
            if len(pCDf) == 0 and len(mCDf) == 0:
                continue
            else:
                # pCDf = getterSpecificCandleData(1, "RELIANCE-EQ")
                pcDf = processDfForMplFinance(pCDf)
                ddf = processDerivativesDfForMplFinance(mCDf)
                mcDf = processDfForMplFinance(mCDf)
                # process position candle for specific pid
                filePathOne = f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\positionplots\\{pid}.png"
                mpf.plot(pcDf, type='candle', style='yahoo', savefig=filePathOne)

                # subplot for market structure
                filePathTwo = f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\positionmplots\\{pid}.png"
                # mpf.plot(mcDf, type='candle', style='yahoo', savefig=filePathTwo)
                subplotMarketStructure(filePathTwo, ddf)

                # plot for first derivative for EMA 5 and EMA 9
                # filePathThree = f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\positionmplots\\{pid}_q.png"
                # plt.plot(ddf['time'], ddf['QOne'], label='QOne', color='yellow')
                # plt.plot(ddf['time'], ddf['QTwo'], label='QTwo', color='blue')
                # plt.savefig(filePathThree)
                # plt.close(fig=None)
                #
                # # plot for second derivative for EMA 5 and EMA 9
                # filePathFour = f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\positionmplots\\{pid}_qq.png"
                # plt.plot(ddf['time'], ddf['QQOne'], label='QQOne', color='yellow')
                # plt.plot(ddf['time'], ddf['QQTwo'], label='QQTwo', color='blue')
                # plt.savefig(filePathFour)
                # plt.close(fig=None)
                pEDf.loc[index, 'flagCP'] = 1
    pEDf.to_csv(
        'E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\PECBList.csv',
        index=False)


# generatorPositionCandlePlotFileRR()

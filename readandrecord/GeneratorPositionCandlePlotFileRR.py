import matplotlib.pyplot as plt
import mplfinance as mpf

from commonudm.GetterReportDateForRR import getterReportDateForRR
from readandrecord.GetterDfFromSpecificRRState import getterDfFromSpecificRRState
from readandrecord.GetterPECBListRR import getterPECBListRR
from readandrecord.ProcessDerivativesDfForMplFinance import processDerivativesDfForMplFinance
from readandrecord.ProcessDerivativesDfForMplFinanceTwo import processDerivativesDfForMplFinanceTwo
from readandrecord.ProcessDfForMplFinance import processDfForMplFinance
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
                qdf = processDerivativesDfForMplFinance(mCDf)
                sdf = processDerivativesDfForMplFinanceTwo(mCDf)
                # process position candle for specific pid
                filePathOne = f"F:\\AT\\report\\media\\{reportDate}\\positionplots\\{pid}.png"
                mpf.plot(pcDf, type='candle', style='yahoo', savefig=filePathOne)

                # subplot for market structure
                filePathTwo = f"F:\\AT\\report\\media\\{reportDate}\\positionmplots\\{pid}.png"
                # mpf.plot(mcDf, type='candle', style='yahoo', savefig=filePathTwo)
                subplotMarketStructure(filePathTwo, qdf)

                # plot for first derivative for EMA 5 and EMA 9
                filePathThree = f"F:\\AT\\report\\media\\{reportDate}\\positionmplots\\{pid}_q.png"
                plt.plot(sdf.index, sdf['QOne'], label='QOne', color='green')
                plt.plot(sdf.index, sdf['QTwo'], label='QTwo', color='blue')
                plt.xticks(rotation=45)
                plt.savefig(filePathThree)
                plt.close(fig=None)

                # plot for second derivative for EMA 5 and EMA 9
                filePathFour = f"F:\\AT\\report\\media\\{reportDate}\\positionmplots\\{pid}_qq.png"
                plt.plot(sdf.index, sdf['QQOne'], label='QQOne', color='green')
                plt.plot(sdf.index, sdf['QQTwo'], label='QQTwo', color='blue')
                plt.xticks(rotation=45)
                plt.savefig(filePathFour)
                plt.close(fig=None)
                pEDf.loc[index, 'flagCP'] = 1
    pEDf.to_csv(
        'F:\\AT\\readandrecord\\rrstate\\PECBList.csv',
        index=False)


# generatorPositionCandlePlotFileRR()

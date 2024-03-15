import mplfinance as mpf

from commonudm.GetterReportDateForRR import getterReportDateForRR
from readandrecord.GetterDfFromSpecificRRState import getterDfFromSpecificRRState
from readandrecord.GetterPECBListRR import getterPECBListRR
from readandrecord.ProcessDfForMplFinance import processDfForMplFinance


def generatorExitCandlePlotFileRR():
    reportDate = getterReportDateForRR()
    # getter position chart black list
    pEDf = getterPECBListRR()
    for index, row in pEDf.iterrows():
        pid = row['pid']
        if row['flagCE'] == 1:
            continue
        else:
            # get position candle for specific pid
            pCDf = getterDfFromSpecificRRState("exitcandles", pid)
            mCDf = getterDfFromSpecificRRState("exitmcandles", pid)
            if len(pCDf) == 0 and len(mCDf) == 0:
                continue
            else:
                # pCDf = getterSpecificCandleData(1, "RELIANCE-EQ")
                pcDf = processDfForMplFinance(pCDf)
                mcDf = processDfForMplFinance(mCDf)
                # process position candle for specific pid
                filePathOne = f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\exitplots\\{pid}.png"
                mpf.plot(pcDf, type='candle', style='yahoo', savefig=filePathOne)
                filePathTwo = f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\exitmplots\\{pid}.png"
                mpf.plot(mcDf, type='candle', style='yahoo', savefig=filePathTwo)
                pEDf.loc[index, 'flagCE'] = 1
    pEDf.to_csv(
        'E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\PECBList.csv',
        index=False)


# generatorPositionCandlePlotFileRR()

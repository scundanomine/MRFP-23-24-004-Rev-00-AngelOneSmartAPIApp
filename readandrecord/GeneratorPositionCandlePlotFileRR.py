import mplfinance as mpf

from commonudm.GetterReportDateForRR import getterReportDateForRR
from readandrecord.GetterDfFromSpecificRRState import getterDfFromSpecificRRState
from readandrecord.GetterPECBListRR import getterPECBListRR
from readandrecord.ProcessDfForMplFinance import processDfForMplFinance


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
            pCDf = getterDfFromSpecificRRState('positioncandles', pid)
            if len(pCDf) == 0:
                continue
            else:
                # pCDf = getterSpecificCandleData(1, "RELIANCE-EQ")
                pcDf = processDfForMplFinance(pCDf)
                # process position candle for specific pid
                filePath = f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\positionplots\\{pid}.png"
                mpf.plot(pcDf, type='candle', style='yahoo', savefig=filePath)
                pEDf.loc[index, 'flagCP'] = 1
    pEDf.to_csv(
        'E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\PECBList.csv',
        index=False)


# generatorPositionCandlePlotFileRR()

import pandas as pd
from commonudm.GetterReportDateForRR import getterReportDateForRR


def getterDfFromSpecificRRState(source, pid):
    reportDate = getterReportDateForRR()
    try:
        df = pd.read_csv(
                f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\{source}\\{pid}.csv")
    except Exception as e:
        print(f"Exception while getterDfFromSpecificRRState is {e}")
        df = pd.DataFrame()
    return df


# print(getterPECBListRR())

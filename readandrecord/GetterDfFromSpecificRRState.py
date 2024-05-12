import pandas as pd
from commonudm.GetterReportDateForRR import getterReportDateForRR
import os


def getterDfFromSpecificRRState(source, pid):
    reportDate = getterReportDateForRR()
    try:
        if os.path.isfile(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\{source}\\{pid}.csv"):
            df = pd.read_csv(
                    f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\{source}\\{pid}.csv")
        else:
            df = pd.DataFrame()
    except Exception as e:
        print(f"Exception while getterDfFromSpecificRRState is {e}")
        df = pd.DataFrame()
    return df


# print(getterDfFromSpecificRRState("exitdetails", 8))

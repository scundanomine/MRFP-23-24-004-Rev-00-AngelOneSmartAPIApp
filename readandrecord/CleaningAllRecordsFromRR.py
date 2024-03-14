from commonudm.CleaningAllFilesFromSpecificDirectory import cleaningAllFilesFromSpecificDirectory
from commonudm.GetterReportDateForRR import getterReportDateForRR
from position.GetterPositionId import getterPositionId


def cleaningAllRecordsFromRR():
    reportDate = getterReportDateForRR()
    pid = getterPositionId()
    if pid == 0:
        cleaningAllFilesFromSpecificDirectory(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\exitcandles")
        cleaningAllFilesFromSpecificDirectory(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\exitdetails")
        cleaningAllFilesFromSpecificDirectory(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\exitplots")
        cleaningAllFilesFromSpecificDirectory(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\exitmcandles")
        cleaningAllFilesFromSpecificDirectory(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\exitmdetails")
        cleaningAllFilesFromSpecificDirectory(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\exitmplots")
        cleaningAllFilesFromSpecificDirectory(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\positioncandles")
        cleaningAllFilesFromSpecificDirectory(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\positiondetails")
        cleaningAllFilesFromSpecificDirectory(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\positionplots")
        cleaningAllFilesFromSpecificDirectory(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\positionmcandles")
        cleaningAllFilesFromSpecificDirectory(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\positionmdetails")
        cleaningAllFilesFromSpecificDirectory(
            f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\report\\media\\{reportDate}\\positionmplots")


# cleaningAllRecordsFromRR()

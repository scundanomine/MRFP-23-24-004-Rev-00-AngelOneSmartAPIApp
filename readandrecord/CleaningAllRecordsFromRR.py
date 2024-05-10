from commonudm.CleaningAllFilesFromSpecificDirectory import cleaningAllFilesFromSpecificDirectory
from commonudm.GetterReportDateForRR import getterReportDateForRR


def cleaningAllRecordsFromRR():
    reportDate = getterReportDateForRR()
    cleaningAllFilesFromSpecificDirectory(
        f"F:\\AT\\report\\media\\{reportDate}\\exitcandles")
    cleaningAllFilesFromSpecificDirectory(
        f"F:\\AT\\report\\media\\{reportDate}\\exitdetails")
    cleaningAllFilesFromSpecificDirectory(
        f"F:\\AT\\report\\media\\{reportDate}\\exitplots")
    cleaningAllFilesFromSpecificDirectory(
        f"F:\\AT\\report\\media\\{reportDate}\\exitmcandles")
    cleaningAllFilesFromSpecificDirectory(
        f"F:\\AT\\report\\media\\{reportDate}\\exitmdetails")
    cleaningAllFilesFromSpecificDirectory(
        f"F:\\AT\\report\\media\\{reportDate}\\exitmplots")
    cleaningAllFilesFromSpecificDirectory(
        f"F:\\AT\\report\\media\\{reportDate}\\positioncandles")
    cleaningAllFilesFromSpecificDirectory(
        f"F:\\AT\\report\\media\\{reportDate}\\positiondetails")
    cleaningAllFilesFromSpecificDirectory(
        f"F:\\AT\\report\\media\\{reportDate}\\positionplots")
    cleaningAllFilesFromSpecificDirectory(
        f"F:\\AT\\report\\media\\{reportDate}\\positionmcandles")
    cleaningAllFilesFromSpecificDirectory(
        f"F:\\AT\\report\\media\\{reportDate}\\positionmdetails")
    cleaningAllFilesFromSpecificDirectory(
        f"F:\\AT\\report\\media\\{reportDate}\\positionmplots")


# cleaningAllRecordsFromRR()

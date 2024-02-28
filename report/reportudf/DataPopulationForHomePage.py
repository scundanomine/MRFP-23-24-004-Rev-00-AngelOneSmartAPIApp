# from report.reportudf.GetterDataForSpecificPidAndDate import getterDataForSpecificPidAndDate
from reportudf.GetterDataForSpecificPidAndDate import getterDataForSpecificPidAndDate


def dataPopulationForHomePage(pid, reportDate):
    reportData = []
    for i in range(1, pid + 1):
        dicT = getterDataForSpecificPidAndDate(i, reportDate)
        reportData.append(dicT)
    return reportData


# print(dataPopulationForHomePage(10, '2024-01-25'))

from django.shortcuts import render
import sys
from reportudf import GetterReportDate, DataPopulationForHomePage, DataPopulationForDetailPage, GetterReportPreDate, GetWinPercentage
sys.path.append('F:\\AT\\position')
import GetterPositionIdForSpecificDate


def homePage(request):
    # while True:
    GetterReportPreDate.getterReportPreDate()
    reportDate = GetterReportDate.getterReportDate()
    pid = GetterPositionIdForSpecificDate.getterPositionIdForSpecificDate(reportDate)
    reportData = DataPopulationForHomePage.dataPopulationForHomePage(pid, reportDate)
    winPercentage = GetWinPercentage.getWinPercentage(pid, reportDate)
    data = {'reportDate': reportDate, 'reportData': reportData, 'winPercentage': winPercentage}
    return render(request, "index.html", data)


def detailPage(request, positionId):
    # while True:
    reportDate = GetterReportDate.getterReportDate()
    reportData = DataPopulationForDetailPage.dataPopulationForDetailPage(positionId, reportDate)
    data = {'pid': positionId, 'reportDate': reportDate, 'reportData': reportData}
    return render(request, "detail.html", data)

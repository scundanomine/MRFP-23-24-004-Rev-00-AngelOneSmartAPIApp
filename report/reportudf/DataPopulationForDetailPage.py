# from report.reportudf.GetterDataForSpecificPidAndDate import getterDataForSpecificPidAndDate
from reportudf.GetterDataForSpecificPidAndDate import getterDataForSpecificPidAndDate


def dataPopulationForDetailPage(pid, reportDate):
    # get data for position detail
    positionDetail = getterDataForSpecificPidAndDate(pid, reportDate, "positiondetails")

    # get data for position detail
    positionCandles = getterDataForSpecificPidAndDate(pid, reportDate, "positioncandles")

    # image url
    positionPlotUrl = f"/media/{reportDate}/positionplots/{pid}.png"

    # get data for exit detail
    exitDetail = getterDataForSpecificPidAndDate(pid, reportDate, "exitdetails")

    # get data for exit detail
    exitCandles = getterDataForSpecificPidAndDate(pid, reportDate, "exitcandles")

    # image url
    exitPlotUrl = f"/media/{reportDate}/exitplots/{pid}.png"

    return {"positionDetail": positionDetail, "positionCandles": positionCandles, "positionPlotUrl": positionPlotUrl,
            "exitDetail": exitDetail, "exitCandles": exitCandles, "exitPlotUrl": exitPlotUrl}


# print(dataPopulationForDetailPage(1, "2024-01-25")["positionPlotUrl"])

# from report.reportudf.GetterDataForSpecificPidAndDate import getterDataForSpecificPidAndDate
from reportudf.GetterDataForSpecificPidAndDate import getterDataForSpecificPidAndDate
from reportudf.GetterCandleDataForForSpecificPidAndDate import getterCandleDataForForSpecificPidAndDate


def dataPopulationForDetailPage(pid, reportDate):
    # get data for position detail
    positionDetail = getterDataForSpecificPidAndDate(pid, reportDate, "positiondetails")

    # get data for position candles
    positionCandles = getterCandleDataForForSpecificPidAndDate(pid, reportDate, "positioncandles")

    # image url
    positionPlotUrl = f"{reportDate}/positionplots/{pid}.PNG"

    # get data for exit detail
    exitDetail = getterDataForSpecificPidAndDate(pid, reportDate, "exitdetails")

    # get data for exit candles
    exitCandles = getterCandleDataForForSpecificPidAndDate(pid, reportDate, "exitcandles")

    # image url
    exitPlotUrl = f"{reportDate}/exitplots/{pid}.PNG"

    return {"positionDetail": positionDetail, "positionCandles": positionCandles, "positionPlotUrl": positionPlotUrl,
            "exitDetail": exitDetail, "exitCandles": exitCandles, "exitPlotUrl": exitPlotUrl}


# print(dataPopulationForDetailPage(1, "2024-01-25")["positionPlotUrl"])

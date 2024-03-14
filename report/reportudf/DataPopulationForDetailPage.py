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

    # get data for market position detail
    positionMDetail = getterDataForSpecificPidAndDate(pid, reportDate, "positionmdetails")

    # image market position url
    positionMPlotUrl = f"{reportDate}/positionmplots/{pid}.PNG"

    # get data for exit detail
    exitDetail = getterDataForSpecificPidAndDate(pid, reportDate, "exitdetails")

    # get data for exit candles
    exitCandles = getterCandleDataForForSpecificPidAndDate(pid, reportDate, "exitcandles")

    # image url
    exitPlotUrl = f"{reportDate}/exitplots/{pid}.PNG"

    # get data for market exit detail
    exitMDetail = getterDataForSpecificPidAndDate(pid, reportDate, "exitmdetails")

    # image market exit url
    exitMPlotUrl = f"{reportDate}/exitmplots/{pid}.PNG"

    return {"positionDetail": positionDetail, "positionCandles": positionCandles, "positionPlotUrl": positionPlotUrl,
            "positionMDetail": positionMDetail, "positionMPlotUrl": positionMPlotUrl,
            "exitDetail": exitDetail, "exitCandles": exitCandles, "exitPlotUrl": exitPlotUrl,
            "exitMDetail": exitMDetail, "exitMPlotUrl": exitMPlotUrl}


# print(dataPopulationForDetailPage(1, "2024-01-25")["positionPlotUrl"])

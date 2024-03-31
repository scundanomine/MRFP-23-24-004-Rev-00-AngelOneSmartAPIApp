# from report.reportudf.GetterDataForSpecificPidAndDate import getterDataForSpecificPidAndDate
from reportudf.GetterDataForSpecificPidAndDate import getterDataForSpecificPidAndDate
from reportudf.GetterCandleDataForForSpecificPidAndDate import getterCandleDataForForSpecificPidAndDate
from reportudf.GetterMarketCandleDataForSpecificPidAndDate import getterMarketCandleDataForSpecificPidAndDate


def dataPopulationForDetailPage(pid, reportDate):
    # get data for position detail
    positionDetail = getterDataForSpecificPidAndDate(pid, reportDate, "positiondetails")

    # get data for position candles
    positionCandles = getterCandleDataForForSpecificPidAndDate(pid, reportDate, "positioncandles")

    # image url
    positionPlotUrl = f"{reportDate}/positionplots/{pid}.PNG"

    # get data for market position detail
    positionMDetail = getterMarketCandleDataForSpecificPidAndDate(pid, reportDate, "positionmdetails")

    # image market position url
    positionMPlotUrl = f"{reportDate}/positionmplots/{pid}.PNG"
    positionMQPlotUrl = f"{reportDate}/positionmplots/{pid}_q.PNG"
    positionMQQPlotUrl = f"{reportDate}/positionmplots/{pid}_qq.PNG"

    # get data for exit detail
    exitDetail = getterDataForSpecificPidAndDate(pid, reportDate, "exitdetails")

    # get data for exit candles
    exitCandles = getterCandleDataForForSpecificPidAndDate(pid, reportDate, "exitcandles")

    # image url
    exitPlotUrl = f"{reportDate}/exitplots/{pid}.PNG"

    # get data for market exit detail
    exitMDetail = getterMarketCandleDataForSpecificPidAndDate(pid, reportDate, "exitmdetails")

    # image market exit url
    exitMPlotUrl = f"{reportDate}/exitmplots/{pid}.PNG"
    exitMQPlotUrl = f"{reportDate}/exitmplots/{pid}_q.PNG"
    exitMQQPlotUrl = f"{reportDate}/exitmplots/{pid}_qq.PNG"

    return {"positionDetail": positionDetail, "positionCandles": positionCandles, "positionPlotUrl": positionPlotUrl,
            "positionMDetail": positionMDetail, "positionMPlotUrl": positionMPlotUrl, "positionMQPlotUrl": positionMQPlotUrl, "positionMQQPlotUrl": positionMQQPlotUrl,
            "exitDetail": exitDetail, "exitCandles": exitCandles, "exitPlotUrl": exitPlotUrl,
            "exitMDetail": exitMDetail, "exitMPlotUrl": exitMPlotUrl, "exitMQPlotUrl": exitMQPlotUrl, "exitMQQPlotUrl": exitMQQPlotUrl}


# print(dataPopulationForDetailPage(1, "2024-01-25")["positionPlotUrl"])

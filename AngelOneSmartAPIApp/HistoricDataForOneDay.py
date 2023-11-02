import datetime


def getHistoricDataForOneDay(obj, c, token):
    candleStickData = []

    # date time formulation
    refDate = datetime.datetime.now() - c
    newDateF = refDate.strftime("%Y-%m-%d %H:%M")
    try:
        historicParam = {
            "exchange": "NSE",
            "symboltoken": token,
            "interval": "ONE_MINUTE",
            "fromdate": newDateF,
            "todate": newDateF
        }
        candleStickData = obj.getCandleData(historicParam)
    except Exception as e:
        print("Historic Api failed: {}".format(e.message))
    return candleStickData["data"]

# print(getHistoricDataForOneDay("2023-09-28"))

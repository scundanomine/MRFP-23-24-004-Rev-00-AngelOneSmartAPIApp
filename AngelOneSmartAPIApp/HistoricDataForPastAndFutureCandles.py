import datetime


def getHistoricDataForPastAndFutureCandles(obj, c, token):
    candleStickData = []
    # date time formulation
    refDate = datetime.datetime.now() - c
    futureRefDate = refDate + datetime.timedelta(minutes=2)
    newDateF = refDate.strftime("%Y-%m-%d %H:%M")
    futureDateF = futureRefDate.strftime("%Y-%m-%d %H:%M")

    try:
        historicParam = {
            "exchange": "NSE",
            "symboltoken": token,
            "interval": "ONE_MINUTE",
            "fromdate": newDateF,
            "todate": futureDateF
        }
        candleStickData = obj.getCandleData(historicParam)
    except Exception as e:
        print("Historic Api failed: {}".format(e.message))
    return candleStickData["data"], refDate

# print(getHistoricDataForOneDay("2023-09-28"))

import datetime


def getHistoricDataForPastTenCandles(obj, c, token):
    candleStickData = []
    # date time formulation
    refDate = datetime.datetime.now() - c
    pastTenMinRefDate = refDate - datetime.timedelta(minutes=9)
    newDateF = refDate.strftime("%Y-%m-%d %H:%M")
    pastDateF = pastTenMinRefDate.strftime("%Y-%m-%d %H:%M")

    try:
        historicParam = {
            "exchange": "NSE",
            "symboltoken": token,
            "interval": "ONE_MINUTE",
            "fromdate": pastDateF,
            "todate": newDateF
        }
        candleStickData = obj.getCandleData(historicParam)
    except Exception as e:
        print("Historic Api failed: {}".format(e.message))
    return candleStickData["data"], pastTenMinRefDate

# print(getHistoricDataForOneDay("2023-09-28"))

import datetime


def historicDataForOneDayForTraditionalPivot(obj, refDate, token):
    candleStickData = []

    try:
        historicParam = {
            "exchange": "NSE",
            "symboltoken": token,
            "interval": "ONE_DAY",
            "fromdate": f"{refDate} 09:15",
            "todate": f"{refDate} 15:30"
        }
        candleStickData = obj.getCandleData(historicParam)
    except Exception as e:
        print("Historic Api failed: {}".format(e.message))
    return candleStickData["data"]

# print(getHistoricDataForOneDay("2023-09-28"))

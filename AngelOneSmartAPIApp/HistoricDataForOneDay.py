
def getHistoricDataForOneDay(obj, date, token):
    candleStickData = []
    try:
        historicParam = {
            "exchange": "NSE",
            "symboltoken": token,
            "interval": "ONE_DAY",
            "fromdate": f"{date} 00:00",
            "todate": f"{date} 15:30"
        }
        candleStickData = obj.getCandleData(historicParam)
    except Exception as e:
        print("Historic Api failed: {}".format(e.message))
    return candleStickData["data"]


# print(getHistoricDataForOneDay("2023-09-28"))

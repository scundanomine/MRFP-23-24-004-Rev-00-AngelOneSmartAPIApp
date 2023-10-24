
def getHistoricDataForPastTenCandles(obj, date, token):
    candleStickData = []
    try:
        historicParam = {
            "exchange": "NSE",
            "symboltoken": token,
            "interval": "ONE_MINUTE",
            "fromdate": f"{date} 09:15",
            "todate": f"{date} 09:24"
        }
        candleStickData = obj.getCandleData(historicParam)
    except Exception as e:
        print("Historic Api failed: {}".format(e.message))
    return candleStickData["data"]


# print(getHistoricDataForOneDay("2023-09-28"))

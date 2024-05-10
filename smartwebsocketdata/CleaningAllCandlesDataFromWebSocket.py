from commonudm.CleaningAllFilesFromSpecificDirectory import cleaningAllFilesFromSpecificDirectory


def cleaningAllCandlesDataFromWebSocket(cleaningFlag=False):
    if cleaningFlag:
        cleaningAllFilesFromSpecificDirectory(
            "F:\\AT\\smartwebsocketdata\\websocketstate\\tokenwisefreshcandledata")
        cleaningAllFilesFromSpecificDirectory(
            "F:\\AT\\smartwebsocketdata\\websocketstate\\tokenwisepartlycandledata")
        cleaningAllFilesFromSpecificDirectory(
            "F:\\AT\\smartwebsocketdata\\websocketstate\\tokenwisewholecandledata")


# cleaningAllRecordsFromRR()

from commonudm.CleaningAllFilesFromSpecificDirectory import cleaningAllFilesFromSpecificDirectory


def cleaningAllCandlesDataFromWebSocket(cleaningFlag=False):
    if cleaningFlag:
        cleaningAllFilesFromSpecificDirectory(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisefreshcandledata")
        cleaningAllFilesFromSpecificDirectory(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisepartlycandledata")
        cleaningAllFilesFromSpecificDirectory(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\smartwebsocketdata\\websocketstate\\tokenwisewholecandledata")


# cleaningAllRecordsFromRR()

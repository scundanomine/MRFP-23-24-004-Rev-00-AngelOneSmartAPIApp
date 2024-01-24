from commonudm.CleaningAllFilesFromSpecificDirectory import cleaningAllFilesFromSpecificDirectory


def cleaningAllRecordsFromRR(cleaningFlag=False):
    if cleaningFlag:
        cleaningAllFilesFromSpecificDirectory(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\exitcandles")
        cleaningAllFilesFromSpecificDirectory(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\exitdetails")
        cleaningAllFilesFromSpecificDirectory(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\exitplots")
        cleaningAllFilesFromSpecificDirectory(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\positioncandles")
        cleaningAllFilesFromSpecificDirectory(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\positiondetails")
        cleaningAllFilesFromSpecificDirectory(
            "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\positionplots")


# cleaningAllRecordsFromRR(True)

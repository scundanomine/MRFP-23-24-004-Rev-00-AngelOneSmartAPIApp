import multiprocessing
from exit.GetCustomDfExitInputs import getCustomDfExitInputs
from exit.GetterExitInputs import getterExitInputs


def getExitInputs(lock=multiprocessing.Lock()):
    # get custom black list dataframe
    df = getCustomDfExitInputs(lock)

    # getter black list
    eIDf = getterExitInputs(lock)

    for index, row in df.iterrows():
        if row["rFlag"] == 1 or row["eFlag"] == 1:
            eIDf.iloc[index] = row
    eIDf.to_csv(
        "E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\entrytriggeredlist\\entrytriggeredstate\\BlackListET.csv",
        index=False)
    # print(eIDf)


# getCustomDfExitInputs()

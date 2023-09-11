import pandas as pd


def loadRFT(dataFrm):
    dataFrm.to_csv("referenceTimer.csv", index=False)
    print(dataFrm)

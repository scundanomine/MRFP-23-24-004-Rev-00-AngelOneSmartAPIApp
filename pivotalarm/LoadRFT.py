import pandas as pd


def loadRFT(dataFrm):
    rft = dataFrm
    rft.to_csv("referenceTimer.csv", index=False)
    print(rft)

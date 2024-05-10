import os
from commonudm.GetterReportDateForRR import getterReportDateForRR
import pandas as pd


def createRRDirectoriesIfNotExist():
    reportDate = getterReportDateForRR()

    # folder creation for state folder
    if not os.path.exists(
            f"F:\\AT\\report\\media\\{reportDate}\\state"):
        os.makedirs(
            f"F:\\AT\\report\\media\\{reportDate}\\state")
        marDf = pd.DataFrame([0], columns=['pid'])
        marDf.to_csv(
            f"F:\\AT\\report\\media\\{reportDate}\\state\\PId.csv",
            index=False)
    # folder creation for position details
    if not os.path.exists(
            f"F:\\AT\\report\\media\\{reportDate}\\positiondetails"):
        os.makedirs(
            f"F:\\AT\\report\\media\\{reportDate}\\positiondetails")
    if not os.path.exists(
            f"F:\\AT\\report\\media\\{reportDate}\\positioncandles"):
        os.makedirs(
            f"F:\\AT\\report\\media\\{reportDate}\\positioncandles")
    if not os.path.exists(
            f"F:\\AT\\report\\media\\{reportDate}\\positionplots"):
        os.makedirs(
            f"F:\\AT\\report\\media\\{reportDate}\\positionplots")

    # folder creation for position market data
    if not os.path.exists(
            f"F:\\AT\\report\\media\\{reportDate}\\positionmdetails"):
        os.makedirs(
            f"F:\\AT\\report\\media\\{reportDate}\\positionmdetails")
    if not os.path.exists(
            f"F:\\AT\\report\\media\\{reportDate}\\positionmcandles"):
        os.makedirs(
            f"F:\\AT\\report\\media\\{reportDate}\\positionmcandles")
    if not os.path.exists(
            f"F:\\AT\\report\\media\\{reportDate}\\positionmplots"):
        os.makedirs(
            f"F:\\AT\\report\\media\\{reportDate}\\positionmplots")

    # folder creation for exit details
    if not os.path.exists(
            f"F:\\AT\\report\\media\\{reportDate}\\exitdetails"):
        os.makedirs(
            f"F:\\AT\\report\\media\\{reportDate}\\exitdetails")
    if not os.path.exists(
            f"F:\\AT\\report\\media\\{reportDate}\\exitcandles"):
        os.makedirs(
            f"F:\\AT\\report\\media\\{reportDate}\\exitcandles")
    if not os.path.exists(
            f"F:\\AT\\report\\media\\{reportDate}\\exitplots"):
        os.makedirs(
            f"F:\\AT\\report\\media\\{reportDate}\\exitplots")

    # folder creation for exit market data
    if not os.path.exists(
            f"F:\\AT\\report\\media\\{reportDate}\\exitmdetails"):
        os.makedirs(
            f"F:\\AT\\report\\media\\{reportDate}\\exitmdetails")
    if not os.path.exists(
            f"F:\\AT\\report\\media\\{reportDate}\\exitmcandles"):
        os.makedirs(
            f"F:\\AT\\report\\media\\{reportDate}\\exitmcandles")
    if not os.path.exists(
            f"F:\\AT\\report\\media\\{reportDate}\\exitmplots"):
        os.makedirs(
            f"F:\\AT\\report\\media\\{reportDate}\\exitmplots")


# createRRDirectoriesIfNotExist()

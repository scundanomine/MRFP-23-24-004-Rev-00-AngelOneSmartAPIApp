import pandas as pd


def setterPreEntryBanned():
    df = pd.DataFrame([[0, "none"]], columns=['rf', 'trend'])
    df.to_csv('F:\\AT\\positionportfolioandmargindisplay\\displaystate\\EntryBanned.csv', index=False)


# setterPreEntryBanned()

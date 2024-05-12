import pandas as pd


def setterPreEntryBanned():
    df = pd.DataFrame([[0, "none"]], columns=['rf', 'trend'])
    df.to_csv('E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\positionportfolioandmargindisplay\\displaystate\\EntryBanned.csv', index=False)


# setterPreEntryBanned()

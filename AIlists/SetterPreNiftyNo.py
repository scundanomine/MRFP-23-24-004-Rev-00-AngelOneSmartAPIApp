import pandas as pd


def setterPreNiftyNo():
    df = pd.DataFrame([0], columns=['NiftyNo'])
    df.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\AIlists\\AIstate\\NiftyNo.csv",
              index=False)


# setterPreNiftyNo()

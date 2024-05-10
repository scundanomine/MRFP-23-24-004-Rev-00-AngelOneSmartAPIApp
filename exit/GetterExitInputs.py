import pandas as pd


def getterExitInputs():
    try:
        df = pd.read_csv(
            f"F:\\AT\\exit\\exitstate\\ExitInputs.csv")
    except Exception as e:
        print(f"The exception while getter Exit inputs is {e}")
        # df = pd.DataFrame(columns=["id", "bFlag"])
        df = getterExitInputs()
    return df


# getterBlackListET()

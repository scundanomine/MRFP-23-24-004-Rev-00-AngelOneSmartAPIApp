import pandas as pd


def getterDebitAndSetterAvailableMargin(mr, lock):
    with lock:
        try:
            df = pd.read_csv(
                "F:\\AT\\margin\\marginstate\\margin.csv")
            df.loc[0, 'margin'] = df.loc[0, 'margin'] - mr
            df.to_csv(
                "F:\\AT\\margin\\marginstate\\margin.csv",
                index=False)
        except Exception as e:
            print(f"The exception while getterDebitAndSetterAvailableMargin is {e}")
            getterDebitAndSetterAvailableMargin(mr, lock)

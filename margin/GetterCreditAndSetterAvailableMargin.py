import pandas as pd
import multiprocessing


def getterCreditAndSetterAvailableMargin(mr, lock=multiprocessing.Lock()):
    with lock:
        try:
            df = pd.read_csv(
                "F:\\AT\\margin\\marginstate\\margin.csv")
            df.loc[0, 'margin'] = df.loc[0, 'margin'] + mr
            df.to_csv(
                "F:\\AT\\margin\\marginstate\\margin.csv",
                index=False)
        except Exception as e:
            print(f"The exception while getterCreditAndSetterAvailableMargin is {e}")
            getterCreditAndSetterAvailableMargin(mr, lock)


# getterCreditAndSetterAvailableMargin(50000)

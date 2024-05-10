import pandas as pd
import os


def getWinPercentage(pid, rDate):
    OPid = int(pid)
    winC = 0
    for i in range(pid):
        if os.path.isfile(
                f"F:\\AT\\report\\media\\{rDate}\\exitdetails\\{i}.csv"):
            while True:
                try:
                    df = pd.read_csv(
                        f"F:\\AT\\report\\media\\{rDate}\\exitdetails\\{i}.csv")
                    break
                except Exception as e:
                    print(f"Exception while getWinPercentage {e}")
            if df.loc[0, "gol"] > 0:
                winC = winC + 1
        else:
            OPid = OPid - 1

    if OPid > 0:
        return round(winC / OPid * 100, 2)
    else:
        return "No position taken yet"


# print(getWinPercentage("2024-02-06"))

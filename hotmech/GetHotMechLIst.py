import pandas as pd


def getHotMechList():
    while True:
        try:
            with open(f"HotMechLst.csv", "r") as f:
                hotMechLst = pd.read_csv(f)
            print("rock!!!")
            break
        except:
            hotMechLst = pd.DataFrame(index=list(range(50)),
                                      columns=["slot", "timer", "id", "desc", "sector", "symbol", "token", "ltp"])
            hotMechLst['slot'] = range(1, 51)
            hotMechLst['id'] = 0
            hotMechLst.to_csv("HotMechLst.csv", index=False)
            break

    return hotMechLst


print(getHotMechList())

import pandas as pd


def getHotMechList():
    while True:
        try:
            with open(f"E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\hotmech\\HotMechLst.csv", "r") as f:
                hotMechLst = pd.read_csv(f)
            # print("rock!!!")
            break
        except:
            hotMechLst = pd.DataFrame(index=list(range(100)),
                                      columns=["slot", "rft", "id", "desc", "sector", "symbol", "token", "ltp", 'typ'])
            hotMechLst['slot'] = range(1, 101)
            hotMechLst['id'] = 0
            hotMechLst.to_csv("E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\hotmech\\HotMechLst.csv", index=False)
            break

    return hotMechLst


# print(getHotMechList())

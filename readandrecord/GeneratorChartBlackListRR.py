from readandrecord.GetterPECBListRR import getterPECBListRR


def generatorChartBlackListRR(pid):
    # get PECBList
    df = getterPECBListRR()
    n = len(df)
    try:
        for i in range(n, pid):
            df.loc[i] = [i+1, 0, 0]
    except Exception as e:
        print(f"The exception while generatorChartBlackListRR is {e}")
        df = getterPECBListRR()
    df.to_csv(
        'F:\\AT\\readandrecord\\rrstate\\PECBList.csv',
        index=False)
    return df


# print(generatorChartBlackListRR(117))

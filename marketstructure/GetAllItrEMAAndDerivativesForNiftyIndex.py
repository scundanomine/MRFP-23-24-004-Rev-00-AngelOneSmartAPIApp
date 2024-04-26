import math


def getAllItrEMAAndDerivativesForNiftyIndex(df):
    # calculation for EMAs
    index = 9
    if df.loc[index, 'C'] != 0 or df.loc[index - 1, 'C'] != 0:
        df.loc[index, 'emaOne'] = (df.loc[9, 'C'] - df.loc[8, 'emaOne']) / 3 + df.loc[8, 'emaOne']
        df.loc[index, 'emaTwo'] = (df.loc[9, 'C'] - df.loc[8, 'emaTwo']) / 5 + df.loc[8, 'emaTwo']
        # calculation for first derivatives
        df.loc[index, 'QOne'] = math.atan((df.loc[index, 'emaOne'] - df.loc[index - 1, 'emaOne']) / 4) * 180 / math.pi
        df.loc[index, 'QTwo'] = math.atan((df.loc[index, 'emaTwo'] - df.loc[index - 1, 'emaTwo']) / 4) * 180 / math.pi
        # calculation for second derivatives
        dyTwo = math.tan(df.loc[index, 'QOne'] * math.pi / 180) * 2
        dyOne = math.tan(df.loc[index - 1, 'QOne'] * math.pi / 180) * 2
        dzTwo = math.tan(df.loc[index, 'QTwo'] * math.pi / 180) * 2
        dzOne = math.tan(df.loc[index - 1, 'QTwo'] * math.pi / 180) * 2
        df.loc[index, 'QQOne'] = math.atan((dyTwo - dyOne) / 4) * 180 / math.pi
        df.loc[index, 'QQTwo'] = math.atan((dzTwo - dzOne) / 4) * 180 / math.pi

    return df
# print(getAllItrEMAAndDerivativesForNiftyIndex())

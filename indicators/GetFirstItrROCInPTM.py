def getFirstItrROCInPTM(df):
    try:
        df['roc'] = 0
        for index, row in df.iterrows():
            if row['C'] != 0:
                for i in range(index + 1):
                    if df.loc[i, "C"] != 0:
                        df.loc[index, 'roc'] = (row['C'] - df.loc[i, "C"]) / row['C'] * 10000
                        break
    except Exception as e:
        print(f"the exception while calculating roc is {e}")
    return df

# print(getROCInPTM())

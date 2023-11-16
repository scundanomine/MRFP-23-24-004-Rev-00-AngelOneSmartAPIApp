import pandas as pd

dfOne = pd.DataFrame([[1, 2, 2, 4], [0, 0, 0, 0]])
print(dfOne)

dfTwo = pd.DataFrame([[1, 9, 2, 6], [5, 5, 8, 9]])
print(dfTwo)
dfTwo.to_csv("", index=False)

dfTwo.iloc[1] = dfOne.iloc[1]
print("++++++++++++++++++++++++")
print(dfTwo)

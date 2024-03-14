import pandas as pd

df = pd.DataFrame([[1, 2, 3, 4, 8, 9], [1, 2, 3, 4, 8, 9], [1, 2, 3, 4, 8, 9]])
dfTwo = pd.DataFrame([[9, 9, 9], [1, 2, 3], [9, 9, 9]])
df.iloc[2][3:] = dfTwo.iloc[2]
print(df)

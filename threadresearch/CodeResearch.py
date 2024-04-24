import pandas as pd

df = pd.DataFrame([[1, 2, 3, 4, 8, 9], [1, 2, 3, 8, 8, 9], [1, 2, 3, 4, 8, 9]])
print(df.loc[0:2])
lst = [1, 4, 8, 9, 5]

print("result for list")
print(lst[0:4])
import pandas as pd
import datetime

df = pd.DataFrame([[1, 2, 4], [5, 4, 6]])
dfOne = pd.DataFrame([[0, 2, 5], [1, 3, 8]])
df = pd.concat([df, dfOne], ignore_index=True)
print(df)



import pandas as pd
import datetime

df = pd.DataFrame([[1, 2, 4], [5, 4, 6]])
print(df)

for index, row in df.iterrows():
    df = pd.DataFrame([row])
    print(df)
    # break

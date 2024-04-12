import pandas as pd

dfOne = pd.DataFrame(columns=['time', 'O', 'H', "L", 'C', 'V'], index=[0, 1, 2])
new_cols = range(60)
dfOne[:] = 0
# cols_to_add = [col for col in new_cols if col not in sdf.columns]
dfOne.loc[:, new_cols] = 0

print(dfOne)

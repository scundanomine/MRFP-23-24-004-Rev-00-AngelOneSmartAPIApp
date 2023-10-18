import pandas as pd

ds = pd.Series(index=list(range(100)))
ds[:] = 0

print(ds)

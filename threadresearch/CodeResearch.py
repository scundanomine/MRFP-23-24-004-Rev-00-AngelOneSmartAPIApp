import pandas as pd
import datetime

# print(pd.to_timedelta(0))
# print(datetime.datetime.now() - pd.to_timedelta(0))

a = "2024-01-19T10:20:00+05:30"
a = a[:16]
a = a.replace('T', ' ')
print(a)

refDate = datetime.datetime.strptime(a, "%Y-%m-%d %H:%M")
print(refDate)

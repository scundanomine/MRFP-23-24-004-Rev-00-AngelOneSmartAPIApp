import datetime
import time

# print(datetime.datetime.now()-datetime.timedelta(days=2))
# print(time.localtime())
# string = "19 Nov 2015  18:45:00.000"
# date = datetime.datetime.strptime(string, "%d %b %Y  %H:%M:%S.%f")
# currentDate = datetime.datetime.now()
# dTime = currentDate-date
# print(date + dTime)

strDate = "30 Oct 2023  15:24:00.000"
refDate = datetime.datetime.strptime(strDate, "%d %b %Y %H:%M:%S.%f")
currentDate = datetime.datetime.now()
print(refDate)
c = datetime.datetime.now() - refDate
# k = datetime.datetime.now() - c

pastDate = datetime.datetime.now() - c
newDateF = pastDate.strftime("%Y-%m-%dT%H:%M:00+05:30")
print(newDateF)
# z = 0
# while z < 5:
#     lst = str(datetime.datetime.now() - c).split('.')[0]
#     mLst = lst.replace(" ", "T")
#     print(mLst)
#     time.sleep(1)
#     z = z + 1

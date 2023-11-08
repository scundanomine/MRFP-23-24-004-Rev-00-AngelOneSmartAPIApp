from commonudm.GetReferenceDateConstant import getRefDateConstant
from eventloop.GetAllItrCandlestickData import getAllItrCandlestickData
from eventloop.GetFirstItrCandlestickData import getFirstItrCandlestickData
import datetime

# calculation for reference time
c = getRefDateConstant("30 Oct 2023  09:35:00.000")

getFirstItrCandlestickData(300, "", "", c)
# getAllItrCandlestickData(300, "", "", c)

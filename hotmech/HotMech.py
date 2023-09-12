import pandas as pd
import xlwings as xw
from hotmech.GetHotMechLIst import *


def hotMech(uid, desc, symbol, sector, token, ltp):
    hm = getHotMechList()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import xlwings as xw

wb = xw.Book("../AngelOneSmartAPIApp/TA_Python.xlsm")
dt = wb.sheets("Exchange")

varS = pd.DataFrame(dt.range("a1:l202").value)
varS.columns = varS.iloc[0]
varS = varS[1:]

varS["id"] = varS["id"].astype("int64")

varS = varS.drop(columns=['symbol', 'token'])

print(varS["id"])


# options = Options()
# options.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
#                           options=options)
# url = "https://www.topstockresearch.com/PivotPoint/IntradaySupportAndResistanceUsingPivotPoint.html"
#
# driver.get(url)
# driver.maximize_window()

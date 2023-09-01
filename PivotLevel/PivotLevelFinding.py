from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import xlwings as xw
# from GetSmallData import *

# smD = getSmallData()
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
url = "https://www.topstockresearch.com/PivotPoint/IntradaySupportAndResistanceUsingPivotPoint.html"

driver.get(url)
driver.maximize_window()

# rows = driver.find_element(By.CSS_SELECTOR, "#results tbody tr")

rows = driver.find_elements(By.CSS_SELECTOR, "#results tbody tr")

print(rows[1].find_elements(By.CSS_SELECTOR, "td")[1].text)

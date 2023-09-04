from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import xlwings as xw
from GetSmallData import *


def getPivot():
    smD = getSmallData()
    options = Options()
    options.add_experimental_option("detach", False)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                              options=options)
    url = "https://www.topstockresearch.com/PivotPoint/IntradaySupportAndResistanceUsingPivotPoint.html"

    driver.get(url)
    driver.maximize_window()

    # rows = driver.find_element(By.CSS_SELECTOR, "#results tbody tr")

    rows = driver.find_elements(By.CSS_SELECTOR, "#results tbody tr")

    # print(rows[1].find_element(By.CSS_SELECTOR, "a").text)
    itr = 0
    for e in rows:
        desc = e.find_element(By.CSS_SELECTOR, "a").text
        if desc in smD['desc'].values:
            uid = smD.loc[(smD['desc'] == desc)]["id"]
            columns = e.find_elements(By.CSS_SELECTOR, "td")
            smD.loc[uid, "ltp"] = columns[1].text
            smD.loc[uid, "sr1"] = columns[2].text
            smD.loc[uid, "sr2"] = columns[3].text
            smD.loc[uid, "sr3"] = columns[4].text
            smD.loc[uid, "sr4"] = columns[5].text
            smD.loc[uid, "sr5"] = columns[6].text
            smD.loc[uid, "sr6"] = columns[7].text
            smD.loc[uid, "sr7"] = columns[8].text
            itr = itr + 1
            if itr > 199:
                break
    return smD

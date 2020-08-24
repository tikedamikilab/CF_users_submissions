# ユーザ名を取得する
# https://codeforces.com/ratings/page/1
# [['Um_nik', 109], ['tourist', 48]]

import pandas as pd
import urllib.request, urllib.error
from time import sleep
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--headless')
driver = webdriver.Chrome('C:\Program Files\Chrome Driver\chromedriver',options=options)

def makeCSVRatedUserNameList():
    page = 4
    baseURL = 'https://codeforces.com/ratings/page/'
    URL = baseURL + str(page)
    print(URL)

    data = pd.read_html(URL, header = 0)
    print(data[5]['Who'][0])

    submissionBaseURL = 'https://codeforces.com/submissions/'
    outputList = []

    for name in data[5]['Who']:
        submissionURL = submissionBaseURL + name
        driver.get(submissionURL)
        sleep(1)
        soup = BeautifulSoup(driver.page_source, features="html.parser")
            
        submissionMAX = [n.get_text() for n in soup.select('div ul li span')][-1]
        try:
            output =[name, int(submissionMAX)]
            print(output)
            outputList.append(output)
        except ValueError as e:
            print('catch KeyError:', e)
    print(outputList)

if __name__ == "__main__":
    makeCSVRatedUserNameList()
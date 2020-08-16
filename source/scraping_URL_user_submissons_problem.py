# ユーザが解いた問題のURLを全部集める

from time import sleep
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--headless')
driver = webdriver.Chrome('C:\Program Files\Chrome Driver\chromedriver',options=options)

# userName = 'tourist'
# start = 1
# end = 48
def makeCSVSubmissonsProblemURL(userName, start, end):
    baseURL = 'https://codeforces.com/submissions/'    

    for i in range(start , end + 1):
        URL = baseURL + userName + '/page/' + str(i)
        print(URL)

        driver.get(URL)
        sleep(1)
        soup = BeautifulSoup(driver.page_source, features="html.parser")
        
        ProblemURL =[n.get('href') for n in soup.select('tbody td[data-problemid] a[href]')]
        
        pd.DataFrame(ProblemURL).to_csv('./users_submissions/' + userName + '_submissons.csv', mode='a',index=None, header=None)

if __name__ == "__main__":
    makeCSVSubmissonsProblemURL('tourist', 1, 48)

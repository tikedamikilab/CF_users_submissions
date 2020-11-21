# 最大ページ数を取得 
#      問題やユーザ名ごとに最大数のページ数を取得
#      メインの入力データ用データを生成する
# 出力データ形式
#　　　[[target, maxpage]]
# 

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

def printTargetMAXPage(name, targetURL):
    driver.get(targetURL)
    sleep(1)
    soup = BeautifulSoup(driver.page_source, features="html.parser")
        
    submissionMAX = [n.get_text() for n in soup.select('div ul li span')][-1]
    
    try:
        output =[name, int(submissionMAX)]
        print(output)
    except ValueError as e:
        print('catch KeyError:', e)
    
if __name__ == "__main__":
    for i in range(1, 100):
        problemID = i
        BaseURL = "https://codeforces.com/problemset/status/"
        targetURL = BaseURL + str(problemID) + "/problem/" + 'A'
        
        printTargetMAXPage(problemID, targetURL)
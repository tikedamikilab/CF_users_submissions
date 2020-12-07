# ユーザが解いた問題のURLを全部集める
# 多分使わない？
#       ここで使われる : source\rate_change.py
# 
# 入力データ
#       userName = ユーザのID
#       start=スクレイピングを始めるページの番号．通常１
#       end= スクレイピングの終わりのページ．その人個人のページからMAXのページ番号を取得
#       ユーザページ例 : https://codeforces.com/submissions/tourist
# 
# 出力データ
#       /contest/615/problem/E
#
# 注意：フォルダは生成されない
# 注意：csvは上書き

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

def make_csv_submissons_url(userName, start, end):
    baseURL = 'https://codeforces.com/submissions/'    

    for i in range(start , end + 1):
        URL = baseURL + userName + '/page/' + str(i)
        print(URL)

        driver.get(URL)
        sleep(1)
        soup = BeautifulSoup(driver.page_source, features="html.parser")
        
        ProblemURL =[n.get('href') for n in soup.select('tbody td[data-problemid] a[href]')]
        submissions_result = [n.get_text() for n in soup.select('tbody td [class="submissionVerdictWrapper"]')]
        output = []
        for i in range(len(ProblemURL)):
            o = [ProblemURL[i], submissions_result[i]]
            output.append(o)
        pd.DataFrame(output).to_csv('./users_submissionURL/' + userName + '.csv', mode='a',index=None, header=None)

if __name__ == "__main__":

    userList = [
        
    ]
    make_csv_submissons_url('tourist', 1, 1)

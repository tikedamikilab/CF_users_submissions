# 最大ページ数を取得 
#      問題やユーザ名ごとに最大数のページ数を取得
#      メインの入力データ用データを生成する
# 入力データ
#      対象を指定する名前（他のプログラムで入力として使用する可能性あり）
#      スクレイピング対象のURL
#      動作確認済み : https://codeforces.com/problemset/status/1/problem/A
#                    https://codeforces.com/submissions/ユーザID
# 出力データ形式
#　　　[[target, maxpage]]
#     
#      問題1から100までのsubmissionページ数.md にあるようなデータがとれる
#   
# 対象のURLによっては下記
#          submissionMAX = [n.get_text() for n in soup.select('div ul li span')][-1]
# を書き換える必要性があるかも
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

def print_target_maxpage(name, targetURL):
    driver.get(targetURL)
    sleep(1)
    soup = BeautifulSoup(driver.page_source, features="html.parser")
        
    submissionMAX = [n.get_text() for n in soup.select('div ul li span')][-1]
    
    try:
        output =[name, int(submissionMAX)]
        print(output, end="")
        print(",", end="", flush=True)
    except ValueError as e:
        print('catch KeyError:', e)
    
if __name__ == "__main__":
    for i in range(1, 100):
        problemID = i
        BaseURL = "https://codeforces.com/problemset/status/"
        targetURL = BaseURL + str(problemID) + "/problem/" + 'A'
        
        print_target_maxpage(problemID, targetURL)
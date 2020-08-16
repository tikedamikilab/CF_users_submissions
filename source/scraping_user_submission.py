# scraping_user_submission
# CFからあるユーザのsubmissionsを取得 -> csvへ
#

import pandas as pd
from datetime import datetime as dt
import time
from urllib import request  # urllib.requestモジュールをインポート
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート

def makeUserSubmissionsCsv():
    start = 1
    end = 1
    userName = 'tourist'
    baseURL = 'https://codeforces.com/submissions/'
    
    for i in range(start , end + 1):
        URL = baseURL + userName + '/page/' + str(i)
        print(URL)

        data = pd.read_html(URL, header = 0)
        print(data)
        data[5].to_csv('./users_submissions/'+ userName +'.csv', header=False, index=False, mode='a')

if __name__ == "__main__":
    makeUserSubmissionsCsv()

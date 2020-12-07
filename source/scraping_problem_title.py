# 
# タイトルと問題番号をエンコード，デコードするためのデータ収集
# 一度使えば，2度使うことはないはず

import pandas as pd
import urllib.request, urllib.error

def make_csv_problem_title(start, end):
    
    baseURL = 'https://codeforces.com/problemset'
    
    for i in range(start , end + 1):
        URL = baseURL + '/page/' + str(i)
        print(URL)

        try:
            data = pd.read_html(URL, header = 0)
            data[0].to_csv('problem_title' +'.csv', header=False, index=False, mode='a')
        except urllib.error.HTTPError as e:
            print('catch KeyError:', e)
            data = pd.read_html(URL, header = 0)
            data[0].to_csv('problem_title' +'.csv', header=False, index=False, mode='a')

if __name__ == "__main__":
    make_csv_problem_title(1, 66)

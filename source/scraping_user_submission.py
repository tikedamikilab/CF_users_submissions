# scraping_user_submission
# ユーザデータ取得に関するメイン部分
#
# CFから指定したユーザのsubmissionsを取得 -> csvへ
# users_submissiomsに格納
#
# 注意 : csv追記
# 注意 : フォルダは作成されない
# 
# 入力データ形式
#      userList = [[ユーザ名, 最大ページ数], ['Um_nik', 109], ['tourist', 48]]
#
# 出力データ形式
#      指定フォルダにユーザ名ごとのcsvファイルが作成される
#      csvに以下の形式で追記される
#            89966600,Aug/14/2020 21:38,Um_nik,E - Hexagons,GNU C++17 (64),Accepted,234 ms,0 KB
#            89966282,Aug/14/2020 21:34,Um_nik,E - Decypher the String,GNU C++17 (64),Wrong answer on test 1,15 ms,100 KB
#      


import pandas as pd
import urllib.request, urllib.error

def make_csv_user_submissions(userName, start, end):
    
    baseURL = 'https://codeforces.com/submissions/'
    
    for i in range(start , end + 1):
        URL = baseURL + userName + '/page/' + str(i)
        print(URL)

        try:
            data = pd.read_html(URL, header = 0)
            data[5].to_csv('./users_submissions/'+ userName +'.csv', header=False, index=False, mode='a')
        except urllib.error.HTTPError as e:
            print('catch KeyError:', e)
            data = pd.read_html(URL, header = 0)
            data[5].to_csv('./users_submissions/'+ userName +'.csv', header=False, index=False, mode='a')

if __name__ == "__main__":
    userList = [
        ['SerVasilich', 29]
    ]
    for user in userList:
        make_csv_user_submissions(user[0], 1, user[1])



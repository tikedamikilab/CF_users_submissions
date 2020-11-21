# source\scraping_target_to_submissiontable.py
# scraping_user_submissionを汎用化したプログラム
#
# CFから指定したページからのsubmissionsを取得 -> csvへ
# 指定フォルダに格納
#
# 現状，dataNumを指定する必要があり，汎用化は上手くいっていない
# dataNumはdataをprintして欲しいtableがあるindexを指定する
#
# 注意 : csv追記
# 注意 : フォルダは作成されない
# 
# 必要データ
#      [[ターゲット, 最大ページ数], ]
#      ここからURLの生成を行う
# 
# 出力データ形式
#      指定フォルダにユーザ名ごとのcsvファイルが作成される
#            './users_submissions/'+ name +'.csv'
#            './' + outputFolder + '/'+ name +'.csv'
#      csvに以下の形式で追記される
#            89966600,Aug/14/2020 21:38,Um_nik,E - Hexagons,GNU C++17 (64),Accepted,234 ms,0 KB
#            89966282,Aug/14/2020 21:34,Um_nik,E - Decypher the String,GNU C++17 (64),Wrong answer on test 1,15 ms,100 KB
#

import pandas as pd
import urllib.request, urllib.error

def makeCSVTargetURL2SubmissionTable(name, targetURL, end, outputFolder,dataNum=0):
    
    for i in range(1, end + 1):
        URL = targetURL + '/page/' + str(i)
        print(URL)

        try:
            data = pd.read_html(URL, header = 0)
            # print(data)
            data[dataNum].to_csv('./' + outputFolder + '/'+ name +'.csv', header=False, index=False, mode='a')
        except urllib.error.HTTPError as e:
            print('catch KeyError:', e)
            data = pd.read_html(URL, header = 0)
            data[dataNum].to_csv('./' + outputFolder + '/'+ name +'.csv', header=False, index=False, mode='a')

if __name__ == "__main__":

    problemID = 1
    end = 1
    problemABCDEF = 'A'
    baseURL = "https://codeforces.com/problemset/status/"
    targetProblemURL = baseURL + str(problemID) + "/problem/" + problemABCDEF
    print(targetProblemURL)

    makeCSVTargetURL2SubmissionTable('problem_' + str(problemID) +'_A' ,targetProblemURL, end, "problem_submissions")

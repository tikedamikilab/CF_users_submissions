# ユーザデータを成型する
# ユーザのsubmissionを問題番号とタイトルに直す
# 
# 入力
# 100244194,Dec/03/2020 09:49,_ShadowSong,C - Two Brackets,GNU C++11,Accepted,31 ms,200 KB
# 100235100,Dec/03/2020 06:49,_ShadowSong,B - Toy Blocks,GNU C++11,Accepted,46 ms,400 KB
#
# 出力
# 一つのcsvに集約する
# ユーザ名, 時系列順解答問題番号,正答0誤答1のやつ
# 

import pandas as pd
import csv

def shaping_user_submission(userNameList):

    title = pd.read_csv('problem_title.csv', header=None)
    print(title)

    baseDir = '_3__submissions/'
    target = baseDir + userNameList[0] + '.csv'
    data = pd.read_csv(target, header=None)

    print(data)

if __name__ == "__main__":
    shaping_user_submission(["_ShadowSong"])
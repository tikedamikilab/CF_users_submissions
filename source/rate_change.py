# 解答した問題数を記録
# なにこれ？
# 注意 > pd.read_csv
#        読み込むcsvファイルはどこから？
#        ここで作成 : source\scraping_URL_user_submissons_problem.py
#        
# 注意 > json_open
#        読み込むjsonはcodeforces apiから手動で取得
# 　　　　おそらくここから : https://codeforces.com/api/user.rating?handle=Fefer_Ivan       
# 
# やってること
#       users_rate_change\ユーザ名_submissons.csv と
#       rate_ユーザ名.json を統合し
#       users_rate_change\ユーザ名_unique.csv に変換
# 
# データ形式を変更し別ファイルに保存（またはprint）
# /contest/1394/problem/D と
# {
    # "contestId": 1392,
    # "contestName": "Codeforces Global Round 10",
    # "handle": "tourist",
    # "rank": 4,
    # "ratingUpdateTimeSeconds": 1597599300,
    # "oldRating": 3515,
    # "newRating": 3506
# }, が
# 1394,D,3506 に変換
# 
# 


import pandas as pd
import csv
import json

def userSubmissionUnique(userName):
    # readするフォルダ名
    baseDir = 'users_rate_change/'
    target = baseDir + userName + '_submissons.csv'
    data = pd.read_csv(target, header=None)

    solvedList = []
    for submission in data[0]:
        if submission not in solvedList:
            solvedList.append(submission)

    json_target = baseDir + 'rate_' + userName + '.json'
    json_open = open(json_target, 'r')
    rate_change = json.load(json_open)

    maxlen = len(rate_change['result']) - 1

    output = []
    with open('./users_rate_change/' + userName + '_unique.csv', 'a', newline='') as f:
        for solved in solvedList:
            if int(solved.split('/')[2]) == int(rate_change['result'][maxlen]['contestId']):
                maxlen = maxlen - 1
            # ここからコンテスト以外の問題抽出
            if int(solved.split('/')[2]) != int(rate_change['result'][maxlen]['contestId']):
                if solved.split('/')[4] == 'A':
                    if int(solved.split('/')[2]) not in output:
                        output.append(int(solved.split('/')[2]))
            # writer = csv.writer(f)
            # writer.writerow([solved.split('/')[2], solved.split('/')[4], rate_change['result'][maxlen]['newRating']])
    print(output[::-1])
if __name__ == "__main__":
    userSubmissionUnique('BinZhao')
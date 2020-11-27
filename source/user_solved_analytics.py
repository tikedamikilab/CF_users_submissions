# source\scraping_user_solved_list.py
# 解答した問題数を記録
# 初期の分析において使用
#
# 入力データ
#       userName = 'tourist'
#       users : source\scraping_rated_username.pyで作成（source\scraping_user_submission.pyにコメントアウトで残ってる）
#       target csv : source\scraping_user_submission.py で作成
# 出力データ
#       ユーザ名，CF開始日時，submission数，正答問題数，submissionを行た日数


import pandas as pd
import csv

def user_submissions_analytics(userName):
    
    baseDir = 'users_submissions/'
    target = baseDir + userName + '.csv'
    data = pd.read_csv(target, header=None)

    solvedList = []
    for submission in data[3]:
        if submission not in solvedList:
            solvedList.append(submission)

    submissionDays = []
    for i in range(len(data)):
        tmp = data[1][i].split()[0]
        if tmp not in submissionDays:
            submissionDays.append(tmp)

    startDay = submissionDays[-1]

    with open('./users_analytics/userAnalytics.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([userName, startDay, len(data), len(solvedList), len(submissionDays)])

if __name__ == "__main__":
    users = [
        
    ]
    for user in users:
        user_submissions_analytics(user[0])

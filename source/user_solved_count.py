# source\user_solved_count.py
# ユーザが指定の範囲の問題を何問回答したか？
# 
# 入力データ
# source\scraping_target_to_submissiontable.py から解答ユーザの一覧
# 出力データ
# 各ユーザごとに指定の問題を何問正答しているか？


import pandas as pd
import csv

def user_solved_problem_count():
    
    baseDir = '_allusers_problem_submissions/'

    userList = []
    solvedcount = []
    targetList = [3,7,13,17,37,43,53,56,74,88,90]
    for i in targetList:
        fileName = "problem_"+str(i)+"_A.csv"
        print(fileName)
        target = baseDir + fileName
        data = pd.read_csv(target, header=None)

        problemUnique = []
        for user in data[2]:
            if user not in userList:
                userList.append(user)
                solvedcount.append(1)
            elif user not in problemUnique:
                problemUnique.append(user)
                solvedcount[userList.index(user)] += 1

    
    with open('./users_analytics/userSolvedCount.csv', 'a', newline='') as f:
        for i in range(0, len(userList)):
            try:
                writer = csv.writer(f)
                writer.writerow([userList[i], solvedcount[i]])
                if i%1000 == 0:
                    print(i)
            except UnicodeEncodeError as e:
                print('catch KeyError:', e)

if __name__ == "__main__":
        user_solved_problem_count()

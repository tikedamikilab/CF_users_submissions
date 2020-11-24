# source\
#
# 入力データ
# 出力データ


import pandas as pd
import csv

# userName = 'tourist'
# start = 1
# end = 48
def userSolvedProblemCount():
    
    baseDir = '_allusers_problem_submissions/'

    userList = []
    solvedcount = []

    for i in range(90, 101):
        fileName = "problem_"+str(i)+"_A.csv"
        print(fileName)
        target = baseDir + fileName
        data = pd.read_csv(target, header=None)
        
        problemUnique = []
        for user in data[2]:
            if user not in userList:
                
                userList.append(user)
                solvedcount.append(1)
            else:
                if user not in problemUnique:
                    problemUnique.append(user)
                    solvedcount[userList.index(user)] += 1

    with open('./users_analytics/userSolvedCount.csv', 'a', newline='') as f:
        for i in range(0, len(userList)):
            writer = csv.writer(f)
            writer.writerow([userList[i], solvedcount[i]])

if __name__ == "__main__":
        userSolvedProblemCount()

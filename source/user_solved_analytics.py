# source\scraping_user_solved_list.py
# 解答した問題数を記録

import pandas as pd
import csv

# userName = 'tourist'
# start = 1
# end = 48
def userSubmissionsAnalytics(userName):
    
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
        userSubmissionsAnalytics(user[0])

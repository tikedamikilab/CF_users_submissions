# 解答した問題数を記録

import pandas as pd
import csv

def userSubmissionUnique():
    userName = 'tourist'
    baseDir = 'users_rate_change/'
    target = baseDir + userName + '_submissons.csv'
    data = pd.read_csv(target, header=None)

    solvedList = []
    for submission in data[0]:
        if submission not in solvedList:
            solvedList.append(submission)

    with open('./users_rate_change/' + userName + '_unique.csv', 'a', newline='') as f:
        for solved in solvedList:
            writer = csv.writer(f)
            writer.writerow([solved.split('/')[2], solved.split('/')[4]])

if __name__ == "__main__":
    userSubmissionUnique()
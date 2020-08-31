# 解答した問題数を記録

import pandas as pd
import csv
import json

def userSubmissionUnique():
    userName = 'tourist'
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

    with open('./users_rate_change/' + userName + '_unique.csv', 'a', newline='') as f:
        for solved in solvedList:
            if int(solved.split('/')[2]) < int(rate_change['result'][maxlen]['contestId']):
                maxlen = maxlen - 1
            writer = csv.writer(f)
            writer.writerow([solved.split('/')[2], solved.split('/')[4], rate_change['result'][maxlen]['newRating']])

if __name__ == "__main__":
    userSubmissionUnique()
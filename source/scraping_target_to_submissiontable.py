# 
#
# チョット保留

import pandas as pd
import urllib.request, urllib.error

def makeCSVTargetURL2SubmissionTable(name, targetURL, end, ):
    
    for i in range(1, end + 1):
        URL = targetURL + '/page/' + str(i)
        print(URL)

        try:
            data = pd.read_html(URL, header = 0)
            data[5].to_csv('./users_submissions/'+ name +'.csv', header=False, index=False, mode='a')
        except urllib.error.HTTPError as e:
            print('catch KeyError:', e)
            data = pd.read_html(URL, header = 0)
            data[5].to_csv('./users_submissions/'+ name +'.csv', header=False, index=False, mode='a')

if __name__ == "__main__":

    problemID = 1
    end = 1
    problemABCDEF = 'A'
    baseURL = "https://codeforces.com/problemset/status/"
    targetProblemURL = baseURL + str(problemID) + "/problem/" + problemABCDEF
    print(targetProblemURL)

    makeCSVTargetURL2SubmissionTable(problemID ,targetProblemURL, end)

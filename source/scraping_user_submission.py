# scraping_user_submission
# CFからあるユーザのsubmissionsを取得 -> csvへ
# users_submissiomsに格納

import pandas as pd

def makeUserSubmissionsCsv():
    userName = 'Benq'
    start = 1
    end = 114
    
    baseURL = 'https://codeforces.com/submissions/'
    
    for i in range(start , end + 1):
        URL = baseURL + userName + '/page/' + str(i)
        print(URL)

        data = pd.read_html(URL, header = 0)
        data[5].to_csv('./users_submissions/'+ userName +'.csv', header=False, index=False, mode='a')

if __name__ == "__main__":
    makeUserSubmissionsCsv()

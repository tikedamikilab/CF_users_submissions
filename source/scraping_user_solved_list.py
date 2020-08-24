# source\scraping_user_solved_list.py
# 解答した問題数を記録

import pandas as pd

# userName = 'tourist'
# start = 1
# end = 48
def makeCSVUserSubmissions(userName, start, end):
    
    baseURL = 'https://codeforces.com/submissions/'
    
    solvedList = []
    for i in range(start , end + 1):
        URL = baseURL + userName + '/page/' + str(i)
        print(URL)

        data = pd.read_html(URL, header = 0)
        for title in data[5]['Problem']:
            if title not in solvedList:
                solvedList.append(title)
        # data[5].to_csv('./users_submissions/'+ userName +'.csv', header=False, index=False, mode='a')
    print(len(solvedList))
    

if __name__ == "__main__":
    makeCSVUserSubmissions('tourist', 1, 48)

# scraping_user_submission
# CFからあるユーザのsubmissionsを取得 -> csvへ
# users_submissiomsに格納

import pandas as pd
import urllib.request, urllib.error

# userName = 'tourist'
# start = 1
# end = 48
def makeCSVUserSubmissions(userName, start, end):
    
    baseURL = 'https://codeforces.com/submissions/'
    
    for i in range(start , end + 1):
        URL = baseURL + userName + '/page/' + str(i)
        print(URL)

        try:
            data = pd.read_html(URL, header = 0)
            data[5].to_csv('./users_submissions/'+ userName +'.csv', header=False, index=False, mode='a')
        except urllib.error.HTTPError as e:
            print(e)
            data = pd.read_html(URL, header = 0)
            data[5].to_csv('./users_submissions/'+ userName +'.csv', header=False, index=False, mode='a')

if __name__ == "__main__":
    userList = [
        
    ]

    for user in userList:
        makeCSVUserSubmissions(user[0], 1, user[1])


# ['Um_nik', 109], ['tourist', 48], ['ecnerwala', 84], ['Benq', 115], ['boboniu', 3],
# ['maroonrk', 38], ['Petr', 29], ['ksun48', 115], ['TLE', 54], ['scott_wu', 66],
# ['Radewoosh',128], ['WZYYN', 79], ['yosupo', 63], ['fateice', 11], ['apiadu', 45],
# ['tEMMIE.w.', 26], ['SkyDec', 61], ['neal', 93], ['molamola.', 42], ['peehs_moorhsum', 14],
# ['Egor', 59], ['300iq', 108], ['Marcin_smu', 54], ['mnbvmar', 50], ['jiangly', 65],
# ['Merkurev', 74], ['hos.lyric', 44], ['gisp_zjz', 42], ['Endagorion', 40], ['cuizhuyefei', 44]
# ['zhouyuyang', 42], ['tlwpdus', 13], ['ko_osaga', 84], ['KAN', 31], ['ainta', 90],
# ['LHiC', 51], ['whzzt', 30], ['FizzyDavid', 64], ['zeronumber', 3], ['kczno1', 15]

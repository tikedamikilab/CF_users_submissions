# 解答した問題数を記録
# なにこれ？
# 注意 > pd.read_csv
#        ここで作成 : source\scraping_URL_user_submissons_problem.py   
# 
# やってること
# 
# 
# データ形式を変更し別ファイルに保存（またはprint）
# RNNへの入力用データ作成
# 
# 


import pandas as pd
import csv
import json

def shaping_url_user_submission(userName, filename):
    # readするフォルダ名
    baseDir = '_6_users_submissionURL/'
    target = baseDir + userName + '.csv'
    data = pd.read_csv(target, header=None)

    output = []
    # output = [userName]
    for i, d in data.iterrows():
        contestID, contestABCDEF = d[0].split('/')[2], d[0].split('/')[4][0]
        result = d[1]

        if contestID == '3' or contestID == '7' or contestID == '13' or contestID == '17' or contestID == '37' or contestID == '43' or contestID == '53' or contestID == '56' or contestID == '74' or contestID == '88' or contestID == '90':
            if contestABCDEF == 'A':
                # output = (encodeing_result(result) + contestABCDEF + contestID) + ' ' + output
                output.append(encodeing_result(result) + contestABCDEF + contestID)

    with open('./shaping_encoding_URL/' + filename + '.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(output)

def encodeing_result(result):
    if result == 'Accepted':
        return str(0)
    else:
        return str(1)

def encoding_abcdef(abcdef):
    abcdef_index = {'A':'00', 'B':'01', 'C':'02', 'D':'03', 'E':'04', 'F':'05', 'G':'06', 'H':'07', 'I':'08',
                    'J':'09', 'K':'10', 'L':'11', 'M':'12', 'N':'13', 'O':'14', 'P':'15', 'Q':'16', 'R':'17',
                    'S':'18', 'T':'19', 'U':'20', 'V':'21', 'W':'22', 'X':'23', 'Y':'24', 'Z':'25'}
    return str(abcdef_index[abcdef])

if __name__ == "__main__":
    userList = [
        
    ]
    for user in userList:
        shaping_url_user_submission(user[0], 'dumyfilename')
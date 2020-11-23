# source\scraping_target_to_submissiontable.py
# scraping_user_submissionを汎用化したプログラム
#
# CFから指定したページからのsubmissionsを取得 -> csvへ
# 指定フォルダに格納
#
# 現状，dataNumを指定する必要があり，汎用化は上手くいっていない
# dataNumはdataをprintして欲しいtableがあるindexを指定する
#
# 注意 : csv追記
# 注意 : フォルダは作成されない
# 
# 必要データ
#      [[ターゲット, 最大ページ数], ]
#      ここからURLの生成を行う
# 
# 出力データ形式
#      指定フォルダにターゲットごとのcsvファイルが作成される
#            './users_submissions/'+ name +'.csv'
#            './' + outputFolder + '/'+ name +'.csv'
#      csvに以下の形式で追記される
#            89966600,Aug/14/2020 21:38,Um_nik,E - Hexagons,GNU C++17 (64),Accepted,234 ms,0 KB
#            89966282,Aug/14/2020 21:34,Um_nik,E - Decypher the String,GNU C++17 (64),Wrong answer on test 1,15 ms,100 KB
#

import pandas as pd
import urllib.request, urllib.error
import time

def makeCSVTargetURL2SubmissionTable(name, targetURL, start, end, outputFolder,dataNum=0):
    
    for i in range(start, end + 1):
        URL = targetURL + '/page/' + str(i)
        print(URL)
        time.sleep(2)
        try:
            data = pd.read_html(URL, header = 0)
            # print(data)
            data[dataNum].to_csv('./' + outputFolder + '/'+ name +'.csv', header=False, index=False, mode='a')
        except urllib.error.HTTPError as e:
            print('catch KeyError:', e)
            data = pd.read_html(URL, header = 0)
            data[dataNum].to_csv('./' + outputFolder + '/'+ name +'.csv', header=False, index=False, mode='a')

if __name__ == "__main__":
    targetlist = [
        # [1, 3131],[2, 313],[3, 279],[4, 4522],[5, 139],[6, 278],[7, 110],[8, 83],[9, 478],[10, 81],[11, 147],[12, 147],[13, 106],[14, 139],[15, 52],[16, 173],[17, 167],[18, 82],[19, 43],[20, 86],
        # [21, 28],[22, 217],[23, 79],[24, 70],[25, 801],[26, 287],[27, 224],[28, 14],[29, 99],[30, 51],[31, 118],[32, 123],[33, 87],[34, 256],[35, 92],[36, 49],[37, 316],[38, 264],[39, 11],[40, 46],[41, 1125],[42, 45],[43, 420],[44, 82],[45, 65],[46, 115],[47, 189],[48, 73],[49, 167],[50, 1947],
        # [51, 30],[52, 90],[53, 70],[54, 33],[55, 55],[56, 110],[57, 49],[58, 1260],[59, 1169],[60, 51],
        # [61, 876],[62, 61],[63, 162],[64, 11],[65, 35],[66, 106],[67, 34],[68, 82],[69, 1347],[70, 57],[71, 2986],[72, 3],[73, 23],[74, 71],[75, 274],[76, 23],[77, 33],[78, 128],[79, 62],[80, 386],[81, 120],[82, 478],[83, 91],[84, 208],[85, 30],[86, 19],[87, 75],[88, 60],[89, 31],[90, 67],[91, 64],[92, 243],[93, 42],[94, 143],[95, 32],[96, 1514],[97, 4],[98, 24],[99, 89]
        [100, 8]
    ]

    # problemID = 50
    # targetProblemURL = "https://codeforces.com/problemset/status/"+str(problemID)+"/problem/A"
    # makeCSVTargetURL2SubmissionTable('problem_' + str(problemID) +'_A' ,targetProblemURL, 1489, 1497, "problem_submissions")    

    for target in targetlist:
        problemID = target[0]
        end = target[1]
        problemABCDEF = 'A'
        baseURL = "https://codeforces.com/problemset/status/"
        targetProblemURL = baseURL + str(problemID) + "/problem/" + problemABCDEF

        makeCSVTargetURL2SubmissionTable('problem_' + str(problemID) +'_A' ,targetProblemURL, 1, end, "problem_submissions")

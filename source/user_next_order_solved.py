# source\scraping_user_solved_list.py
# 特定の問題の次，どの問題を解答しどの結果だったかを記録
# RNNの予測との比較において使用
#
# 入力データ
# 
# 出力データ
# 



import pandas as pd
import csv
import numpy as np

from tensorflow import keras

def user_next_order_solved(target):
    edgewight = np.zeros((22+1,22+1))

    with open(target) as inputfile:
        users_submissions = csv.reader(inputfile, delimiter = ',')
        l = [row for row in users_submissions]

    users_submissions = np.array(l)
    users_submissions = keras.preprocessing.sequence.pad_sequences(users_submissions, padding='post', maxlen=50)

    print(users_submissions[0])
    print(encoding_problemid2index(str(0)))
    for user_submissions in users_submissions:
        for i in range(len(user_submissions)-1):
            edgewight[encoding_problemid2index(user_submissions[i])][encoding_problemid2index(user_submissions[i+1])] += 1
        
    df = pd.DataFrame(edgewight)
    df.to_csv("TesEdgeWight.csv", index=False, encoding="utf-8", header=False)                

def encoding_problemid2index(problemid):
    problemid2index ={
        '0':0, '3000':1,'3001':2,'7000':3,'7001':4,'13000':5,'13001':6,'17000':7,'17001':8,'37000':9,'37001':10,
        '43000':11,'43001':12,'53000':13,'53001':14,'56000':15,'56001':16,'74000':17,'74001':18,'88000':19,'88001':20,'90000':21,'90001':22, 
    }
    return int(problemid2index[str(problemid)])

if __name__ == "__main__":
    baseDir = 'shaping_encoding_URL/'
    
    target = baseDir + '8-10mon_2' + '.csv'

    user_next_order_solved(target)

# scraping_user_submission
# ユーザデータ取得に関するメイン部分
#
# CFから指定したユーザのsubmissionsを取得 -> csvへ
# users_submissiomsに格納
#
# 注意 : csv追記
# 注意 : フォルダは作成されない
# 
# 入力データ形式
#      userList = [[ユーザ名, 最大ページ数], ['Um_nik', 109], ['tourist', 48]]
#
# 出力データ形式
#      指定フォルダにユーザ名ごとのcsvファイルが作成される
#      csvに以下の形式で追記される
#            89966600,Aug/14/2020 21:38,Um_nik,E - Hexagons,GNU C++17 (64),Accepted,234 ms,0 KB
#            89966282,Aug/14/2020 21:34,Um_nik,E - Decypher the String,GNU C++17 (64),Wrong answer on test 1,15 ms,100 KB
#      
#
# dataのインデックス変える必要が出てくると思われ

import pandas as pd
import urllib.request, urllib.error

def make_csv_user_submissions(userName, start, end):
    
    baseURL = 'https://codeforces.com/submissions/'
    
    for i in range(start , end + 1):
        URL = baseURL + userName + '/page/' + str(i)
        print(URL)

        try:
            data = pd.read_html(URL, header = 0)
            data[0].to_csv('./users_submissions/'+ userName +'.csv', header=False, index=False, mode='a')
        except urllib.error.HTTPError as e:
            print('catch KeyError:', e)
            data = pd.read_html(URL, header = 0)
            data[0].to_csv('./users_submissions/'+ userName +'.csv', header=False, index=False, mode='a')

if __name__ == "__main__":
    userList = [
        ['Amores', 29],['Sali_adelkhah', 64],['daidailanlan', 40],['yzyejh', 14],['latvian', 36],['hakobyan.tigran', 37],['sazzad', 17],['TempuX', 24],['Momentum', 81],['Trish', 14],['juarez.paulino', 28],['dragonslayerintraining', 67],['Sereja', 75],['stryan123', 12],['agat00', 8],['The_CodeBreakeR', 32],['K_operafan', 22],['kbl_didi_ridi', 36],['Sor8sh_tm', 24],['Toshik', 67],['merolish', 47],['darry140', 34],['Dalisyron', 58],['t.janssen52', 25],['iShibly', 123],['KhaledMuhammad', 82],['YakutovDmitriy', 89],['lehar_11', 5],['apple_juice', 16],['MetaBro', 23],['7Midav7', 35],['Yousef_Salama', 91],['david_varela', 51],['raynor30', 66],['vikram.gaur', 12],['vode', 21],['Alhelal_01', 108],['mongolrgata', 54],['shio', 52],['nise_nabe', 20],['poopi', 39],['lyrics', 24],['franckmy', 48],['b_r', 14],['arshak.khoshnevis', 51],['bluemmb', 64],['heliatk', 40],['mashashma',17],['Wholewheatbread', 32],['Aidos', 148],['mirsaid_mir', 38],['Ahmed_Salama', 56],['LIWKaguya', 38],['actium', 66],['Shinchan_Thakur', 35],['Damir', 17],['fuck_acm', 14],['enoyhs', 7],['peter50216', 36],['No_Use_Anymore', 64],['ET_', 26],['JoKe', 12],['bdtiger', 6],['rdiachenko', 45],['OmarHashim', 87],['chauhain', 44],['AleksanderBalobanov', 185],['eagle93', 90],['luckyi', 41],['amylase', 17],['Meraxes', 25],['KBL', 46],['vvenkai', 36],['kujta1', 24],['-Morass-', 145],['pva701', 47],['charity', 104],['c5xheavy', 50],['Stratonov', 69],['aliasadiiii', 112],['Lightless', 75],['peking2', 31],['valikluks1995', 18],['koder_dima', 20],['wackloner', 35],['Zahidul_Islam', 74],['_HossamYehia_', 212],['Zool', 89],['ruo', 189],['Sofyana', 47],['codeforces_judge', 55],['maksay', 58],['Zhandos', 19],['Carlos', 67],['ddd', 10],['lihaitao', 18],['HassanRezk', 45],['Bugman', 99],['Hackson', 24],['tugushka', 45],['sonhuytran', 10],['sroyal', 57],['Malinovsky239', 50],['urusant', 79],['vepifanov', 96],['Jicote', 26],['safarisoul', 42],['mc_mosa', 48],['rexim', 27],['0w1', 111],['QZAR', 21],['atetubou', 40],['tomdmitriev', 36],['Thasin_Sheikh', 90],['Filins', 23],['ahmad_mamdouh', 48],['dreamjaded', 9],['ebedkm', 17],['semicfly', 17],['havaliza', 62],['Mosyagin', 95],['Root', 18],['Frez', 87],['mirianashvili', 21],['al13pn', 37],['Lvitsa', 53],['p3rfect', 52],['TiChuot97', 54],['draconiun', 43],['daizhenyang', 38],['kennethsnow', 53],['jomatt', 55],['kefaa', 132],['FilipVesovic', 53],['tamir', 43],['marque', 18],['Slamur', 101],['unrated', 16],['abistrigova#', 188],['AnnemaMissa', 12],['Marishka', 7],['dalex', 58],['Rex-myFriendForever', 23],['serhatgiydiren', 82],['301_anky', 34],['prodipdatta7', 161],['Qazaqstan', 20],['justHusam', 76],['abd.yerzhan', 26],['Arsenal911', 34],['Natali', 26],['pitfall', 115],['I.A.K.O.V', 43],['Sinner', 37],['userlond', 14],['Nadezhda', 14],['nevergiveup', 55],['_Noor', 37],['voquocthang', 41],['jrjahed100', 69],['HappyNewYearMike', 52]
    ]

    for user in userList:
        make_csv_user_submissions(user[0], 1, int(user[1]))

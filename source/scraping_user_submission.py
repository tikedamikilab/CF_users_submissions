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
            #['______i______', 52],['dragonmas', 46],['Alex_Wei', 45],['sri_akshya_18', 63],['code06', 15],['Stronger2020', 25],['route150', 13],['ekaterine2017', 34],['elina.nouri300', 24],['Master_Prog', 13],['scorpion', 90],['Shadowest', 14],['orailly', 87],['TEAs', 74],['Keerill', 9],['bnuvjudge', 338],['baezilisK', 18],['MatteoJug', 13],['Sahaand', 58],['KartalKaan', 15],['Vlad_kv', 71],['Hyppocrat', 22],['LordArian', 42],['zec23456', 27],['Mohammadreza_mz', 61],['Arima', 45],['july', 19],['A.c.lion', 10],['cool_handle_much_wow', 29],['aan93', 29],['greenhope', 15],['vmp', 15],['fanatid', 10],['sainiarpit12', 47],['YukiSora', 7],['_tiger_', 51],['BaherZ', 34],['Sadra', 81],['ZEROm', 27],['yano0oyan', 24],['Muh', 101],
            ['__ivan__', 51],['vinitgandhi007', 29],['self_healing', 17],['ian9696', 49],['FedyuninV', 18],['Victoralin10', 27],['JetAn', 11],['fancy', 9],['Eric_Valdivia', 21],['bubnov', 24],['abacadaea', 26],['ximo', 33],['Shersh', 10],['Danial', 89],['marut', 24],['ggaammeerr', 9],['ridhishjain', 15],['JeffreyHui', 14],['jcomputer000', 19],['chriscode_8', 8],['di_halt', 127],['jack_mk', 34],['minhquaningenious', 34],['buko', 33],['Hodobox', 35],['Cardi', 17],['ya_hossein', 51],['lys1280023', 47],['kavsub', 3],['sr_k', 10],['htrinh', 43],['Armanyss', 22],['Nickname124', 48],['pernay', 8],['cup_of_tea', 63],['fsb4000', 7],['iankury', 57],['alperen', 4],['Axelandpixel', 8],['zinai_boboyang', 6],['AndreiBiruk', 12],['lxrtxdy', 36],['Mystogan', 9],['Betlista', 16],['marcel.windys', 3],['PedramAghazadeh', 79],['mohammedehab2002', 60],['A.Grishchenko', 5],['hogeover30', 78],['Ezhik', 20],['AU.Bahosain', 69],['Alex_KPR', 16],['Koblyk', 63],['binh95', 9],['yermak0v', 103],['lemonsuper', 14],['251083874', 14],['patsp', 7],['cacophonix', 41],['snrahul', 40],['caozhexyz', 3],['thphong', 26],['Hoda_Hisham', 65],['Ac-93', 70],['ashmelev', 42],['ashcodish', 66],['MarwanPP', 23],['I-juice', 30],['rinigan', 48],['vish', 9],['MJavad', 12],['spark_coder', 5],['TranCongDuy', 25],['pasha', 13],['priyanka_14', 21],['alishaterian', 49],['cuiaoxiang', 104],['Spacejoker', 28],['gmunkhbaatarmn', 15],['beyondxgb', 26],['chenbinghui1', 6],['SandyKarunia', 35],['S.Yesipenko', 32],['Arpan_Bhowmik', 96],['DotACM', 15],['sokian', 94],['Omelianenko', 149],['Azizul_cse27', 51],['maksim.banin', 16],['stevegregg', 29],['Solix', 42],['hosseinhashemi', 29],['WeHaveInt', 141],['LocknKey', 59],['tusher', 22],['Ilnur_the_best', 80],['Neverauskas', 20],['Abra', 26],['LintuStorm', 49],['Respect2D', 12],['takaramono', 26],['Soroosh', 38],['Killer45', 66],['the_expandable', 19],['A.K.Goharshady', 25],['SkorKNURE', 23],['_jte_', 31],['aakashkhatri', 13],['nagasaisujan160998', 62],['Nodir.Daminov', 65]
        ]

    for user in userList:
        make_csv_user_submissions(user[0], 1, int(user[1]))

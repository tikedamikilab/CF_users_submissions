# ユーザが解いた問題のURLを全部集める
#       ここで使われる : source\rate_change.py
# 
# 入力データ
#       userName = ユーザのID
#       start=スクレイピングを始めるページの番号．通常１
#       end= スクレイピングの終わりのページ．その人個人のページからMAXのページ番号を取得
#       ユーザページ例 : https://codeforces.com/submissions/tourist
# 
# 出力データ
#       /contest/615/problem/E,採点結果
#
# 出力データは時系列と逆なので注意（インデックス小さい方が新しい）
#
# 注意：フォルダは生成されない
# 注意：csvは上書き

from time import sleep
from bs4 import BeautifulSoup  # BeautifulSoupクラスをインポート
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--headless')
driver = webdriver.Chrome('C:\Program Files\Chrome Driver\chromedriver',options=options)

def make_csv_submissons_url(userName, start, end):
    baseURL = 'https://codeforces.com/submissions/'    

    for i in range(start , end + 1):
        URL = baseURL + userName + '/page/' + str(i)
        print(URL)

        driver.get(URL)
        sleep(1)
        soup = BeautifulSoup(driver.page_source, features="html.parser")
        
        ProblemURL =[n.get('href') for n in soup.select('tbody td[data-problemid] a[href]')]
        submissions_result = [n.get_text() for n in soup.select('tbody td [class="submissionVerdictWrapper"]')]
        output = []
        for i in range(len(ProblemURL)):
            o = [ProblemURL[i], submissions_result[i]]
            output.append(o)
        pd.DataFrame(output).to_csv('./users_submissionURL/' + userName + '.csv', mode='a',index=None, header=None)

if __name__ == "__main__":

    userList = [
            ['______i______', 52],['dragonmas', 46],['Alex_Wei', 45],['sri_akshya_18', 63],['code06', 15],['Stronger2020', 25],['route150', 13],['ekaterine2017', 34],['elina.nouri300', 24],['Master_Prog', 13],['scorpion', 90],['Shadowest', 14],['orailly', 87],['TEAs', 74],['Keerill', 9],['bnuvjudge', 338],['baezilisK', 18],['MatteoJug', 13],['Sahaand', 58],['KartalKaan', 15],['Vlad_kv', 71],['Hyppocrat', 22],['LordArian', 42],['zec23456', 27],['Mohammadreza_mz', 61],['Arima', 45],['july', 19],['A.c.lion', 10],['cool_handle_much_wow', 29],['aan93', 29],['greenhope', 15],['vmp', 15],['fanatid', 10],['sainiarpit12', 47],['YukiSora', 7],['_tiger_', 51],['BaherZ', 34],['Sadra', 81],['ZEROm', 27],['yano0oyan', 24],['Muh', 101],['__ivan__', 51],['vinitgandhi007', 29],['self_healing', 17],['ian9696', 49],['FedyuninV', 18],['Victoralin10', 27],['JetAn', 11],['fancy', 9],['Eric_Valdivia', 21],['bubnov', 24],['abacadaea', 26],['ximo', 33],['Shersh', 10],['Danial', 89],['marut', 24],['ggaammeerr', 9],['ridhishjain', 15],['JeffreyHui', 14],['jcomputer000', 19],['chriscode_8', 8],['di_halt', 127],['jack_mk', 34],['minhquaningenious', 34],['buko', 33],['Hodobox', 35],['Cardi', 17],['ya_hossein', 51],['lys1280023', 47],['kavsub', 3],['sr_k', 10],['htrinh', 43],['Armanyss', 22],['Nickname124', 48],['pernay', 8],['cup_of_tea', 63],['fsb4000', 7],['iankury', 57],['alperen', 4],['Axelandpixel', 8],['zinai_boboyang', 6],['AndreiBiruk', 12],['lxrtxdy', 36],['Mystogan', 9],['Betlista', 16],['marcel.windys', 3],['PedramAghazadeh', 79],['mohammedehab2002', 60],['A.Grishchenko', 5],['hogeover30', 78],['Ezhik', 20],['AU.Bahosain', 69],['Alex_KPR', 16],['Koblyk', 63],['binh95', 9],['yermak0v', 103],['lemonsuper', 14],['251083874', 14],['patsp', 7],['cacophonix', 41],['snrahul', 40],['caozhexyz', 3],['thphong', 26],['Hoda_Hisham', 65],['Ac-93', 70],['ashmelev', 42],['ashcodish', 66],['MarwanPP', 23],['I-juice', 30],['rinigan', 48],['vish', 9],['MJavad', 12],['spark_coder', 5],['TranCongDuy', 25],['pasha', 13],['priyanka_14', 21],['alishaterian', 49],['cuiaoxiang', 104],['Spacejoker', 28],['gmunkhbaatarmn', 15],['beyondxgb', 26],['chenbinghui1', 6],['SandyKarunia', 35],['S.Yesipenko', 32],['Arpan_Bhowmik', 96],['DotACM', 15],['sokian', 94],['Omelianenko', 149],['Azizul_cse27', 51],['maksim.banin', 16],['stevegregg', 29],['Solix', 42],['hosseinhashemi', 29],['WeHaveInt', 141],['LocknKey', 59],['tusher', 22],['Ilnur_the_best', 80],['Neverauskas', 20],['Abra', 26],['LintuStorm', 49],['Respect2D', 12],['takaramono', 26],['Soroosh', 38],['Killer45', 66],['the_expandable', 19],['A.K.Goharshady', 25],['SkorKNURE', 23],['_jte_', 31],['aakashkhatri', 13],['nagasaisujan160998', 62],['Nodir.Daminov', 65]
        ]
    for user in userList:
        make_csv_submissons_url(user[0], 1, user[1])

# ユーザが解いた問題のURLを全部集める
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
            ['Mostafa_Khaled_Robot', 2],['zapdospops', 63],['ET_TMN', 4],['Akmoyu', 20],['MajAK', 30],['meme_lord', 59],['Rustam1111', 59],['ImagineWarrior', 29],['krishna369', 52],['sona_444', 5],['slycelote', 34],['out0fbounds', 18],['rincewind', 15],['b.moogii09', 28],['Uyghur', 3],['Daniar', 135],['xxxyyyzzz', 25],['knavadeep99', 23],['qua_intrelle7', 14],['I_See_You', 61],['satoshii', 10],['Dhruv25', 51],['tmxk', 5],['Wael.Al.Jamal', 86],['Isfandiyor', 46],['Yazdan_ra', 37],['mahmouder', 13],['xim97', 22],['sbasrik', 16],['Tuitkf', 18],['Light_Yagami', 11],['OrlandoIsay', 47],['asdfqwertyiop', 5],['abhi', 8],['nikalosa', 5],['de_troit', 17],['Zhuravlyov.A', 21],['Munkhdulguun1', 8],['Mahdi_Jfri', 50],['AmanyGamal', 9],['xhae', 29],['saichandu6', 57],['the_amazon14', 34],['CLown1331', 83],['irakli-janiashvili', 6],['rainboy', 134],['Anji', 53],['_ethereal_', 26],['carlosramirez', 10],['keivan', 33],['NeverSpec', 39],['LayCurse', 56],['MarcosK', 193],['Parhomets', 17],['DanMaklen', 11],['MhmdAssem67', 31],['DevJewel', 31],['Suraj_Yadav', 19],['menonsahab', 11],['hznu4', 67],['maratonando3', 264],['tinyguyYY', 10],['sinak03', 48],['Mohammad_Mohsin_COU', 20],['bor.is', 28],['dyrroth', 28],['Deathly_Hallows', 107],['ppaarsa', 72],['sdibt4', 80],['TankEngineer', 58],['Aman', 20],['THE_SABRES_OF_PARADISE', 30],['_KMS_', 30],['remonhasan', 9],['KH18', 8],['china_wxp', 4],['Tornado_2004', 4],['abdo.gamal.coder', 13],['Joker1010123', 62],['kyuridenamida', 55],['amollfc', 55],['Batja_15', 54],['i_love_hamster', 54],['Lakh', 42],['AFGhazy', 46],['hmzsalem39', 22],['wil93', 22],['ftiasch', 55],['Attobyte', 17],['m.r.m', 38],['Mehedihasanprodhan', 38],['Gotzillaz', 36],['Mrbeaches', 4],['auroral.adam', 11],['yang_bro', 5],['Jack5505', 60],['antonkov', 47],['zmitser.ch', 6],['Gassa', 68],['abdelhafiez8080', 35],['sdibt1', 80],['aryanv', 69],['travm12', 27],['Rubanenko', 67],['dby', 11],['Elibay', 133],['Kaneki_04', 24],['Ra16bit', 62],['Princ_iple', 118],['calm_ankush', 22],['You_Know_Who', 22],['unbelievable02', 69],['kenimo', 16],['MarioYC', 40],['aerohit', 3],['MohamedZain', 78],['SamuelLim', 45],['nitvjudge1', 40],['Salo7a', 43],['parsaalimohammadi', 43],['fafal_abnir', 41],['MahdiGheidi', 35],['ViNDeX', 11],['secretlearner.68', 36],['tntan1106', 16],['sephiloss', 22],['saurabh18', 5],['H3X', 24],['dalia_bolla', 9],['Protik_chakroborty', 20],['samiha_akter', 16],['mk74rus', 6],['Fritz_97', 26],['Stebaev', 19],['LeGross', 61],['IDDMX', 9],['Printemps.o', 13],['nguyenmanhphuc', 25],['Son-Goku', 17],['okcd00', 4],['abhithekid', 6],['Azox', 8],['foucault', 8],['redchrom', 14],['aminnajafvand', 32],['Spacelessd', 14],['olga.zhasan', 7],['KerollosAsaad', 26],['Progger', 13],['mohamed103', 5],['2222', 20],['MaxBjj', 6],['Nikiktafokusnik', 21],['rlac', 24],['hssh', 16],['root000', 25],['EmK', 11],['Solve_Every_Where', 70],['bahar.f1', 27],['iSlava', 67],['F202130100', 36],['am1998', 9],['ald', 9],['aadishj02', 59],['tflave', 24],['ilovemymind', 12],['alberttoshiro', 17],['shreyas_710', 17],['Ancient_mage', 110],['Credit_Card_CRD', 110],['Sabelan', 14],['ft.azadi', 14],['ApacheEx', 14],['Urbanowicz', 8],['atubo', 14],['Thanya_Leif', 42],['huansuz1', 32],['Steps09', 8],['kamjustas', 21],['kastellanos', 7],['omar_abdalrazik', 15],['Dalenator', 132],['SonOfBits', 47],['shohaghsust', 40],['flyasdfvcxz', 23],['ernestfan', 25],['green_eagle131', 22],['trax_2703', 17],['Ayanical', 17],['upfeed', 5],['caro33', 16],['KayvanMazaheri', 13],['The_old_man', 17],['tmphndl', 7],['Hiasat', 112],['rfpermen', 94],['dmitrydyatlov', 7],['todo', 19],['lxt1996', 5],['cpy', 24],['tus-team', 9],['SaMer', 45],['kshj78', 85],['Kareem_Mohamed', 70],['cup_of_tea#', 63],['abdelkarim', 52],['wh1te_whale', 38],['GusztavSzmolik', 26],['Brainless_Loco', 34],['szh123', 20],['Amireza', 105],['P___', 66],['AngrySeal', 36],['KhaledEltahan', 23],['beginner1010', 62],['bit10011001', 20],['komiya', 17],['abtin-shahpoory', 26],['yas1r', 11],['Dr.Mac', 7],['Empty', 21],['SamirMohamed133', 23],['Hyoga', 4],['Eran', 67],['Waiter', 6],['tenshi_kanade#', 76],['tawfekhesham', 33],['ilikebarryallen', 36],['nevidomy', 8],['ckodser', 51],['Al-Motasem', 29],['mohanad93', 21],['Leonid', 19],['SpookyCookie', 11],['IRRAKLY', 3],['faraz.f', 30],['nikkcartwright', 3],['sprasanth2k', 38],['praneeth_ray', 13],['kuzmichev_dima', 32],['mosamir', 21],['Shahd_Moemen', 32],['linkinu', 14],['Best_sponge', 14],['Xristo19', 4],['sajjad.h', 46],['levani2019', 4],['hznu3', 67],['Keti13', 6],['jamnik', 33],['Pooya.Ml', 41],['lizirukh', 4],['tarek.nawara', 21],['kaushik.mv3', 16],['permin', 26],['L.I.S.', 12],['I_love_Malika', 105],['0p9o8i', 37],['KADR', 62],['saket', 4],['pt1989', 10],['kolya37', 11],['umangahuja11', 40],['arshia83sharifi', 40],['samshad.ru', 35],['Kammola', 71],['tasneemria', 19],['jAckAL_1586', 35],['essi', 61],['imrankane2005', 5],['Tafsir_Rahman', 36],['Khangal.B', 75],['anto777', 33],['danuwfna', 26],['Bekheit', 39],['spidercode12', 16],['Ayazbayev_D', 78],['liugang123', 8],['pco', 8],['eik0u', 18],['niranshi04', 12],['ConanKudo', 14],['Igor_Kudryashov', 32],['memphis0603', 14],['ishibashijun', 37],['goga12', 14],['_pallab_99', 31],['just_sara', 29],['A-Safarkhon', 38],['mona_hashem', 25],['theRabiulAwal', 37],['milderhc', 33],['DreadlockEugene', 5],['shivammate', 27],['TheRealYoussef', 17],['B_U_Rafi', 17],['aladdin3', 29],['sevenkplus', 37],['meetu1902', 20],['racsosabe', 92],['Uzumaki_Narutoo', 171],['SandorGarcia#', 60],['Vatsal53', 39],['indy256', 33],['av.driftking', 15],['FORHAD-SUST-BD', 9],['Emsawy', 81],['DragoonKiller', 15],['MyXoBeK', 4],['nonstop-baban', 37],['Avi_2506', 37],['ayesha49', 26],['Oporajita', 19],['NavneetLohia', 35],['Babanin_Ivan', 21],['abhiruchi16', 17],['oblivious_z', 17],['RezaSi', 24],['AbduSharif', 47],['BlackEagle', 4],['viks176', 15],['kancha', 8],['dGreen', 32],['Skady', 7],['err0r', 110],['yadavsunil00001', 7],['Indecchi', 46],['simsa.st', 19],['thaherkhan', 11],['naagi', 27],['supernour09', 42],['anpicasso.r', 5],['lXTobiXl', 46],['smi', 9],['islamhamdi', 11],['AliAbdallah', 13],['niquefa', 3],['Ab_Sabaa', 21],['IamRD', 17],['gurpreet_ait', 43],['wilbertliu', 5],['NaDaAshraf', 50],['nagochan', 9],['Dias', 16],['wasyapetya', 19],['naihuangbao', 5],['vudduu', 11],['MuhammadAk_14', 11],['ThSonNguyen', 19],['Xorand', 5],['Utka', 16],['chitose', 5],['Badhon', 14],['urahara#', 37],['ghooo', 40],['mylyanyk.ivan', 43],['cgy4ever', 49],['mamhh', 5],['QuRdAdZe', 25],['ddx01', 33],['z_karaulashvili', 52],['scottai1', 22],['amanxstriker', 22],['bit-2', 12],['kamrul_brur', 25],['Ola.Abdallah', 51],['Gemy18', 20],['pioneer', 9],['asif_iut', 13],['zsyzgu#', 13],['_confused', 18],['mh4746', 58],['Chy_Shahrear', 38],['mohit', 8],['BAJUKA', 11],['alex_x', 11],['ayann', 18],['nayimsust', 5],['Maram_Mohammad', 9],['BlackBerry', 4],['Praveen230102', 15],['sj2506', 7],['maone', 6],['IndrojitMondal', 6],['WangTianYi', 10],['vcfl', 4],['Qulinxao', 5],['RDR', 4],['LongCtrl', 7],['TUITUF_Bahrom', 28],['Vinod_Shunmugavel', 3],['Eilen', 7],['Rabahjamal', 50],['Khela_Pari_Nah', 50],['Anton_', 5],['robb_billy', 4],['anjali121', 14],['sign_in158', 6],['Kenan', 6],['ragesh91', 8],['cigarcial', 6],['ACfighter', 2],['mahmud1002', 18],['mohamed_ramadan621', 18],['lucifer_b', 24],['NYN31', 39],['undefined_thimpu', 14],['ConLonCon', 5],['C.O.W.', 18],['robert_nabil20022002', 42],['Darko', 16],['Sulta', 7],['IbraheemJanajreh', 109],['Snipx', 25],['free0u', 9],['ashkan__', 13],['Iman', 11],['Farzad', 10],['PavelChadnov', 54],['aqua4', 19],['mibrahim070', 10],['Ka8eeM', 30],['souravvv', 39],['Baskape', 6],['hyoussef', 68],['ahmed.farag1111', 13],['Dark_Rider_0.0', 13],['zyx3d', 6],['dimiter', 20],['urutom', 9],['SvetlanaMuha2005', 30],['Tom66', 10],['Mahmouddd', 21],['yarrr', 55],['YouSube', 29],['Hussien_Ibrahiem', 59],['innocent_coder', 25],['ash_pikachu', 23],['Denor', 21],['king_programing', 11],['gx_wind', 7],['Sisyy', 110],['dima11221122', 29],['Black', 50],['quest_2', 8],['Zhas', 5],['amribrahim333', 13],['Mohammed_Abdallah', 43],['roa.a-r', 32],['tohuuquan', 13],['akshayk0406', 9],['Coder_Guy', 26],['sana.b', 3],['jiten_321', 50],['Badrangiikh', 40],['sabry_ragab', 24],['golyj_na_stole', 8],['AFiFY', 55],['xfce8888', 50],['ntlarry', 4],['Mockingjay', 38],['Permanent', 38],['mob_lived', 8],['sbcd90', 5],['kirakira', 47],['drake14', 34],['thedreamereng', 19],['lasten', 64],['mostafa_thabet', 30],['syed_jafrul_husen', 35],['anshu-gupta', 38],['GarimaAgrawal', 38],['aymanmostafa', 24],['calculus.saransh', 7],['kemo-fci', 18],['okasha', 36],['umad', 49],['marwankhaled', 25],['HazemElseify', 25],['khaled_khattab', 26],['Mehran-r', 6],['ChaosMaster', 8],['giba', 9],['xeronix', 8],['Geralt', 8],['NSV', 87],['Rahimmia', 50],['KK_ndv#', 24],['KK_ncv91#', 29]
        ]
    for user in userList:
        make_csv_submissons_url(user[0], 1, user[1])

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
            ['______M______', 53],['Nurs107', 13],['hardikdua', 32],['AMnu', 59],['Moen1578', 51],['071-22041-07-Almaz', 16],['Siyuan', 33],['domferrel', 2],['bakliwalaarchit', 7],['Naim_Hasan', 64],['Petar', 11],['kasrafouladi', 36],['N1amr', 36],['Arrias', 134],['tangyiqwan', 17],['jedikni', 29],['nikalosaberidze', 85],['MGS763', 18],['nomiku99', 76],['BATM4N', 29],['lehar', 8],['zwgtxdy', 11],['bm_anas', 11],['zjsxzy', 11],['scott_wu', 67],['percyjackson', 7],['owenomar', 20],['kaiboy', 88],['wobwab007', 23],['heartsinatlantis', 13],['maratonando', 269],['ITDOI', 102],['MohamedMagdy', 62],['supachai_pay', 36],['jowher', 9],['aatemplar', 9],['numitus', 31],['Alfeh', 61],['MathCrusader', 25],['kajol_cse', 33],['pmad1234', 21],['A7med_mo3awad', 13],['dpw4112001', 13],['fuwutu', 7],['nikits', 15],['ar_mbstu2014', 13],['gaporf', 90],['cmashinho', 30],['bergus', 38],['anhaabc', 33],['introibo', 24],['JohnKEA', 12],['yashar_sb_sb', 70],['ahmed_ali199', 6],['Jayzhang', 28],['kopok2', 30],['Ignite_X', 22],['vivek_patel', 4],['Kimia.H', 32],['SamiulSourav', 51],['joylintp', 52],['maxim_polt', 3],['rezaulhsagar', 44],['jackowitzd2', 14],['lodar', 21],['tanzaku', 51],['MelihOzcan', 11],['CodeTamer.', 15],['fsshakkhor', 133],['phamloc', 11],['Angeldar', 7],['Remstam', 8],['Aleksey', 16],['Y-MP', 8],['_Vadim_', 39],['weixian', 9],['neharao9', 7],['pankajb23', 26],['darkknight10', 34],['kalpjain', 34],['Photon_', 89],['Alisafe', 38],['hs484', 38],['ChiMiu', 5],['Artemis.Fowl', 25],['maratonando2', 265],['vici', 25],['zczfight', 26],['tazim5032', 26],['CtrlAlt', 76],['AND1989', 25],['b2lawa', 18],['FatSheep', 15],['_Lumos', 116],['ankeet', 97],['NourElRashidy', 91],['chenpengyu', 9],['Lazzaro', 31],['desperado123', 32],['Svyat', 97],['Korvin79', 11],['New_AgeII', 28],['elrodeo', 7],['myservis2010', 6],['_Evoiz_', 72],['Romeo.', 8],['Heshamovic', 116],['MiHon', 22],['OutSide', 34],['ir5', 14],['michael_tan', 5],['Andark', 7],['Fcdkbear', 87],['wrinx', 186],['naaaag', 5],['OmaaarZ', 33],['techaddict', 37],['Irmuun.Ch', 38],['keep.deep', 17],['MercSint', 11],['vasu_didi', 18],['Scipt', 12],['alexey.enkov', 28],['Phoenix', 40],['C137', 118],['compiler_101', 150],['not', 10],['Andrew_Emad', 38],['abdouforever', 11],['mekagem', 12],['Artishok', 14],['abdelrahman____tarek', 69],['ssohn', 19],['rahulveeran5', 19],['rdivyanshu', 13],['Shavkat_Aminov', 191],['__STR', 42],['yajun#', 19],['Ibrohim_Salohitdinov', 76],['Abu-Gasem1', 26],['cavalier', 10],['shyamvinay', 19],['niyaznigmatul', 64],['Timur_Sitdikov#', 62],['fujiyama', 15],['Diabolic', 19],['enesoncu', 43],['MR_Freeman', 63],['sazol.ss1998', 37],['uwi', 171],['RoyalCoderPRO', 171],['AhmedSamir.1907', 46],['McLaren', 13],['Dr.Gogback', 25],['tridorje', 49],['UoA_ZQC', 79],['totallynotan', 14],['I_love_Hoang_Yen', 149],['Balajiganapathi', 41],['Only_love97', 53],['georgen6', 3],['tryagainlater', 5],['Turysbek', 81],['E.Rokyan', 4],['zafar_sust_bd', 8],['haizhe', 18],['haas', 43],['Islam.Abdo', 56],['2O16', 30],['mcsharma1990', 16],['boomstick', 3],['Mohammad_Kartoumeh', 164],['g_todadze2', 7],['Alkochza', 10],['deadRabbit#', 15],['hydrastuff', 56],['farhad519', 54],['k-mats', 10],['ASAP_Mike', 10],['Temirulan#', 146],['Anonymous', 48],['Mostafa.Ali', 19],['Seif', 84],['joseph_sobhy', 30],['AshVinn', 25],['T0RRES', 104],['OmaeWaMouShenDeiru', 55],['imazato', 10],['HannaYz', 57],['Double_O', 54],['heba_gamal', 32],['theWall', 22],['AhmedHamed', 74],['arbitrary_A', 86],['HAEtaRhoEta', 86],['Antony_w', 6],['FourFourTwo', 54],['cheez', 26],['fabiankasUN', 19],['ABIR', 27],['T-D-K', 32],['Abanob_Emad66', 40],['anchik12345', 29],['Barricadenick', 33],['MohabOsamah', 21],['farukkastamonuda', 98],['shindo', 14],['.jeffrey', 8],['kenthang', 5],['OnceMoreTime', 30],['MuhammedMokbelQ_Q', 36],['MohamadAdel', 59],['jayanto', 44],['santjuan', 35],['msagimbekov', 40],['Alhelal_TWO', 40],['S010M', 38],['nab', 15],['jayesh02', 7],['ant.ermilov', 35],['BII', 12],['shoumo', 17],['nnhamane', 19],['jubairahmed', 26],['satvik007', 20],['ananyagarg.mec18', 20],['Sangha74', 20],['Willionaire', 16],['Sugardorj#', 89],['jlepack', 5],['TarifEzaz', 21],['splinterC3LL', 22],['MQstafa', 23],['kabir.sohel', 14],['hakeem', 44],['philologist', 74],['HellKitsune#', 80],['Alethor', 10],['ltaha', 39],['milkyklim', 5],['hjr265', 8],['pasin30055', 9],['Faster', 52],['dragonfire', 5],['mirdamad', 3],['noob_programmer', 11],['grizz', 5],['Buu-Zaid', 33],['mai_ahmed', 24],['Tutul_dhar', 44],['mokid_hobby_IU', 31],['chizon', 5],['daftcoder', 15],['vincentsthe', 4],['travellerX', 57],['lordn3mrod', 4],['NGiUp', 8],['shtori', 31],['zglicz', 22],['jariasf', 18],['mihaildemidoff', 6],['Moustafa_Abbas', 21],['propashii', 46],['Shafaet', 31],['jaaguptamme', 73],['OlaAdel', 39],['bookofsky', 15],['rushKA', 14],['AlphaNumero', 20],['adityarajiv', 59],['roni_cse', 2],['helderdias', 15],['delta', 30],['ostroumov', 20],['mehrab.sa', 27],['ugly.frog2805', 13],['Nahla95', 16],['Abdallah', 19],['Dr.McKay', 6],['Tanin', 7]
        ]

    for user in userList:
        make_csv_user_submissions(user[0], 1, int(user[1]))

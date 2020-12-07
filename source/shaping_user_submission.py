# ユーザデータを成型する
# ユーザのsubmissionを問題番号とタイトルに直す
# 
# 入力
# 100244194,Dec/03/2020 09:49,_ShadowSong,C - Two Brackets,GNU C++11,Accepted,31 ms,200 KB
# 100235100,Dec/03/2020 06:49,_ShadowSong,B - Toy Blocks,GNU C++11,Accepted,46 ms,400 KB
#
# 出力
# 一つのcsvに集約する
# ユーザ名, 時系列順解答問題番号,正答0誤答1のやつ
# 
# チョット作りが雑

import pandas as pd
import csv

def shaping_user_submission(userNameList):

    title = pd.read_csv('problem_title.csv', header=None, encoding="utf-8")

    for user in userNameList[0]:
        baseDir = '_3__submissions/'
        target = baseDir + user + '.csv'
        data = pd.read_csv(target, header=None)


        with open('./shaping_submissions/'+ user +'.csv', 'a', newline='', encoding="utf-8") as f:
            writer = csv.writer(f)
            for i, d in data.iterrows():
                s = d[3].split("-")[1][1:]
                for j, t in title.iterrows():
                    if t[1].startswith(s):
                        writer.writerow([d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7], t[0], s])
                        break

if __name__ == "__main__":
    userNameList=[
        ['sorry_im_smurfing', 20],['Mk_Python_v1', 46],['Anus1373', 50],['watashi', 56],['Unlenin', 44],['trunghieu11', 72],['sqybi', 6],['SteelRaven',44],['yugle7', 97],['okuzn', 115],['cs1g', 38],['epizend', 8],['_ShadowSong', 98],['Vasiliy_48', 38],['haleyk100198', 122],['Chen_ChaoRui', 19],['watchman', 24],['pakh', 12],['GaryWong', 21],['kirimedia', 12],['Shik', 95],['dima_gozha', 64],['tmt514', 77],['wdydyb', 13],['Duxar', 45],['Saken', 58],['aias', 32],['alex20030190', 118],['Archon.JK', 67],['marat.snowbear', 102],['ivan.v.gerasimov', 49],['y_shindoh', 57],['bjgo', 8],['Tsumiman', 16],['Soulflayer', 13],['vilcheuski', 159],['Electronick', 61],['o948', 29],['guille', 160],['metalopocalipsis', 39],['lee-jinhen', 62],['biltharesatyendra', 129],['Moor', 24],['cesar625', 36],['HamedWBN1', 51],['TheMaverick', 67],['ebd', 15],['mystery_boy', 33],['wubbalubbabugbug', 59],['aminabedi', 22],['Furko', 126],['Nik_Storm_2010', 62],['dionysios', 88],['sg94', 12],['pablo.aguilar', 9],['freebsdx', 57],['Dunaril', 19],['rankalee', 82],['DimsFromDergachy', 18],['artur.socha', 59],['Catherine6', 3],['sarasouju', 11],['dkjsfkhg', 63],['graceoflives', 51],['Doxe', 61],['vlfom', 64],['NVAL', 156],['DDDDDDDDDDDDDDDDDDDDDDDD', 34],['goodhope', 71],['sugar', 31],['MSPA', 32],['Misha100896', 108],['davidepallotti', 11],['classius', 18],['A_Le_K', 68],['a1s3a', 63],['Sammarize', 23],['sdryapko', 43],['jiangzhijie', 44],['NuM', 97],['ReaLNero1', 107],['DoublePointer', 40],['fafafft', 9],['Quinas', 94],['shurick', 6],['ishikado', 62],['YakovPolykovsky', 69],['Henko', 24],['xiaoshua', 28],['kawatea', 58],['abdukodir', 32],['sggutier', 79],['ArmanK', 27],['affix', 14],['vlad107', 99],['UESTC_Defense', 29],['mayakin', 175],['EarlOfDitches', 114],['Deamon', 62],['Likogra', 21],['Heart_Blue', 139],['nongi', 104],['Qoovy', 49],['Azat_Yusupov#', 144],['bidzilya', 81],['shinian', 20],['Vadim2', 82],['Eeyore', 50],['coral_peng', 15],['alexander-nsk94', 34],['ZiyaoWei', 10],['ffx', 23],['gensim', 14],['wjli', 121],['madxmad', 40],['Ahmad_Elsagheer', 97],['firstbegin', 8],['Taras89', 12],['CurbStomp', 35],['fastholf', 20],['JohStraat', 74],['Proscriptus', 20],['Tariqul', 82],['c.utkarsh777', 13],['yongwhan', 111],['lnwvr', 16],['Moemen95', 55],['KFile', 11],['doptster', 28],['NoSoul', 63],['resendiz', 44],['tnakao', 61],['BIT', 19],['Ali.Pi', 78],['gskhirtladze', 144],['vagnard', 61],['Ufowoqqqo', 62],['ANWAR_HOSSAIN', 34],['og.kostya', 114],['CleRIC', 75],['Ramp', 58],['sping128', 91],['xwchen', 48],['alculquicondor', 36],['evima', 58],['prpr', 20],['ilyakryukov', 10],['afMartinez', 6],['SPAND', 25],['clown-fish_Benben', 6],['130705009', 61],['tomash_em', 34],['Orfest', 41],['smiley007', 23],['DimaPhil', 39],['kiko91_7', 11],['wisterik', 22],['Izot_NNSTU', 28],['theSiddhantSharma', 78],['poikniok', 138],['Hachiikung', 107],['dreamoon_love_AA', 198],['simrandokania', 24],['Savaw', 81],['islam-al-aarag', 42],['rng_58', 40],['Mark_tven', 35],['miramar', 80],['newheathen', 34],['atnurgaliev', 20],['AndreySiunov', 35],['VAVAvile', 64],['sweiss', 48],['MaryamG', 45],['prana', 35],['tehqin', 28],['rasmus', 61],['stolis', 41],['Badalyan_Shavarsh', 62],['mkirsche', 123],['aka.Sohieb', 124],['htzfun', 34],['legend_ni', 6],['nickbuelich', 54],['ladan', 49],['killerdjo', 19],['nealzane', 95],['Igor_2017', 120],['the_art_of_war', 129],['ilovepink', 22],['Padme', 17],['trungvthe130284', 98],['yEmre', 34],['Medium', 18],['hlahuhkln', 16],['Warrior', 15],['random.johnnyh', 49],['Amelius', 36],['Valentin_E', 70],['xiaowuc1', 125],['thienlongtpct', 112],['tomas.svab', 38],['MAK', 17],['coderemite', 37],['s.mahdieh', 39],['liuyubobobo', 40],['ruban', 229],['ce1190222', 9],['Khaled91', 17],['Xerxes', 32],['upsolving', 45],['Tampere#', 38],['flash36', 35],['I_love_Tanya_Romanova', 242],['tux1986', 24],['Nox', 18],['Carl___P', 8],['shaon_sust', 21],['.tx', 113],['caustique', 73],['sicon54', 94],['m_p', 16],['Dmohan', 14],['practice_hard', 52],['alibaba', 195],['kewl', 16],['Akikaze', 153],['unit7', 38]
    ]
    shaping_user_submission(userNameList)
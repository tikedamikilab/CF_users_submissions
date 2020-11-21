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
            print('catch KeyError:', e)
            data = pd.read_html(URL, header = 0)
            data[5].to_csv('./users_submissions/'+ userName +'.csv', header=False, index=False, mode='a')

if __name__ == "__main__":
    userList = [
        ['SerVasilich', 29]
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
# ['LHiC', 51], ['whzzt', 30], ['FizzyDavid', 64], ['zeronumber', 3], ['kczno1', 15],
# ['kczno1', 15], ['-XraY-', 66], ['nick452', 3], ['Dmitriy.Belichenko', 53],['kefaa2', 148], ['zx2003', 37], ['duality', 28], ['PavelKunyavskiy', 39], ['gtrhetr', 17], ['vepifanov', 95], ['E869120', 41], ['tmwilliamlin168', 66], ['Errichto', 61], ['snuke', 32], ['aid', 58], ['fivedemands', 5], ['Swistakk', 70], ['Batrr', 65], ['sevenkplus', 37], ['supy', 7], ['LayCurse', 46], ['SpyCheese', 15], ['yhx-12243', 21], ['natsugiri', 83], ['cookiedoth', 43], ['qwerty787788', 60], ['receed', 30], ['amethyst0', 38], ['izban', 84], ['yasugongshang', 51], ['djq_cpp', 32], ['mmaxio', 71], ['I_love_chickpea', 95], ['dreamoon_love_AA', 193], ['majk', 59], ['hank55663', 162], ['Golovanov399', 72], 
# ['zeliboba', 37], ['krijgertje', 122], ['Hazyknight', 54], ['pashka', 17], ['RomaWhite', 41], ['vintage_Vlad_Makeev', 97], ['faebdc', 12], ['step_by_step', 76], ['yokozuna57', 25], ['Nebuchadnezzar', 88], ['xymtxdy', 47], ['panole', 10], ['Chelly', 5], ['eatmore', 18], ['scanhex', 26], ['wzp666', 6], ['Maksim1744', 42], ['Kamfucius', 27], ['ltst', 2], ['QAQAutoMaton', 23], ['Elegia', 38], ['stal_xy23z7b8', 12], ['jijiang', 7], ['kort0n', 45], ['It5t', 2], ['gs12117', 23], ['AndreySergunin', 55], ['xyz111', 32], ['conflict', 21], ['Geothermal', 45], ['ugly2333', 33], ['RNS_CUS', 120], ['PinkRabbit', 45], ['gamegame', 38], ['blackbori', 16], ['Cyanic', 30], ['cdkrot', 40], ['EricHuang2003', 5], 
# ['_h_', 26], ['uwi', 165], ['VArtem', 24], ['tatyam', 13], ['lqs2015', 69], ['SirShokoladina', 38], ['heno239', 62], ['saba2000', 62], ['ilnil', 10], ['stevenkplus', 71], ['ohweonfire', 51], ['sigma425', 39], ['Subconscious', 26], ['chenjb', 30], ['mayaohua2003', 27], ['I_love_Tanya_Romanova', 240], ['dlalswp25', 24], ['zscoder', 65], ['kdh9949', 18], ['tfg', 161], ['kraborak', 27], ['yashChandnani', 63], ['Arterm', 49], ['Alex_2oo8', 41], ['user202729_', 41], ['atomicenergy', 13], ['Shayan', 128], ['Timur_Sitdikov', 60], ['riadwaw', 58], ['WA_TLE', 10], ['mango_lassi', 46], ['xtqqwq', 4], ['DmitryGrigorev', 87], ['cold_chair', 13], ['inaFSTream', 4], ['SSRS_', 30], ['ATS', 22], ['Isonan', 38], 
# ['risujiroh', 68], ['Amoo_Safar', 43], ['wiwitrifai', 76], ['ashmelev', 41], ['ikatanic', 43], ['Fulisike', 46], ['lzr_010506', 33], ['icecuber', 52], ['Tlatoani', 26], ['Eccentricity', 2], ['dorijanlendvaj', 64], ['ffao', 36], ['Eliden', 15], ['Anadi', 91], ['PinkieRabbit', 4], ['zemen', 40], ['Temotoloraia', 39], ['Retro3014', 16], ['Coder', 18], ['nickIuo', 10], ['Itst', 39], ['al13n', 43], ['KMAASZRAA', 46], ['A_Fan_of_the_AK_King--lk', 8], ['imeimi', 18], ['zeus_orz', 34], ['Roundgod', 88], ['DCXDCX', 3], ['sd0061', 84], ['mtsd', 38], ['Zhukov_Dmitry', 24], ['MofK', 43], ['conqueror_of_tourist', 16], ['djq_fpc', 7], ['orz', 17], ['ccf_n0i', 2], ['lumibons', 28], ['KrK', 166], ['Reyna', 98], 
# ['Motarack', 78], ['orbitingflea', 37], ['alex9801', 26], ['tabasz', 43], ['Maripium', 33], ['Noam527', 46], ['Jayce132', 19], ['Jacob', 8], ['CodePlatina', 17],

# ['Martin53', 31], ['Jatana', 74], ['Atreus', 82], ['zjczzzjczjczzzjc', 21], ['kmjp', 201], ['142857', 5], ['frodakcin', 38], ['CN_zwang2002', 35], ['hitonanode', 33], ['Shef', 22], ['Lily', 21], ['Nazrin', 5], ['aropan', 34], ['teapotd', 47], ['Localization', 4], ['nuip', 78], ['Polygon-yg', 10], ['kostka', 63], ['NephrenRuqInsania', 9], ['hugopm', 34], ['nealchen', 12], ['MicGor', 89], ['Tiramister', 39], ['ztc.', 11], ['mrscherry', 3], ['JOHNKRAM', 14], ['Skywynne', 15], ['kobae964', 46], ['turmax', 41], ['Kostroma', 68], ['retrograd', 52], ['nikolapesic2802', 84], ['Akulyat', 93], ['chokudai', 10], ['kotamanegi', 75], ['A.K.E.E.', 25], ['Will_Dearborn', 6], ['Deemo',
# 140], ['amnesiac_dusk', 81], ['CMXRYNP', 19], ['BigBag', 127], ['skip2004', 18], ['ynsm', 9], ['.I.', 163], ['Heltion', 44], ['gepardo', 70], ['Sooke', 29], ['Shik', 95], ['RNS_KSB', 45], ['hehezhou', 8], ['antontrygubO_o', 45], ['orzdjq', 5], ['rqi', 15], ['Nezzar', 75], ['xiaowuc1', 120], ['ZZZZZZZZZZZZZZZZZZ', 4], ['poisonous', 5], ['nikgaevoy', 17], ['sqrtdecompton', 38], ['Vergara', 22], ['khsoo01',
# 13], ['emma', 142], ['balbit', 27], ['Ilya_MSU', 49], ['Pigbrain', 41], ['ilyakor', 28], ['ACCE12138', 3], ['kriii', 28], ['pikmike', 154], ['nonamefour0210', 24], ['NotaMotuaQAQ', 2], ['Yongaron', 15], ['xpptsdy', 6], ['egor_bb', 30], ['Volkov_Ivan', 31], ['79brue', 14], ['littlelittlehorse', 14], ['olphe', 58], ['neko_nyaaaaaaaaaaaaaaaaa', 54], ['Rubikun', 53], ['Xellos', 95], ['kal013', 33], ['wrong',
# 20], ['Lagoon_', 17], ['Kaban-5', 72], ['8-_-8', 73], ['SoMuchDrama', 43], ['emthrm', 39], ['Toxel', 81], ['dario2994', 29], ['RNS_MHB', 91], ['tender_green', 23], ['SendThemToHell', 48], ['pwypeanut', 15], ['cjy2003', 16], ['lezdzh', 9], ['kotatsugame', 20], ['spacevortex', 11], ['jdurie', 63], ['shb123', 16], ['aurora2001', 2], ['Nikitosh', 44], ['osmanorhan', 60], ['luhong', 19], ['GoGooLi', 7], ['cwise', 26], ['znirzej', 37], ['wucstdio', 33], ['tonyjjw', 22], ['Ali.Kh', 118], ['peti1234', 42], ['Morokei', 19], ['Farhod_Farmon', 182], ['.__.', 80], ['ezLadder', 5], ['wifiiii', 41], ['Sert', 119], ['Zayin', 34], ['jo_ulej', 41], ['xyz100', 3], ['sugarrr', 20], ['TadijaSebez', 110], ['liji', 10], ['shenxy13', 9], ['pwild', 35], ['maximumSHOT', 148], ['sumitacchan', 9], ['nhho', 129], ['tempura0224', 36], ['gs18115', 20], ['9baka_Cirno', 10], ['NoLongerRed', 15], ['fuppy', 22], ['jerome_wei', 9], ['hloya_ygrt', 85], ['smiken', 70], ['Gom', 9], ['jklepec', 35], ['isaf27', 39], ['yuma_', 63], ['cescmentation_folch', 78], ['waynetuinfor', 164], ['MAOoo', 31], ['leaf1415', 57], ['HeHere', 16], ['zylber', 11], ['chenkuowen', 10], ['sminem', 3], ['Rafbill', 58], ['Torta', 15], ['MrDindows', 145], ['dimas.kovas', 40], ['falanga', 32], ['-is-this-fft-', 44], ['cerberus97', 87],
# ['rapca', 26], ['Lewin', 70], ['Semenar', 9], ['sava-cska', 23], ['Mustang98', 50], ['Gassa', 63], ['KADR', 61], ['sjcakioi', 8], ['Pyqe', 55], ['TeaPot', 21], ['rstoick', 4], ['penguin1017', 21], ['ppavic', 38], ['MesyuraTheOldDumbGoblin', 2], ['soros666', 13], ['I_love_tigersugar', 74], ['voidmax', 47], ['yp155136', 71], ['skylinebaby', 42], ['DBradac', 41], ['Enchom', 36], ['caoyue', 12], ['I_love_Nikaidou_Shinku', 2], ['jonathanirvings', 33], ['ismagilov.code', 24], ['AlesyaIvanova', 24], ['beginend', 29], ['andrew.volchek', 70], ['DPR-pavlin', 23], ['summitwei', 30], ['LJC00118', 34], ['geniosity', 2], ['marX', 87], ['peltorator', 35], ['satashun', 39], ['JeBeK', 33], ['ToTLeS', 81], ['buko', 33], ['goie', 2], ['notmyalt', 4], ['Sonechko', 95], ['Prabowo', 34]

# ['pokeball', 6], ['Nachia', 8], ['AloneKnight', 8], ['Nyaan', 12],
# ['icfan', 4], ['skxqks', 22], ['nigus', 40], ['Ari', 63], ['.erfanesm.', 5], ['SecondThread', 74], ['qazswedx2', 13], ['saketh', 122], ['primenumber', 9], ['interestingLSY', 55], ['square1001', 25], ['how_to_become_purple', 83], ['Juzek', 15], ['Lebossle', 9], ['Alpha_Q', 45], ['nvmdava', 47], ['jschneider2013', 10], ['arthur.nascimento', 58], ['xuanquang1999', 73], ['Expectation', 3], ['superguymj', 11], ['jakedavis', 24], ['Pajaraja', 17], ['Binary_Search_Tree', 14], ['errorgorn', 30], ['hld67890', 24], ['Legilimens2020', 2], ['wangziji', 19], ['oleh1421', 55], ['ztc_dot', 2], ['Aleks5d', 81], ['ReD_AwHiLe', 27], ['staniewzki', 18], ['mariand', 25], ['Potassium', 38], ['dyxg', 13], ['Shayan.P', 99], ['zbww', 23], ['JeffreyLC', 25], ['McDonald', 13], ['LMOliver', 8], ['Muffinhead', 2], ['tute7627', 44],
# ['SmileyCraft', 10], ['RAVEman', 47], ['malfple', 22], ['dragoon', 24], ['noimi', 76], ['Danylo99', 90], ['alexandra_udristoiu', 19], ['galen_colin', 44], ['darnley', 21], ['zhouzhendong', 29], ['SunshinePie', 2], ['monsoon', 14], ['yao11617', 19], ['memset0c', 18], ['_twilight', 18], ['nehnait', 4], ['catupper', 31], ['.tx', 113], ['beet', 29], ['Jeel_Vaishnav', 47], ['Mojumbo', 25], ['K_T_O', 6], ['VadymKa', 23], ['PoDuReM', 29], ['rama_pang', 45], ['tamionv', 27], ['emoairx', 35], ['xyz32768', 2], ['Alex_Sophie', 2], ['Goorkiewicz', 41], ['Shibuyap', 14], ['Jakube', 59], ['realDonaldTrunp', 4], ['tnowak', 21], ['SPatrik', 40], ['msuwakow', 19], ['Apsara', 12], ['Tweetexas', 14], ['Miffoury', 2], ['MrDecomposition', 49], ['Ra16bit', 58], ['Anachor', 93], ['jxdxhy', 8], ['KayacanV', 22], ['ddytxdy', 26], ['Meeena', 3], ['Barichek', 112], ['xuanyi', 7], ['aarr', 46], ['01191020csl', 5], ['Holidin', 43], ['KevinWan', 52], ['Kuroni9623_orz', 6], ['bayweiheng', 10], ['mateusz', 43], ['Petro1488', 52], ['m_99', 13], ['KingPonyHead', 4], ['ix35', 10], ['rapel', 59], ['cxaphoenix', 55], ['Tommyr7', 30], ['takumi152', 9], ['QCFium', 3], ['sokokaleb', 42], ['almogwald', 13], ['OYJason', 8], ['onjo', 24], ['lmtdora2004', 5], ['cjtoribio', 107], ['pajenegod', 99], ['betrue12', 63], ['asdfghjk', 11], ['milisav', 32], ['posij118', 14], ['antony191',
# 18], ['andrew', 128], ['Samsara_soul', 3], ['poopi', 39], ['sunsiyu', 7], ['VLamarca', 65], ['Celesta', 20], ['TiwAirOAO', 15], ['OrzLiM_817', 2], ['5times187', 2], ['gyz_gyz', 60], ['MaximOboznyi', 36],
# ['fedoseev.timofey', 56], ['Kongweijia', 3], ['rushcheyo', 12], ['timf1089', 49], ['math957963', 21], ['The.Last.Wizard', 99], ['aa2985759', 36], ['Delfad0r', 24], ['Suika_predator', 23], ['UnstoppableChillMachine', 93], ['TearinFree', 17], ['knightL', 57], ['jumpmelon',
# 6], ['ichyo', 22], ['taeyeon_ss', 2], ['KimGongju', 14], ['dvdg6566', 31], ['DeadPillow', 296], ['fastfurioustransform', 3], ['boook', 107], ['KostasKostil', 23], ['Aidos', 146], ['i_am_noob', 22], ['Wild_Hamster', 96], ['ludo', 20], ['wrinx', 149], ['hitman623', 129], ['Medeowex', 132], ['Egor.Lifar', 183], ['enjapma', 18], ['L0TUS', 21], ['prick', 2], ['300iqWontWinIOI2020', 2], ['Sealionheart', 63], ['the_art_of_war', 128], ['Felerius', 41], ['aytel', 42], ['zhangguangxuan99', 26], ['StanislavDon', 20], ['LittleBeetle', 29], ['gina0605', 8], ['Antoine', 74], ['Iscream2001', 3], ['jjaworska', 8], ['adamant', 81], ['forestryks', 17], ['NoCodeNoLife', 30], ['CrescentRose', 5], ['RandomID7896', 6], ['aaaaajack', 51], ['nong', 35], ['vipjml', 13], ['tran0826_1', 35], ['shion_', 13], ['Arthur', 64], ['xlk',
# 39], ['-Wave-', 27], ['Oopsimbad', 31], ['disangan233', 17], ['chenyanbo', 23], ['romanasa', 40], ['RobeZH', 84], ['f.bialas', 13]
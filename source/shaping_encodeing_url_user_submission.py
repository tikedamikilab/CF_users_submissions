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
    baseDir = '_6_8_submissionURL/'
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
                output.append(contestID + encoding_abcdef(contestABCDEF) + encodeing_result(result))
        output.reverse()

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
        ['ArtemParkhomets', 70],['lovefly1983', 23],['ROUNIA78', 17],['adi.badayalya', 22],['jannatmawa58', 4],['STommydx', 83],['hariprasath', 28],['pnm1384', 24],['Shinbai', 83],['Salat', 7],['umarsultan', 34],['ving.xia', 40],['vkuzkokov', 4],['YaNurs', 16],['Bob2006', 57],['Fduxwlqd', 4],['Angry_Nigger', 63],['laoliumang', 31],['surendrasingh9426', 17],['HaiDuong', 22],['2018030401051', 16],['NurlanTolegenov', 38],['grindthecode', 29],['Quby', 9],['triple_e', 26],['AKruglyak', 7],['2016', 31],['elistark', 33],['Skybytskyi.Nikita', 58],['Amr-Alaa', 37],['jackreturn0', 27],['DeadPillow', 299],['Brave_N', 45],['after', 40],['Toirov_Sadi', 85],['enticing_crusader', 21],['arnoldjulians', 11],['sgaflv', 16],['Alilo-Sy', 17],['kiDbanDeath', 41],['ashes0409', 15],['agul', 48],['reldan', 52],['adibbatous', 7],['Ownography', 52],['omar42', 113],['Dalgerok', 147],['mahaveer1141', 10],['z.farrukh2000', 12],['EKGMA', 77],['shevardnadze', 4],['Mehrdad_ravenS', 45],['Larten', 38],['Gaunt', 32],['aleksandr_severinov', 22],['Vaghar', 8],['Legends_of_superflarrow', 7],['softmob', 106],['ballon', 93],['ibrahimelmasri', 13],['Slevin', 25],['LiuRunkY', 60],['rafeek_nehad', 55],['75number', 22],['gvalentiny', 13],['ajmarin', 7],['hoangle134134134', 22],['OmarAhmed', 70],['PC_DOS', 7],['LoDThe', 70],['XenoAmess', 73],['imhereonlyforcookies', 51],['To_Easy', 4],['Mex-Mans', 100],['legendary', 117],['AntonDubovik', 17],['Don_Vito_Corleone_77', 58],['Belonogov', 93],['hznu1', 68],['Jozik', 7],['thenymphsofdelphi', 68],['riadwaw', 58],['su_58', 30],['AlexandruOlteanu2017', 18],['DeZi', 27],['reiracofage', 37],['ttrkaya', 40],['HASP', 37],['Taras_Shevchuk', 6],['E.Hon', 5],['voxel', 50],['SuperLight', 7],['schovkla', 24],['Spellbound', 12],['Blink', 10],['MrNull', 38],['hsnprsd', 55],['PanZverski', 22],['chanming', 18],['toxzi', 133],['Alimol', 26],['Yo_S_iN', 89],['Fixeg', 7],['cxlove', 63],['blackmailer', 32],['CharlesDai', 31],['noor148', 46],['arjunsanjeev7', 70],['Untitled', 13],['TWO_POINTER', 31],['tzc_wk', 40],['Ilya_MSU', 49],['Sert', 122],['akashm', 13],['fsh317574518', 26],['Chernova_Katya', 11],['YasserZ', 13],['135678942570', 40],['ProGrammar666', 11],['Psilocybe', 35],['Kareem', 51],['hopeAconce', 52],['vlad', 21],['egor4kus', 35],['syt', 12],['Kenny_HORROR', 23],['phoenix71', 69],['KareemWS', 14],['RAVEman', 48],['Mohamed-Khaled', 27],['Chasty', 49],['alisher.turubayev', 37],['aime15', 16],['Vasiltsov', 14],['Deemo', 144],['p.ferrari', 29],['phidang', 37],['witua', 67],['AhmedSoliman', 64],['Shtrix', 31],['mera_sirgiy', 7],['sdya', 57],['saikat98', 15],['Togrul-BSU', 15],['Hadi_Asiaie', 20],['Veldrin', 12],['FabianConP', 23],['halwhite', 5],['ahmed_aly', 23],['Venom', 23],['hznu2', 67],['overrorflow', 23],['Ratuvog', 31],['multisystem', 23],['Ksu_PomorSU', 16],['Yury_Bandarchuk', 99],['qq20091200', 11],['vanogam', 107],['1a1a1a', 30],['carber', 37],['Zeus1997', 14],['TRR', 56],['findeasy', 19],['-Starlight-', 13],['PML', 11],['allocator', 8],['Petruchcho', 61],['M.Alijon', 84],['nehalem', 11],['kostya_by', 50],['cupcup', 9],['magdi', 25],['Bsh_Egyptian', 20],['Zyflair', 21],['Predimonio', 20],['anhhung4u', 40],['Shajib_', 84],['moh.amr', 57],['prateep', 108],['Farhod_Farmon', 186],['sotota', 32],['kocko', 83],['__am', 22],['_lucifer_', 89],['oyy123', 5],['maratmiki', 12],['tis', 5],['dancooper', 32],['Rahin31', 30],['sahil09', 7],['landcold7', 68],['monotonical21', 15],['nzamulov', 50],['soumyajeet', 18],['Omar_Morsi', 147],['Kazim#', 65],['CheatEnabled', 21],['TomBombadil', 23],['Dark_Love', 27],['KingOfWrongAnswer', 108],['9aminul', 21],['QWorks123', 33],['BenderRodriges', 20],['praveenkulkarni', 13],['compales2', 5],['orbit', 12],['abhishen', 52],['Alexander-1709', 12],['Rohinee_Sarvaiya', 10],['Anurag', 15],['acedpedped', 19],['sakenism', 22],['_KameHameha_', 22],['roopenmangat', 27],['Goblin', 13],['Un.CD', 20],['kreep', 16],['_op.z', 53],['Shayan', 128],['ybc_c', 9],['sayani_ghosh', 44],['u1904123', 44],['OmarEl-Mohandes', 23],['53645', 22],['canis_majoris123', 23],['Eugene_nik', 13],['deeptiagg16', 25],['bbugaev', 35],['w00w12l', 11],['urbilya', 7],['strelok1918', 14],['mohamed_salama', 19],['Eternity', 5],['Tahlil', 16],['ashk43712', 24],['darkangel#', 7],['SyFy', 22],['rancho', 15],['xth1', 12],['diogen', 15],['_Mes_Ney_Sua_Dyb_10', 53],['mdahabib', 15],['Abdo_Sameh', 29]
    ]
    for user in userList:
        shaping_url_user_submission(user[0], 'dumyfilename')
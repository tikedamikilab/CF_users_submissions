# scraping_user_submission
# CFからあるユーザのsubmissionsを取得 -> csvへ
# users_submissiomsに格納

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
            print(e)
            data = pd.read_html(URL, header = 0)
            data[5].to_csv('./users_submissions/'+ userName +'.csv', header=False, index=False, mode='a')

if __name__ == "__main__":
    userList = [
        ['kczno1', 15], ['-XraY-', 66], ['nick452', 3], ['Dmitriy.Belichenko', 53],['kefaa2', 148], ['zx2003', 37], ['duality', 28], ['PavelKunyavskiy', 39], ['gtrhetr', 17], ['vepifanov', 95], ['E869120', 41], ['tmwilliamlin168', 66], ['Errichto', 61], ['snuke', 32], ['aid', 58], ['fivedemands', 5], ['Swistakk', 70], ['Batrr', 65], ['sevenkplus', 37], ['supy', 7], ['LayCurse', 46], ['SpyCheese', 15], ['yhx-12243', 21], ['natsugiri', 83], ['cookiedoth', 43], ['qwerty787788', 60], ['receed', 30], ['amethyst0', 38], ['izban', 84], ['yasugongshang', 51], ['djq_cpp', 32], ['mmaxio', 71], ['I_love_chickpea', 95], ['dreamoon_love_AA', 193], ['majk', 59], ['hank55663', 162], ['Golovanov399', 72], 
        ['zeliboba', 37], ['krijgertje', 122], ['Hazyknight', 54], ['pashka', 17], ['RomaWhite', 41], ['vintage_Vlad_Makeev', 97], ['faebdc', 12], ['step_by_step', 76], ['yokozuna57', 25], ['Nebuchadnezzar', 88], ['xymtxdy', 47], ['panole', 10], ['Chelly', 5], ['eatmore', 18], ['scanhex', 26], ['wzp666', 6], ['Maksim1744', 42], ['Kamfucius', 27], ['ltst', 2], ['QAQAutoMaton', 23], ['Elegia', 38], ['stal_xy23z7b8', 12], ['jijiang', 7], ['kort0n', 45], ['It5t', 2], ['gs12117', 23], ['AndreySergunin', 55], ['xyz111', 32], ['conflict', 21], ['Geothermal', 45], ['ugly2333', 33], ['RNS_CUS', 120], ['PinkRabbit', 45], ['gamegame', 38], ['blackbori', 16], ['Cyanic', 30], ['cdkrot', 40], ['EricHuang2003', 5], 
        ['_h_', 26], ['uwi', 165], ['VArtem', 24], ['tatyam', 13], ['lqs2015', 69], ['SirShokoladina', 38], ['heno239', 62], ['saba2000', 62], ['ilnil', 10], ['stevenkplus', 71], ['ohweonfire', 51], ['sigma425', 39], ['Subconscious', 26], ['chenjb', 30], ['mayaohua2003', 27], ['I_love_Tanya_Romanova', 240], ['dlalswp25', 24], ['zscoder', 65], ['kdh9949', 18], ['tfg', 161], ['kraborak', 27], ['yashChandnani', 63], ['Arterm', 49], ['Alex_2oo8', 41], ['user202729_', 41], ['atomicenergy', 13], ['Shayan', 128], ['Timur_Sitdikov', 60], ['riadwaw', 58], ['WA_TLE', 10], ['mango_lassi', 46], ['xtqqwq', 4], ['DmitryGrigorev', 87], ['cold_chair', 13], ['inaFSTream', 4], ['SSRS_', 30], ['ATS', 22], ['Isonan', 38], 
        ['risujiroh', 68], ['Amoo_Safar', 43], ['wiwitrifai', 76], ['ashmelev', 41], ['ikatanic', 43], ['Fulisike', 46], ['lzr_010506', 33], ['icecuber', 52], ['Tlatoani', 26], ['Eccentricity', 2], ['dorijanlendvaj', 64], ['ffao', 36], ['Eliden', 15], ['Anadi', 91], ['PinkieRabbit', 4], ['zemen', 40], ['Temotoloraia', 39], ['Retro3014', 16], ['Coder', 18], ['nickIuo', 10], ['Itst', 39], ['al13n', 43], ['KMAASZRAA', 46], ['A_Fan_of_the_AK_King--lk', 8], ['imeimi', 18], ['zeus_orz', 34], ['Roundgod', 88], ['DCXDCX', 3], ['sd0061', 84], ['mtsd', 38], ['Zhukov_Dmitry', 24], ['MofK', 43], ['conqueror_of_tourist', 16], ['djq_fpc', 7], ['orz', 17], ['ccf_n0i', 2], ['lumibons', 28], ['KrK', 166], ['Reyna', 98], 
        ['Motarack', 78], ['orbitingflea', 37], ['alex9801', 26], ['tabasz', 43], ['Maripium', 33], ['Noam527', 46], ['Jayce132', 19], ['Jacob', 8], ['CodePlatina', 17]
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


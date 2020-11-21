# 実行不能
# 状況不明
# おそらくcsvからcos類似度の結果を取得するはず
# エラー内容 > AttributeError: 'Series' object has no attribute 'flatten'

import pandas as pd
import csv

def sample():
    baseDir = 'users_rate_change/0_cos_check3_0.2.csv'
    data = pd.read_csv(baseDir)
    index = data['problemID'].flatten()
    print(data['cos'][0][1:-1].split(','))

    solvedList = [71, 158, 118, 50, 231, 344, 268, 520, 25, 474, 671, 701, 615, 456, 624, 352, 707, 706, 742, 743, 752, 750, 744, 754, 758, 765, 767, 776, 777, 779, 782, 785, 791, 787, 792, 789, 801, 798, 805, 806,
799, 794, 811, 814, 816, 821, 820, 819, 818, 809, 822, 1, 2, 3, 4, 5, 6, 832, 7, 834, 835, 839, 841, 842, 849, 851, 853, 856, 861, 77, 868, 869, 872, 912, 932]

    # for solved in solvedList:
    #     print(d['cos'][1:-1].split()


if __name__ == "__main__":
    sample()
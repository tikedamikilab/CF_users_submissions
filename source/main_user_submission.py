# main
# 並列実行を行うプログラム
# 実行しているプログラムはProcess内を参照

# 注意 > makeCSVらしい．

# userName = ユーザのID
# start=スクレイピングを始めるページの番号．通常１
# end= スクレイピングの終わりのページ．その人個人のページからMAXのページ番号を取得
# ユーザページ例
# https://codeforces.com/submissions/tourist

from multiprocessing import Process
import scraping_URL_user_submissons_problem
import scraping_user_submission

if __name__ == "__main__":
    # userName = 'Um_nik'
    # start = 1
    # end = 108
    userName = 'BinZhao'
    start = 1
    end = 16
    p1 = Process(target = scraping_URL_user_submissons_problem.makeCSVSubmissonsProblemURL, args=(userName, start, end))
    p2 = Process(target = scraping_user_submission.makeCSVUserSubmissions, args=(userName, start, end))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
# main
# チョットだけ楽にする
from multiprocessing import Process
import scraping_URL_user_submissons_problem
import scraping_user_submission

if __name__ == "__main__":
    # userName = 'Um_nik'
    # start = 1
    # end = 108
    userName = 'tourist'
    start = 1
    end = 48
    p1 = Process(target = scraping_URL_user_submissons_problem.makeCSVSubmissonsProblemURL, args=(userName, start, end))
    p2 = Process(target = scraping_user_submission.makeCSVUserSubmissions, args=(userName, start, end))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
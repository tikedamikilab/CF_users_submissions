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
    Process(
        scraping_URL_user_submissons_problem.makeCSVSubmissonsProblemURL(userName, start, end),
        scraping_user_submission.makeCSVUserSubmissions(userName, start, end)
    )
    
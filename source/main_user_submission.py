# 

import scraping_URL_user_submissons_problem
import scraping_user_submission

if __name__ == "__main__":
    scraping_URL_user_submissons_problem.makeSubmissonsProblemURL('tourist', 1, 48)
    scraping_user_submission.makeUserSubmissionsCsv('tourist', 1, 48)
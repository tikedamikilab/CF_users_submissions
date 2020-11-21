# source\scraping_targetproblem_solvedusers.py
#
# チョット保留

import pandas as pd
import urllib.request, urllib.error

def makeCSVTargetProblemSolvedUsers(problemID, end, problemABCDEF = 'A'):
    baseURL = "https://codeforces.com/problemset/status/"
    targetProblemURL = baseURL + str(problemID) + "/problem/" + problemABCDEF
    print(targetProblemURL)

if __name__ == "__main__":
    makeCSVTargetProblemSolvedUsers(1, 1)

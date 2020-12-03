from source import scraping_target_to_maxsubmission                         

if __name__ == "__main__":
    for i in range(1, 100):
        problemID = i
        BaseURL = "https://codeforces.com/problemset/status/"
        targetURL = BaseURL + str(problemID) + "/problem/" + 'A'
        
        st.printTargetMAXPage(problemID, targetURL)


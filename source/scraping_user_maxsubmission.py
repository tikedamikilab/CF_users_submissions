import scraping_target_to_maxsubmission     
import pandas as pd                    

if __name__ == "__main__":

    baseDir = 'users_analytics/'
    target = baseDir + "_target_userSolvedCount" + '.csv'
    data = pd.read_csv(target)

    # print(data[data['count'] == 11])

    for index, data in data[data['count'] == 10].iterrows():
        user = data['username']
        BaseURL = "https://codeforces.com/submissions/"
        targetURL = BaseURL + str(user)
        scraping_target_to_maxsubmission.print_target_maxpage(user, targetURL)


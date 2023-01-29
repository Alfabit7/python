
def ShowScoreAverage(userNameDict, name):
    averageScoreList = []
    print(userNameDict[name])
    for subject in userNameDict[name].values():
        # print(subject)
        for i in subject:
            averageScoreList.append(i)
    score = round(sum(averageScoreList)/len(averageScoreList), 2)
    return score

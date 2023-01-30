
def ShowScoreAverageUser(userNameDict, name):
    averageScoreList = []
    print()
    print(f'Все оценки ученика {name} {userNameDict[name]}')
    for subject in userNameDict[name].values():
        for i in subject:
            averageScoreList.append(i)
    score = round(sum(averageScoreList)/len(averageScoreList), 2)
    return score


def ShowScoreLesson(userNameDict, lesson):
    scoreLessonList = []
    for name in userNameDict:
        for grade in userNameDict[name][lesson]:
            scoreLessonList.append(grade)
    print()
    print(f'Всего оценок по предмету {lesson}: {len(scoreLessonList)}')
    score = round(sum(scoreLessonList)/len(scoreLessonList))
    return score

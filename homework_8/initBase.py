from random import randint as rn
# Наполняет словарь userNameDict именами учеников и предметами и оценками (инициализация userNameDict )


def loadList(allUser, allLessons):
    userNameDict = {}
    for us in allUser:
        userNameDict[us] = {}
        for lesson in allLessons:
            userNameDict[us][lesson] = []
            for k in range(countGrade):
                userNameDict[us][lesson].append(generateGrade(allUser))
    return userNameDict


#  Функция для генерации оценок
countGrade = 2
gradeLow = 1
gradeHigth = 5


def generateGrade(allUser):
    lenRange = (len(allUser))
    for i in range(lenRange):
        grade = rn(gradeLow, gradeHigth)
    return grade

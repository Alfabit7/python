import view
import importList
import initBase
import scoreAverage
import modExp

userNameDict = {}
allUser = []
allLessons = []
importListUsers = 'namesUsersList.txt'
importListLessons = 'lesson.txt'


def start():
    allUser = importList.createList(importListUsers)
    allLessons = importList.createList(importListLessons)
    userNameDict = initBase.loadList(allUser, allLessons)
    initBase.generateGrade(allUser)
    while True:
        menu = view.ShowMenu()
        if menu == 1:
            name = input('Введите имя ученика: ')
            userNameDict[name] = {}
            allUser.append(name)
            if allLessons:
                for lesson in allLessons:
                    userNameDict[name][lesson] = []

        elif menu == 2:
            lesson = input('Введите название предмета: ')
            for name in allUser:
                userNameDict[name][lesson] = []
            allLessons.append(lesson)

        elif menu == 3:
            if allUser:
                name = input('Введите имя ученика: ')
                if name not in allUser:
                    print()
                    print(
                        f'Ученика с именем {name} в списке нет, сначала добавьте ученика {name} для этого выбереите пункт меню 1 ')
                    continue
            else:
                print()
                print(
                    'Список учеников пуст, сначала добавьте ученика, для этого выберите  пункт меню -1 ')
                start()
            if allLessons:
                lesson = input('Введите название предмета: ')
                if lesson not in allLessons:
                    print()
                    print(
                        f'Предмета с названием {lesson} в списке нет, сначала добавьте предмета {lesson} для этого выберите пункт меню 2 ')
                    continue
                else:
                    grade = view.InputGrade()
                    userNameDict[name][lesson].append(grade)
            else:
                print(
                    'Список предметов пуст сначала добавьте предмет, для этого выберите  пункт меню -2 ')
                start()
        elif menu == 4:
            name = input('Введите имя ученика: ')
            print(userNameDict[name])
        elif menu == 5:
            print(f'Все ученики \n {allUser}')
        elif menu == 6:
            print(f'Все предметы \n {allLessons}')
        elif menu == 7:
            print(userNameDict)
        elif menu == 8:
            name = input('Введите имя ученика: ')
            score = scoreAverage.ShowScoreAverageUser(userNameDict, name)
            print(f'Средний бал ученика {name} = {score}')
        elif menu == 9:
            lesson = input('Введите название предмета: ')
            score = scoreAverage.ShowScoreLesson(userNameDict, lesson)
            print(f'Средний бал по предмету {lesson} = {score}')
        elif menu == 10:
            path = input('Введите название файла: ')
            modExp.SaveBase(userNameDict, path)
        elif menu == '':
            print('exit')
            break

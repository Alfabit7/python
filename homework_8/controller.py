import view
userNameDict = {}
allUser = []
allLessons = []

def start():
    while True:
        menu = view.ShowMenu()
        if menu == 1:
            name = input('Введите имя ученика: ')
            userNameDict[name] = {}
            allUser.append(name)
            if allLessons:
                for lesson in allLessons:
                    userNameDict[name][lesson] = []
            print(userNameDict)

        elif menu == 2:
            lesson = input('Введите название предмета: ')
            for name in allUser:
                userNameDict[name][lesson] = []
            allLessons.append(lesson)
            print(userNameDict)
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
                    print(userNameDict)
            else:
                print(
                    'Список предметов пуст сначала добавьте предмет, для этого выберите  пункт меню -2 ')
                start()
        elif menu == 4:
            name = input('Введите имя ученика: ')
            print(userNameDict[name])
        elif menu == 5:
            print(f'Все ученики {allUser}')
        elif menu == 6:
            print(f'Все предметы {allLessons}')
        elif menu == '':
            print('exit')
            break

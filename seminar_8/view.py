
def ShowMenu():
    print()
    print('Для показа спика учеников нажмите-1, Для показа листа оценок нажмите-2')
    print('Для показа листа оценок нажмите-3,  Для добавления нового ученика нажмите-4, Выход из программы- Enter')
    selectUser = input('Введите номер меню: ')
    return selectUser


def showUser(userList):
    for users in userList:
        for userEl in users:
            for el in userEl.keys():
                if el == 'Имя' or el == 'Фамилия':
                    print(users, end=' ')
                else:
                    continue


def AddUser(userList):
    secondUser = input('Введите фамилию: ')
    nameUser = input('Введите имя: ')
    newDictName = {'Фамилия': secondUser}
    newDictSecondName = {'Имя': nameUser}
    userList.append(newDictName)
    userList.append(newDictSecondName)
    return userList


def ShowGrade(userList):
    a = []
    userGrade = input('введите фамилию ученика: ')
    for users in userList:
        for userEl in users:
            for el in userEl.values():
                if el == userGrade:
                    for grade in users:
                        for findEl in grade.keys():
                            if findEl == 'Оценка':
                                for findGrade in grade.values():
                                    print(
                                        f'Оценка ученика с фамилией {userGrade}: {findGrade}')

                        # print(f'grade{grade}')
                        # # print(f'grade{grade.keys()}')
                        # a.append(grade.keys())

                        # if grade.keys() == "dict_keys(['Название предмета'])":
                        #     print(grade.valuse())

                        # if grade.keys() == 'Оценка':
                        #     print(grade.values(), end=' ')
                        # else:
                        #     print('sdfd')
    # print(a)

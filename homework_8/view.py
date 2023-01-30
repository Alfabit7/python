def ShowMenu():

    while True:
        print()
        print('1 Добавить ученика: ' '\n' '2 Добавить предмет: ' '\n' '3 Добавить оценку ученику: ' '\n' '4 Посмотреть оценки ученика: ' '\n' '5 Посмотреть список учеников: ' '\n' '6 Посмотреть список предметов: ' '\n' '7 Показать все данные: ' '\n' '8 Показать средний бал ученика: ' '\n' '9 Показать средний бал школы по предмету: ' '\n''10 Выход Enter: ')
        menu = input('Выберите пункт меню: ')
        try:
            menu = int(menu)
        except ValueError:
            if menu != '':
                print()
                print('Буквы вводить нельзя!')
            else:
                break
            continue
        if 0 < menu <= 9:
            break
        else:
            print()
            print('Цифры должны быть от 1 до 9')
    return menu


def InputGrade():
    while True:
        grade = input('Введите оценку предмета от 1 до 5: ')
        try:
            grade = int(grade)
        except ValueError:
            print()
            print('Буквы вводить нельзя')
            continue
        if 0 < grade <= 5:
            break
        else:
            print()
            print('Введите цифры от 1 до 5')
    return grade

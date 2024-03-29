def main_menu():
    print('1. Показать справочник контактов (жми 1) ')
    print('2. Поиск (жми 2) ')
    print('3. Импорт базы контактов (жми 3) ')
    print('4. Экспорт базы контактов (жми 4) ')
    print('5. Добавить новый контакт (жми 5)  ')
    print('6. Удалить контакт (жми 6)  ')
    print('7. Для сортировки по Фамилии жми 7')
    print('8. Редактирование контакта (жми 8) ')
    print('9. Для выхода жми Enter \n')
    menu = input('Выберите пункт меню: ')
    return menu


def show_database(list_of_dict):

    for idx, man in enumerate(list_of_dict):
        print(
            f'{(idx+1):4}  Фамилия: {man[0]:18} Имя: {man[1]:10}  Номер: {man[2]:10}\t Комментарий: {man[3]:3}')


def second_menu(text):
    a = input(text)
    return (a)


def inputNumber(text, len_data_base):
    while True:
        value = input(text)
        try:
            value = int(value)
        except ValueError:
            print('Вы ввели некорректное значение, попробуйте еще раз')
            continue
        if 1 < value <= len_data_base:
            break
        else:
            print(f'Значение строки должно быть от 1 до {len_data_base}')
    return value


def add_user():
    F_name = input('Введите имя: ')
    L_name = input('Введите фамилию: ')
    phonenum = input('Введите номер телефона: ')
    coment = input('Введите комментарий: ')
    user_dict = {'Фамилия': F_name, 'Имя': L_name,
                 'Телефон': phonenum, 'Комментарий': coment}
    return user_dict


def show_str(list_of_dict):
    print(f'N  Фамилия:        Имя:        Номер:           Комментарий: ')
    for idx, el in enumerate(list_of_dict):
        man = el
        print(f'{man[0]}      {man[1]}       {man[2]}         {man[3]}')

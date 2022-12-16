# Проверяет, что введено число, а не текст
def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print('Ошибка. Требуется ввод числа')
    return number

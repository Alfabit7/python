# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

firstElement = int(input('введите первый элемент последовательности: '))
step = int(input('введите шаг последовательности: '))
countElement = int(
    input('введите сколько элементов последовательности нужно вывести: '))

# list comprehension
result = [firstElement + (i-1)*step for i in range(1, countElement+1)]
print(result)


# for i in range(1, countElement):
#     result = firstElement + (i-1)*step
#     print(result)

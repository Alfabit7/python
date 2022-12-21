# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
a = 10
arrTuple = set(random.randint(0, 15) for i in range(a))
arrList = list(arrTuple)
print(arrTuple)
result = 0
for i in range(0, len(arrList)):
    if i % 2 != 0:
        result += arrList[i]
print(result)

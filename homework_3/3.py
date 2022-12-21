# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значеним дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from decimal import Decimal
arrList = [1.1, 1.2, 3.1, 5, 10.01]
newList = []

for i in arrList:
    i = Decimal(str(i))
    diff = i-int(i)

    if diff != 0:
        newList.append(diff)
    else:
        continue
print()
print(arrList)
print(
    f'Разница между максимальной и минимальной дробной частью списка arrList:  {max(newList)-min(newList)}')

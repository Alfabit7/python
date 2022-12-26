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


# решение 2
# import random
# leng = int(input('введите размер списка = '))
# my_L = []
# for i in range(leng):
#     my_L.append((float(random.randint(100, 999))/100))
# print(my_L)

# max = 0
# min = 1

# for num in my_L:
#     num = str(num)
#     if "." in num:
#         index_point = num.find('.')
#         N = float(num[index_point:])

#     if N > max:
#         max = N
#     if N < min:
#         min = N


# print(f'Разница между {max} - {min}  = {round(max - min, 2)}')


# решение 3
# import random
# from random import randint
# import os
# os.system('cls')


# s = []
# s1 = []
# for i in range(randint(2, 10)):
#     num = random.uniform(0, 10)
#     s.append(round(num, 2))
#     num1 = s[i] % 1
#     s1.append(round(num1, 2))

# print("Случайно заданный список из вещественных чисел : ")
# print()

# print(s)
# print(s1)
# print()
# res = max(s1) - min(s1)
# print("Разница между максимальным и минимальным значением дробной части : ", res)


# backup
# from decimal import Decimal
# arrList = [1.1, 1.2, 3.1, 5, 10.01]
# newList = []

# for i in arrList:
#     i = Decimal(str(i))
#     diff = i-int(i)

#     if diff != 0:
#         newList.append(diff)
#     else:
#         continue
# print()
# print(arrList)
# print(
#     f'Разница между максимальной и минимальной дробной частью списка arrList:  {max(newList)-min(newList)}')

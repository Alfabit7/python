# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from math import ceil
import random
a = 0
b = 10
y = 8
arrList = [random.randint(a, b) for i in range(y)]
end = len(arrList)-1
result = 0
newList = []

for i in range((end//2)+1):
    result = arrList[i]*arrList[end]
    newList.append(result)
    end -= 1
print(arrList, len(arrList))
print(newList)


# решение 2
# a = []
# len_ls = int(input('Введите длину списка: '))
# for i in range(len_ls):
#     a.append(int(input(f'Введите {i + 1} число: ')))
# print(a)

# newArr = []
# for j in range(int(len_ls / 2)):
#     newArr.append(a[j] * a[-j - 1])
# if len_ls % 2 != 0:
#     newArr.append(a[j + 1]**2)
# print(newArr)


# решение 3

# my_list = [2, 3, 4, 5, 6]
# listNew = []

# for i in range(len(my_list)):
#     listNew.append(my_list[0] * my_list[-1])
#     del my_list[0]
#     del my_list[-1]
#     if len(my_list) == 1:
#         listNew.append(my_list[0] ** 2)
#         del my_list[0]
#     if len(my_list) == 0:
#         break
# print(listNew)

# решение 4
# my_list = [2, 3, 5, 6]
# listNew = []

# for i in range(len(my_list)//2):
#     listNew.append(my_list.pop(0) * my_list.pop(-1))
# if len(my_list) == 1:
#     listNew.append(my_list.pop(0) ** 2)

# print(listNew)


# решение 6
# a = []
# len_ls = int(input('Введите длину списка: '))
# for i in range(len_ls):
#     a.append(int(input(f'Введите {i + 1} число: ')))
# print(a)

# newArr = []
# for j in range(ceil(len_ls / 2)):
#     newArr.append(a[j] * a[-j - 1])

# print(newArr)

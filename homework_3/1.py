# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


import random
len_list = 10
arrTuple = set(random.randint(0, 15) for i in range(len_list))
arrList = list(arrTuple)
print(arrTuple)
result = 0
for i in range(0, len(arrList)):
    if i % 2 != 0:
        result += arrList[i]
print(result)


# решение 2
# import random as rand
# my_list = [23, 45, 73, 1, 4, 3, 9]
# sumEl = 0

# # 1-й вариант

# for item in range(1, len(my_list), 2):
#     sumEl += my_list[item]
# print(sumEl)


# 2-й вариант

# for item in range(len(my_list)):
#     if item % 2 != 0:
#         sumEl += my_list[item]
# print(sumEl)


# решение 3

l = int(input('Введите длину списка: '))
ls = [rand.randint(1, 50) for i in range(l)]
sum = 0
for i in range(1, l, 2):
    sum += ls[i]
print(ls)
print(f'Сумма чисел на нечетных позициях равна: {sum}')


# решение оптимальное
# import random as rand

# l = int(input('Введите длину списка: '))
# ls = [rand.randint(1,50) for i in range(l)]

# new_ls = ls[1:l:2]
# sum_nefw_ls = sum(new_ls)
# print(ls)
# print(new_ls)
# print(f'Сумма чисел на нечетных позициях равна: {sum_nefw_ls }')

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random
# start_range = 0
# end_range = 8
# len_list = 20
# random_list = [random.randint(start_range, end_range) for i in range(len_list)]
# print(f'Случайный список: {random_list} длина списка {len(random_list)}')
# new_list = []
# for el in random_list:
#     if el in new_list:
#         continue
#     else:
#         new_list.append(el)
# print(f'Новый список без дублей {new_list} длина списка {len(new_list)}')


# РЕШЕНИЕ 2 с с помощью множества
start_range = 0
end_range = 8
len_list = 20
random_list = [random.randint(start_range, end_range) for i in range(len_list)]
new_list = set(random_list)
print()
print(f'Случайный список: {random_list} длина списка {len(random_list)}')
print(f'Новый список без дублей {new_list} длина списка {len(new_list)}')

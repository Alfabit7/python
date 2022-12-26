
# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

#     1) с помощью математических формул нахождения корней квадратного уравнения

#     2) с помощью дополнительных библиотек Python

# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.


# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
# number_list = input('Введите числа через пробел ').split()
# max_num = int(number_list[0])
# min_num = int(number_list[0])
# for el in number_list:
#     el = int(el)
#     if max_num < el:
#         max_num = el
#     if min_num > el:
#         min_num = el
# print(number_list)
# print(max_num, min_num)


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# d = b**2 - 4*a*c
# d==0 x = (-1)*b/2*a
#   d>0  x1 = (-b - math.sqrt(D)) / 2 * a
#    d>0      x2 = (-b + math.sqrt(D)) / 2 * a

# третья задача
# number_1 = int(input('Введите первое число: '))
# number_2 = int(input('Введите второе число: '))
# max_num = max(number_1, number_2)
# min_num = min(number_1, number_2)
# for num in range(max_num, number_1*number_2 + 1, max_num):
#     if num % min_num == 0:
#         print(num)
#         break

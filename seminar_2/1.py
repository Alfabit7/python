# 11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#  Пример:
#  - Для N = 5: 1, -3, 9, -27, 81

number = int(input('Input N '))
list = []
for i in range(0, number):
    list.append((-3) ** i)
print(list)

# РЕШЕНИЕ 2
# n = int(input('Введите N '))
# num = 1
# separator = ' '
# result = ''
# for i in range(1, n):
#     num *= -3
#     result = result + str(num) + separator
# print('1 '+result)

# РЕШЕНИЕ 3
# n = int(input('Input N '))
# for i in range(n):
#     print((-3)**(i))

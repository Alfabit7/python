# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

user_number = int(input('введите число: '))
i = 2
while user_number != 1:
    while user_number % i == 0:
        print(i, end=' ')
        user_number /= i
    i += 1

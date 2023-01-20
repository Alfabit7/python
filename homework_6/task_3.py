
# Задача 32:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
num1 = int(input('Введите число num1: '))
num2 = int(input('Введите степень числа num1: '))
result = num1


def myPow(a, b, result):
    if b == 1:
        return result
    return myPow(a, b-1, result*num1)


print(myPow(num1, num2, result))

# Решение циклом
# def myPow(a, b):
#     res = 1
#     while b > 0:
#         res = res*a
#         b -= 1
#     return res
# print(myPow(num1, num2))

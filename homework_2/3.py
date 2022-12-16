# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

userNumber = int(input('Введите число N '))
result = 0
for i in range(1, userNumber+1):
    result += (1+(1/i))**i
print(round(result, 3))

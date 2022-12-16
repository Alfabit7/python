# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0, 56 -> 11
userNumber = float(input('Введите вещественное число '))
print(f'Вы ввели число: {userNumber}')
result = 0
for i in str(userNumber):
    if i != '.':
        result += int(i)
print(f'Сумма чисел {userNumber} равна {result}')

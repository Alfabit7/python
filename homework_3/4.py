# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
userNumber = None
inputFlag = True
while inputFlag:
    try:
        userNumber = int(input('Введите число в десятичной системе: '))
        inputFlag = False
    except ValueError:
        print('Повторите ввод')

number = userNumber
binaryNumber = ""
while number > 0:
    binaryNumber = str(number % 2)+binaryNumber
    number = number//2
print(f'Число {userNumber} в двоичной системе равно: {binaryNumber}')


# решение 2
# x = int(input("Введите любое натуральное число: "))
# n = bin(x)
# print()
# print("Вид введенного числа в двоичной системе счисления :", n)

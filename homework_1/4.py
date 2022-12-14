# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarterNumber = int(input('Введите номер четверти от 1 до 4 включителько '))
while quarterNumber < 1 or quarterNumber > 4:
    print('Повторите ввод')
    quarterNumber = int(
        input('Введите номер четверти от 1 до 4 включителько '))

if quarterNumber == 1:
    print('x > 0 and y > 0')
elif quarterNumber == 2:
    print('x < 0  y > 0')
elif quarterNumber == 3:
    print('x < 0  and y < 0')
elif quarterNumber == 4:
    print('x > 0  y < 0')

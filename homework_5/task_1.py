# 39(1). Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале. Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. В конце вывести игрока, который победил

# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.

# В качестве дополнительного усложнения можно:
#         a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 0 до 28)

#         b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )
#    пока количество конфет больше 28 игрокик продолжают делать ход
import random

# Первым ходит игрок угадвший число num от 0 до 2
namePlayer_1 = 'Игрок №1'
namePlayer_2 = 'Игрок №2'


def randomNumber():
    num = random.randint(0, 2)
    return num


# Кто ходит первым
print(
    f' Первым угадывает число {namePlayer_1}, введите число от 0 до 2: ', end=' ')
num = randomNumber()
guess = int(input())
if num == guess:
    print(f'Ходит первым игрок {namePlayer_1}')

winnerFlag = True
while guess != num:
    if winnerFlag:
        print(f'Угадывает {namePlayer_2},', end=' ')
        num = randomNumber()
        guess = int(input())
        winnerFlag = False
        if guess == num:
            print(f'Ходит первым {namePlayer_2}', end=' ')
            winnerFlag = True

    else:
        print(f'Угадывает  {namePlayer_1}', end=' ')
        num = randomNumber()
        guess = int(input())
        winnerFlag = True
        if guess == num:
            print(f'Ходит первым {namePlayer_1}', end=' ')
            winnerFlag = False
# Кто ходит первым  END

print()
# Функция записывает ход игрока в перменную movePlayer


def StepPlayer():
    movePlayer = int(input())
    while movePlayer < 1 or movePlayer > 28:
        print('Введите число от 1 до 28')
        movePlayer = int(input())
    return movePlayer


candy = 99  # конфеты

while candy > 28:
    if winnerFlag == True:
        print(
            f'{namePlayer_1} возьмите количество конфет от 1 до 28 включительно:', end=' ')
        winnerFlag = False
        movePlayer = StepPlayer()
    else:
        print(
            f'{namePlayer_2} возьмите количество конфет от 1 до 28 включительно:', end=' ')
        winnerFlag = True
        movePlayer = StepPlayer()

    candy -= movePlayer
    print(f'candy = {candy}')
    if candy < 29 and winnerFlag == True:
        print(f'Победил {namePlayer_1} ')
    elif candy < 29 and winnerFlag == False:
        print(f'Победил {namePlayer_2} ')

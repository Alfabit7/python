# 39(2). Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале, игроки ходят поочередно, необходимо вывести карту(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента, каждый из которого обозначает сответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик, и проверку на победу( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)
# создаем игру и окно
import random
fieldGameList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in fieldGameList:
    for j in i:
        print(j, end=' ')
    print()

# Функция проверяет что пользователь ввел число от 1 до 10


def MovePlayer():
    while True:
        value = input(f'Введите число от {numStartRange} до {numEndRange}: ')
        try:
            value = int(value)
        except ValueError:
            print(
                f'Повторите ввод. Нужно ввести число от {numStartRange} до {numEndRange}:')
            continue
        if numStartRange <= value <= numEndRange:
            break
        else:
            print(
                f'Число не входит в диапазон от {numStartRange} до {numEndRange}')
    return value


def randomNumber():
    num = random.randint(0, 2)
    return num


# guessNumber = randomNumber()
guessNumber = 2

print('Жеребьевка. Ходит первым игрок угадавший число')
numStartRange = 1
numEndRange = 2
player_1 = 'Игрок № 1'
player_2 = 'Игрок № 2'
winner = player_1
print(f'Ходит  {winner}')

while True:
    if winner == player_1:
        userInput = MovePlayer()
        if guessNumber == userInput:
            print(f'Первым ходит   {player_1}')
            break

        else:
            winner = player_2
            print(f'Ходит  {winner}')
            userInput = MovePlayer()
    else:
        if guessNumber == userInput:
            print(f'Первым ходит  {player_2}')
            break

        else:
            winner = player_1
            print(f'Ходит  {winner}')

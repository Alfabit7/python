# 39(2). Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале, игроки ходят поочередно, необходимо вывести карту(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента, каждый из которого обозначает сответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка, на которую мы хотим поставить крестик или нолик, и проверку на победу( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)
# создаем игру и окно
import random
fieldGameList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def RenderFieldGame():
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


guessNumber = randomNumber()

print('Жеребьевка. Крестиками ходит первым игрок угадавший число')
numStartRange = 1
numEndRange = 2
player_1 = 'Игрок № 1'
player_2 = 'Игрок № 2'
namePlayer = player_1
print(f'Ходит  {namePlayer}')

# Жеребьевка на первый ход
while True:
    if namePlayer == player_1:
        userInput = MovePlayer()
        if guessNumber == userInput:
            print(f'Первым ходит  {player_1}')
            symbolStep = 'x'
            break

        else:
            namePlayer = player_2
            print(f'Ходит  {namePlayer}')
            userInput = MovePlayer()
    else:
        if guessNumber == userInput:
            print(f'Первым ходит {player_2}')
            symbolStep = 'x'
            break

        else:
            namePlayer = player_1
            print(f'Ходит  {namePlayer}')
# END Жеребьевка на первый ход

numStartRange = 1
numEndRange = 9
RenderFieldGame()
# Функция изменяет клетку на х или о


def ChangeCell(stepChar):

    for el in fieldGameList:
        if stepPlayer in el:
            for i in range(len(el)):
                if el[i] == stepPlayer:
                    el[i] = symbolStep
    return fieldGameList


# Функция проверяет что клетка не занята
checkList = []


def CheckedCell(step):
    if step in checkList:
        print('Это клетка уже занята, введите номер другой свободной клетки')
        return False
    else:
        checkList.append(step)
        return True

# Функция кто победил


def checkedWinner(arr):
    if arr[0][0] == arr[0][1] == arr[0][2] or arr[1][0] == arr[1][1] == arr[1][2] or arr[2][0] == arr[2][1] == arr[2][2] or arr[0][0] == arr[1][0] == arr[2][0] or arr[0][1] == arr[1][1] == arr[2][1] or arr[0][2] == arr[1][2] == arr[2][2] or arr[0][0] == arr[1][1] == arr[2][2] or arr[0][2] == arr[1][1] == arr[2][0]:
        return False
    else:
        return True


maxStep = 9
step = 0
flagWinner = True
while step < maxStep and flagWinner:
    print(f'Ходит игрок {namePlayer}')
    if namePlayer == player_1:
        stepPlayer = MovePlayer()
        a = CheckedCell(stepPlayer)
        while not a:
            stepPlayer = MovePlayer()
            a = CheckedCell(stepPlayer)
        else:
            symbolStep = 'x'
            ChangeCell(symbolStep)
            flagWinner = checkedWinner(fieldGameList)
            if flagWinner == False:
                break
            else:
                namePlayer = player_2
                RenderFieldGame()
    else:

        stepPlayer = MovePlayer()
        a = CheckedCell(stepPlayer)

        while not a:
            stepPlayer = MovePlayer()
            a = CheckedCell(stepPlayer)
        else:
            symbolStep = 'o'
            ChangeCell(symbolStep)
            flagWinner = checkedWinner(fieldGameList)
            if flagWinner == False:
                break
            else:
                namePlayer = player_1
                RenderFieldGame()
    step += 1
print(f'Победил {namePlayer}')

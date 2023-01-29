from random import randrange as rn
# Генератор имен
listUsers = []
importListUsers = 'nameslist.txt'

# Из файла txt читает строки с фио ученика и записывает каждую строку как элемент список
with open(importListUsers, 'r', encoding='UTF-8') as file:
    allFile = file.readlines()
    lenAllFile = len(allFile)
    for user in allFile:
        if len(listUsers) < len(allFile)-1:
            listUsers.append(user[:len(user)-1])
        else:
            listUsers.append(user)
print(listUsers)

#   из готового списка имен добавляет рандомно имена в новый список, длина нового списка задется пользователем
# newList = []
# countUsers = 1000
# for i in range(countUsers):
#     randomNumber = rn(0, len(listUsers), 1)
#     newList.append(f'{listUsers[randomNumber]}{i}')

# print(newList)

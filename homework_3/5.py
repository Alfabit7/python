# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
inputFlag = True
userNumber = None
while inputFlag:
    try:
        userNumber = int(input('Enter number: '))
        inputFlag = False
    except:
        print('replay enter')

i = 0
f1 = 0
f2 = 1
sum = 0
oneList = [f1, f2]
twoList = None
for i in range(userNumber):
    sum = f1+f2
    oneList.append(sum)
    f1 = f2
    f2 = sum
twoList = oneList.copy()
twoList.reverse()

for i in range(len(twoList)):
    if i % 2 == 0:
        twoList[i] = (twoList[i]*-1)
    else:
        twoList[i] = (twoList[i])
twoList.remove(0)

mergList = twoList+oneList
print(mergList)

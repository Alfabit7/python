# Задача 31: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]
myArr = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

num1 = int(input('Введите число нижней границы поиска: '))
num2 = int(input('Введите число верхней границы поиска: '))
result = [i for i in myArr]
arrIndex = []
for idx, val in enumerate(myArr):
    if num1 <= val <= num2:
        arrIndex.append(idx)
print(arrIndex)

# Solution 2
# for i in range(len(myArr)):
#     if num1 <= myArr[i] <= num2:
#         arrIndex.append(i)
#         arrIndex
# print(arrIndex)

# Solution 3
# lst = [indx for indx,val in enumerate(myArr) if num1<=val<=num2]
# print(lst)

# 1)Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.
import random
a = 1
b = 7

array = [random.randint(a, b) for i in range(20)]
print(array)

d = {}
for i in array:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

max = 0
key = 0
for i in range(a, (b+1)):
    if (d[i] > max):
        max = d[i]
        key = i
print(f"Максимальное повторение элемента {key}- {max} раз.")


#  РЕШЕНИЕ 2 нужно доработать
# import random
# number = int(input('Введите n '))
# maxRandom = int(input('input max random number'))
# maxAmount = 0

# list = []
# count = [0] * (maxRandom+1)

# for i in range(0, number):
#     list.append(random.randint(0, maxRandom))

# for i in list:
#     count[int(i)] += 1

# for i in count:
#     if i > maxAmount:
#         i = maxAmount

# print(list)
# print(max(count))
# print('Максимальное количество раз появилась ' +
#       str(count[maxAmount]) + ', ' + str(maxAmount+1) +' раз')

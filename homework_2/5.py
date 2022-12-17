# 17 Реализуйте алгоритм перемешивания массива
import random
start = 0
end = 15
count = end
list = []  # упорядоченный список
list2 = []  # рандомный список
for i in range(start, end):
    list.append(i)
print(f'Исходный список {list}')

# Создаем второй список длиной равный первому с рандомными значеними элементов в диапазоне от 0 до длины первого списка
while count > 0:
    el = random.randint(start, end-1)
    if el in list2:
        continue
    else:
        list2.append(el)
        count -= 1

# Перемешиваем list
for i in range(start, end-1):
    indexList = i   # хранит индекс первого списка
    valueList = list[i]  # хранит значение первого списка
    i = list2[i]    # меняем индекс на значение первого элемента второго списка
    temp = list[i]  # temp хранит значение первого списка, которое будем менять
    list[i] = valueList  # меняем у значения valueList индекс
    list[indexList] = temp
print(f'Перемешаный список {list}')

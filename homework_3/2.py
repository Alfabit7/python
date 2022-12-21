# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random
a = 0
b = 10
y = 11
arrList = [random.randint(a, b) for i in range(y)]
end = len(arrList)-1
result = 0
newList = []

for i in range((end//2)+1):
    result = arrList[i]*arrList[end]
    newList.append(result)
    end -= 1
print(arrList)
print(newList)

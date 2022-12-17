# 17 Реализуйте алгоритм перемешивания массива
import random
start = 0
end = 10
count = end
list = []
list2 = []
for i in range(start, end):
    list.append(i)
print(list)

while count > 0:
    el = random.randint(start, end)
    if el in list2:
        continue

    else:
        list2.append(el)
        count -= 1
print(list2)

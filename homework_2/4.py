# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

userNumber = int(input('Введите число N '))
list = []
for i in range(-userNumber, userNumber+1):
    list.append(i)
print(list)


result = 0
# Считываем данные с файла
with open('homework_2/value.txt', 'r') as file:
    for line in file:
        # print(line, end="")
        result += list[int(line)]

print(result)

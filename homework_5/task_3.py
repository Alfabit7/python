# Обязательная:
# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

count = 1
text = '1112222442334555556677'
# text = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'
newText = ''
print(text)

# Кодирует
for i in range(len(text)-1):
    if text[i] == text[i+1]:
        count += 1
        if i == len(text)-2:  # Добавляет последний символ если он и предыдущий повторяются
            newText += str(count)+str(text[i+1])
    else:
        newText += str(count)+str(text[i])
        count = 1
        if i == len(text)-2:  # Добавляет последний символ если он не повторяется
            newText += str(count)+str(text[i+1])
print(newText)


# Раскодирует для букв
# newList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# count = ''
# oldText = ''
# for i in range(len(newText)):
#     if newText[i] in newList:
#         count += str(newText[i])
#     else:
#         oldText += newText[i]*int(count)
#         count = ''
# print(oldText)


# Раскодирует для цифр
count = 0
oldText = ''
for i in range(len(newText)-1):
    if i == 0:
        count = int(newText[i])
        oldText += str(str(newText[i+1])*count)

    elif i % 2 == 0 and i != 0:
        count = int(newText[i])
        oldText += str(str(newText[i+1])*count)

print(oldText)

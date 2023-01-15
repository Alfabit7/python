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
import numbers
count = 1
myTextNumber = '1112222442334555556677'
myTextLetters = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'
text = 'AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE'


# Кодирует строку
def Encodes(text: str):
    print(f'Source text: {text}')
    newText = ''
    count = 1
    for i in range(len(text)-1):

        if text[i] == text[i+1]:
            count += 1
            if i == len(text)-2:  # Добавляет последний символ если он и предыдущие повторяются
                newText += str(count)+str(text[i+1])
        else:
            newText += str(count)+str(text[i])
            count = 1
            if i == len(text)-2:  # Добавляет последний символ если он не повторяется
                newText += str(count)+str(text[i+1])
    print(f'Encodes text: {newText}')
    return newText

# Функция раскодирует строку


def Decodes(text):
    if text.isnumeric():
        # Раскодирует для цифр
        count = 0
        oldText = ''
        for i in range(len(text)-1):
            if i == 0:
                count = int(text[i])
                oldText += str(str(text[i+1])*count)

            elif i % 2 == 0 and i != 0:
                count = int(text[i])
                oldText += str(str(text[i+1])*count)
        print(f'Decodes text: {oldText}')
    else:
        # Раскодирует для букв
        newList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        count = ''
        oldText = ''
        for i in range(len(text)):
            if text[i] in newList:
                count += str(text[i])
            else:
                oldText += text[i]*int(count)
                count = ''
        print(f'Decodes text: {oldText}')
    return oldText


print()
encodeTexLetters = Encodes(myTextLetters)
Decodes(encodeTexLetters)
print()
encodeTextNumber = Encodes(myTextNumber)
Decodes(encodeTextNumber)
print()


# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".


text = 'Напишите прабвограмму, удаляющую из тексабвта все слова, содержащие "абв".'
text = text.split()

for element in text:
    if not 'абв' in element:
        print(element, end=' ')


# РЕШЕНИЕ2
data = 'аф фыв ыва ываабв, ывадлойц. Оывало абвываф, длоываабв.'
data = ' '.join(list(filter(lambda slovo: not 'абв' in slovo, data.split())))
print(data)

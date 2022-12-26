# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
polinomial_1 = ''
polinomial_2 = ''

with open("homework_4/polinomial_1.txt", "r") as file:
    for line in file:
        polinomial_1 = line
print(polinomial_1)

with open("homework_4/polinomial_2.txt", "r") as file:
    for line in file:
        polinomial_2 = line
print(polinomial_2)

polinomial_1 = polinomial_1.split('+')
polinomial_2 = polinomial_2.split('+')
print()
polinomial_1 = ('').join(polinomial_1).split('**')
polinomial_2 = ('').join(polinomial_2).split('**')
polinomial_1 = ('').join(polinomial_1).split()
polinomial_2 = ('').join(polinomial_2).split()
last_two_charts = 2
polinomial_1 = polinomial_1[:-last_two_charts]
polinomial_2 = polinomial_2[:-last_two_charts]
# ['4x8', '4x7', '24x6', '10x5', '96x4', '52x3', '88x2', '100x', '65']
print(f'polinoial_1 = {polinomial_1}')
# ['80x5', '85x4', '53x3', '86x2', '98x', '55']
print(f'polinoial_2 =  {polinomial_2}')
print()

newList = []
i = 0
for i in range(len(polinomial_1)):
    if 'x' in polinomial_1[i]:
        newList.append(polinomial_1[i])
        # newList[i] = polinomial_1[i]
    else:
        continue
print(f'newList = {newList}')


new_list_pow = []
polinomial_1 = []
for el in newList:
    index_x = el.find('x')  # 1
    index_after_x = int(index_x+1)
    len_el = len(el)  # 3

    polinomial_1.append(el[0:index_x])
    new_list_pow.append(el[index_after_x:len_el])

len_new_list_pow = int(len(new_list_pow))
del new_list_pow[len_new_list_pow-1]
print(f'коэффициент polinomial_1 = {polinomial_1}')
print(f'степень  polinomial_1 = {new_list_pow}')

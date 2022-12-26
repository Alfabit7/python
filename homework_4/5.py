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
polinomial_1 = ('').join(polinomial_1).split('**')
polinomial_2 = ('').join(polinomial_2).split('**')
polinomial_1 = ('').join(polinomial_1).split()
polinomial_2 = ('').join(polinomial_2).split()
last_two_charts = 2
polinomial_1 = polinomial_1[:-last_two_charts]
polinomial_2 = polinomial_2[:-last_two_charts]
# ['4x8', '4x7', '24x6', '10x5', '96x4', '52x3', '88x2', '100x', '65']
# print(f'polinoial_1 = {polinomial_1}')
# ['80x5', '85x4', '53x3', '86x2', '98x', '55']
# print(f'polinoial_2 =  {polinomial_2}')

print()
polinomial_1_str = ('x').join(polinomial_1)
polinomial_2_str = ('x').join(polinomial_2)
# print(polinomial_1_str)
# print(polinomial_2_str)
polinomial_1 = polinomial_1_str.split('x')
polinomial_2 = polinomial_2_str.split('x')
# print(f'polinominal_1 = {polinomial_1}')
# print(f'polinomial_2 = {polinomial_2}')
print()
list_1 = []
list_2 = []
list_3 = []
list_4 = []
for i in range(len(polinomial_1)):
    if i % 2 == 0:
        list_1.append(polinomial_1[i])
    else:
        # list_2.append(polinomial_1[i])
        continue


for i in range(len(polinomial_2)):
    if i % 2 == 0:
        list_2.append(polinomial_2[i])
    else:
        # list_4.append(polinomial_2[i])
        continue


len_polinomial_1 = len(list_1)
len_polinomial_2 = len(list_2)
if len_polinomial_1 > len_polinomial_2:
    max_len_polinomial = list_1
    min_len_polinomial = list_2
else:
    min_len_polinomial = list_1
    max_len_polinomial = list_2

diff = len(max_len_polinomial) - len(min_len_polinomial)
result_list = max_len_polinomial[:diff]
max_len_polinomial = max_len_polinomial[diff:]
print(max_len_polinomial)
print(min_len_polinomial)
for i in range((len(min_len_polinomial))):
    min_len_polinomial[i] = int(
        min_len_polinomial[i]) + int(max_len_polinomial[i])
print(min_len_polinomial)
print(result_list+min_len_polinomial)

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
polinomial_1 = ''
polinomial_2 = ''

with open("homework_4/polinomial_1.txt", "r") as file:
    for line in file:
        polinomial_1 = line

print()
print(polinomial_1)
print("+")

with open("homework_4/polinomial_2.txt", "r") as file:
    for line in file:
        polinomial_2 = line
print(polinomial_2)
print('=')

polinomial_1 = polinomial_1.split('+')
polinomial_2 = polinomial_2.split('+')
polinomial_1 = ('').join(polinomial_1).split('**')
polinomial_2 = ('').join(polinomial_2).split('**')
polinomial_1 = ('').join(polinomial_1).split()
polinomial_2 = ('').join(polinomial_2).split()
last_two_charts = 2
polinomial_1 = polinomial_1[:-last_two_charts]
polinomial_2 = polinomial_2[:-last_two_charts]

polinomial_1_str = ('x').join(polinomial_1)
polinomial_2_str = ('x').join(polinomial_2)

polinomial_1 = polinomial_1_str.split('x')
polinomial_2 = polinomial_2_str.split('x')

list_1 = []
list_2 = []
for i in range(len(polinomial_1)):
    if i % 2 == 0:
        list_1.append(polinomial_1[i])
    else:
        continue

for i in range(len(polinomial_2)):
    if i % 2 == 0:
        list_2.append(polinomial_2[i])
    else:
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

for i in range((len(min_len_polinomial))):
    min_len_polinomial[i] = int(
        min_len_polinomial[i]) + int(max_len_polinomial[i])

result_list = result_list+min_len_polinomial

k = len(result_list)-1
i = 0
result_str = ''
while i != int(len(result_list)-1):
    if i == 0:
        result_el = str(result_list[i])+'x**'+str(k)
        result_str = result_str + '' + result_el
    elif k == 1:
        result_el = ' + '+str(result_list[i])+'x'
        result_str = result_str + '' + result_el

    else:
        result_el = str(result_list[i])+'x**'+str(k)
        result_str = result_str + ' + ' + result_el
    i += 1
    k -= 1

result_str = result_str+' + ' + str(result_list[len(result_list)-1]) + ' = 0'
print()
print(result_str)
with open("homework_4/sum_polinomial.txt", "w") as somefile:
    somefile.write(result_str)

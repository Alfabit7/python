# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
directory_1 = 'homework_4/polinomial_1.txt'
directory_2 = 'homework_4/polinomial_2.txt'

# считываем строку с многочленом из файла


def Read_files(directory: str):
    with open(directory, "r") as file:
        for line in file:
            polinomial_1 = line
            return polinomial_1


polinomial_1 = Read_files(directory_1)
polinomial_2 = Read_files(directory_2)
print()
print(polinomial_1)
print("+")
print(polinomial_2)
print('=')

# Парсим коэффиценты из многочлена и записываем в список


def Parsing_ratio(polinomial: str):
    polinomial = polinomial.split('+')
    polinomial = ('').join(polinomial).split('**')
    polinomial = ('').join(polinomial).split()
    last_two_charts = 2
    polinomial = polinomial[:-last_two_charts]
    polinomial_str = ('x').join(polinomial)
    polinomial = polinomial_str.split('x')
    temp = []
    for i in range(len(polinomial)):
        if i % 2 == 0:
            temp.append(polinomial[i])
            # print(list_1)
        else:
            continue
    polinomial = temp.copy()
    return polinomial


polinomial_1 = Parsing_ratio(polinomial_1)
polinomial_2 = Parsing_ratio(polinomial_2)

# Находим находим длины многочленов и делаем срез с большого многочлена  по длине маленького
len_polinomial_1 = len(polinomial_1)
len_polinomial_2 = len(polinomial_2)
if len_polinomial_1 > len_polinomial_2:
    max_len_polinomial = polinomial_1
    min_len_polinomial = polinomial_2
else:
    min_len_polinomial = polinomial_1
    max_len_polinomial = polinomial_2
diff = len(max_len_polinomial) - len(min_len_polinomial)
result_list = max_len_polinomial[:diff]
max_len_polinomial = max_len_polinomial[diff:]

# считаем сумму коэффицентов многочленов и записываем в список sum_ratio
#  после чего склеиваем два списка: первый срез от большого коэффициенты которого не надо было складывать и просуммированный список sum_ratio
sum_ratio = []
for i in range((len(min_len_polinomial))):
    sum_ratio.append(i)
    sum_ratio[i] = int(
        min_len_polinomial[i]) + int(max_len_polinomial[i])
result_list = result_list+sum_ratio


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
print(result_str)
print()
with open("homework_4/sum_polinomial.txt", "w") as somefile:
    somefile.write(result_str)

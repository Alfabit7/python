# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
import random
import task_4

directory_1 = 'homework_4/polinomial_1.txt'
directory_2 = 'homework_4/polinomial_2.txt'
k = random.randint(2, 11)
task_4.Generate_polynomial('homework_4/polinomial_1.txt', k)
k = random.randint(2, 11)
task_4.Generate_polynomial('homework_4/polinomial_2.txt', k)

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


# РЕШЕНИЕ2
# import random
# # формируем словарь где ключ это степень, а значение это коээфициент Х многочлена

# def Generate_polinomial_dict():
#     user_number = int(input('Введите число, коэфицент многочлена: '))
#     my_dict = {}
#     print()
#     while user_number != -1:
#         my_dict[user_number] = random.randint(1, 100)
#         user_number -= 1
#     return my_dict

# # Формируем строку polinomial_str многочлена  из словаря my_dict где ключ степень значение коээфициент Х


# def Generate_string_polinomial(my_dict: dict):
#     polinomial_str = ''
#     char_x = 'x'
#     char_pow = '**'
#     char_plus = ' + '
#     for value, ratio in my_dict.items():
#         if value != 1 and value != 0:
#             polinomial_str = polinomial_str + \
#                 str(ratio) + char_x + char_pow + str(value) + char_plus
#         elif value == 0:
#             polinomial_str = polinomial_str+char_plus+str(ratio)
#         else:
#             polinomial_str = polinomial_str + str(ratio) + char_x
#     return polinomial_str

# # Строку многочлена конвертит в словарь где степень это ключ коэффициент это значение


# def Parsing_string_polinomial_to_dict(polinomial: str):
#     polinomial = polinomial.split('+ ')
#     new_dict = {}
#     j = len(polinomial)-1
#     for el in polinomial:
#         x_index = el.find('x')
#         if x_index != -1:
#             new_dict[j] = (el[:x_index])
#         else:
#             new_dict[j] = el
#         j -= 1
#     return new_dict

# polinomial__dict_1 = Generate_polinomial_dict()
# polinomial__dict_2 = Generate_polinomial_dict()
# polinomial_1 = Generate_string_polinomial(polinomial__dict_1)
# polinomial_2 = Generate_string_polinomial(polinomial__dict_2)


# # Находим большой и маленьккий словарь по длине
# if len(polinomial__dict_1) < len(polinomial__dict_2):
#     min_dict = polinomial__dict_1
#     max_dict = polinomial__dict_2
# else:
#     min_dict = polinomial__dict_2
#     max_dict = polinomial__dict_1

# # Складываем два словаря
# sum_dict = {}
# i = len(max_dict)-1
# while i != -1:
#     if i >= len(min_dict):
#         sum_dict[i] = max_dict[i]
#     else:
#         sum_dict[i] = int(max_dict[i])+int(min_dict[i])
#     i -= 1

# sum_dict = Generate_string_polinomial(sum_dict)
# print(f'polinomial_1= {polinomial_1}')
# print(f'polinomial_2= {polinomial_2}')
# print(f'sum_dict=  {sum_dict}')

# РЕШЕНИЕ 3
# num_1 = '83*x^2 + 43*x^1 + 57*x^0 = 0'#.replace(' ', '')
# num_1 = num_1[:num_1.find('=')].split('+')
# num_2 = '23*x^5 + 25*x^4 + 37*x^3 + 72*x^2 + 41*x^1 + 52*x^0 = 0'
# num_2 = num_2[:num_2.find('=')].split('+')

# my_dict = {}

# for elem in num_1:
#     elem = elem.strip()
#     key = int(elem[elem.find('^') + 1:])
#     my_dict[key] = int(elem[:elem.find('*')])
#     print(my_dict)

# for elem in num_2:
#     elem = elem.strip()
#     key = int(elem[elem.find('^') + 1:])
#     if key in my_dict:
#         my_dict[key] += int(elem[:elem.find('*')])
#     else:
#         my_dict[key] = int(elem[:elem.find('*')])


# my_str = ''
# for key, value in sorted(my_dict.items(),reverse=True):
#     my_str += f'{value}*x^{key} + '

# my_str = my_str[:my_str.rfind('+')] + '= 0'
# END РЕШЕНИЕ 3


# РЕШЕНИЕ4


# РЕШЕНИЕ 4
# num_1 = '83*x^2 + 43*x + 57 = 0'.replace(' ', '')
# num_1 = num_1[:num_1.find('=')].split('+')
# num_2 = '23*x^5 + 25*x^4 + 37*x^3 + 72*x^2 + 41*x + 52 = 0'.replace(' ', '')
# num_2 = num_2[:num_2.find('=')].split('+')
# num_all = num_1 + num_2

# my_dict = {}

# for elem in num_all:
#     if 'x' not in elem:
#         key = 0
#     elif '^' not in elem:
#         key = 1
#     else:
#         key = int(elem[elem.find('^') + 1:])

#     if key > 0:
#         if key in my_dict:
#             my_dict[key] += int(elem[:elem.find('*')])
#         else:
#             my_dict[key] = int(elem[:elem.find('*')])
#     else:
#         if key in my_dict:
#             my_dict[0] += int(elem)
#         else:
#             my_dict[0] = int(elem)
#     print(my_dict)

# my_str = ''
# for key, value in sorted(my_dict.items(),reverse=True):
#     if key == 0:
#         my_str += str(value)
#     elif key == 1:
#         my_str += f'{value}*x + '
#     else:
#         my_str += f'{value}*x^{key} + '

# my_str = my_str + ' = 0'

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

name_file = 'homework_4/polinomial.txt'
# k = int(input('Введите число k многочлена : '))
k = random.randint(2, 11)


def Generate_polynomial(name_file, k):
    poli_all = ''
    newList = []
    start_range = 0
    end_range = 100
    while k != 0:
        ratio_random = random.randint(start_range, end_range)
        if ratio_random != 0:
            if k != 1:
                poli_one_el = str(ratio_random)+'x**'+str(k)
                poli_all = poli_all + ' + ' + poli_one_el
                k -= 1
            else:
                poli_one_el = '+ '+str(ratio_random)+'x'+' +'
                poli_all = poli_all + ' ' + poli_one_el
                k -= 1
    newList = poli_all.split()
    ratio_random = random.randint(start_range, end_range)
    if ratio_random != 0:
        newList.append(ratio_random)
    newList.append(' = 0')
    del newList[0]  # Удаляем плюс в начале списка
    poli_all = ''
    for i in range(len(newList)):
        if i != len(newList):
            poli_all += str(newList[i])+' '
        else:
            poli_all = ' + '+str(newList[i])
    print(poli_all)

    with open(name_file, "w") as somefile:
        somefile.write(poli_all)
    return poli_all


# if __name__ == '__main__':
Generate_polynomial(name_file, k)


# РЕШЕНИЕ 2

# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# import random
# k = int(input())
# result = ""
# for i in range(k,-1,-1):
#     koeff = random.randint(0,3)
#     if koeff == 0:
#         continue
#     if koeff == 1:
#         if i == 1:
#             result += f"x+"
#         elif i == 0:
#             result += f"{koeff}"
#         else:
#             result += f"x**{i}+"
#     else:
#         if i == 1:
#             result += f"{koeff}*x+"
#         elif i == 0:
#             result += f"{koeff}"
#         else:
#             result += f"{koeff}*x**{i}+"
# result += " = 0"
# print(result)

# f = open("filepol.txt","w")
# f.write(result)
# f.close()

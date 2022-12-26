# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
inputFlag = True
userNumber = None
while inputFlag:
    try:
        userNumber = int(input('Enter number: '))
        inputFlag = False
    except:
        print('replay enter')

i = 0
f1 = 0
f2 = 1
sum = 0
oneList = [f1, f2]
twoList = None
for i in range(userNumber):
    sum = f1+f2
    oneList.append(sum)
    f1 = f2
    f2 = sum
twoList = oneList.copy()
twoList.reverse()

for i in range(len(twoList)):
    if i % 2 == 0:
        twoList[i] = (twoList[i])
    else:
        twoList[i] = (twoList[i]*-1)
twoList.remove(0)

mergeList = twoList+oneList
print(mergeList)

# РЕШЕНИЕ 2
# def postive_fib(n):
#     postive_list = [0,1]
#     for i in range(n-1):
#         postive_list.append(postive_list[-2]+postive_list[-1])
#     return postive_list
#
# def negative_fiv(n):
#     negative_list = [0,1]
#     for i in range(n-1):
#         negative_list.append(negative_list[-2]-negative_list[-1])
#     return negative_list
#
#
# print(negative_fiv(8)[::-1] + postive_fib(8)[1:])

# РЕШЕНИЕ 3
k = int(input('Введите число: '))

lst_fib = []


# Для положительных
a = 1
b = 1
for i in range(k):
    # Первым действие вставляем значение "а" в список, а затем выщитываем новое значение "а"
    lst_fib.append(a)
    temp = a  # храним значение "a" во временной переменной
    a = b  # значение "a" уже в списке, поэтому приравниваем новое значение, равное "b"
    b = temp + a  # следующее значение равно сумме прошлого и текущего значения "a"

# Для отрицательных
a = 0
b = 1
for i in range(k+1):
    # Каждый раз вставляем значение "a" на позицию с индексом 0
    lst_fib.insert(0, a)
    temp = a
    a = b
    b = temp - a

print(lst_fib)


# решение 2

# x = int(input("Введите любое натуральное число: "))

# a, b = 0, 1
# s = []
# s.append(a)
# s.append(b)

# for i in range(x - 1):
#     fib = a + b
#     s.append(fib)
#     a = b
#     b = fib

# a, b = 0, 1

# for i in range(x):
#     negfib = b - a
#     s.insert(0, negfib)
#     b = a
#     a = negfib
# print()
# print('Список чисел Фибоначчи, в том числе для отрицательных индексов: ')
# print()
# print(s)


# решение 3
# x = int(input("Введите любое натуральное число: "))

# a, b = 0, 1
# s = [0,1]

# for i in range(x - 1):
#     fib = a + b
#     s.append(fib)
#     a,b = b, fib
# a, b = 0, 1
# for i in range(x):
#     negfib = b - a
#     s.insert(0, negfib)
#     b = a
#     a = negfib
# print('Список чисел Фибоначчи, в том числе для отрицательных индексов: ')
# print(s)

# решение 3
# N = int(input('введите число Фибоначчи = '))

# Fib = [0, 1]
# negaFib = [1]

# for n in range(2, N+1):
#     f = Fib[n-2] + Fib[n-1]
#     Fib.append(f)
#     if n%2 == 0:
#         negaFib.insert(0, -(f))
#     else:
#         negaFib.insert(0, f)

# FinFib = negaFib + Fib

# print(f'{FinFib}')

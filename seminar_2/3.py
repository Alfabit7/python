# 13. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
one = input('Input string ')
two = input('Input secons string ')
count = 0
for i in range(len(one) - len(two) + 1):
    if one[i:i+len(two)] == two:
        count += 1
print(count)


# РЕШЕНИЕ 2
# one = input('Input string ')
# two = input('Input secons string ')
# print(one.count(two))


# РЕШЕНИЕ 3

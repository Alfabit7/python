import random
import math


# def PowX(x):
#     return x*x


# myArr = [lambda i: (i, i*i) for i in range(1, 20) if i % 2 == 0]

# myArr = [i for i in range(1, 20) if i % 2 == 0]

# РАБОТАЕТ
myArr = [i for i in range(1, 20)]
myArr = [lambda i: i*i for i in range(1, 20)]
# myArr = [PowX(i) for i in range(1, 20) if i % 2 == 0]
# myArr = list(map(lambda x: x*3, myArr))
print(myArr)


# print()
# for el in myArr:
#     print(pow(el, 2), end=" ")

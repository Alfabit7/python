# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
import random
myArr = [1, 2, 3, 4, 6, 7, 8, 9, 10, 12, 13, 14, 16, 18]

for i in range(1, len(myArr)):
    if myArr[i]-1 != myArr[i-1]:
        print(myArr[i]-1, end=' ')
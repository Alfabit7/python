# 42)Имеется упорядоченный список:
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

# Перебрать все элементы этого списка с помощью функций enumerate и элементы, стоящие на главной диагонали(имеющие равные индексы со списком и индексом элемента внутри списка), превратить в нули.

# enumerate

# a = [2, 4, 6, 8]
# for indx,val in enumerate(a):
#     if val>5:
#         a[indx] = 0
# print(a)

for indx, val in enumerate(A):
    for i in range(len(val)):
        if i == indx:
            val[i] = 0
            print(val)

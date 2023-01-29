# 41)Напишите программу на Python для поиска пересечения двух заданных массивов с помощью Lambda, filter.
arr1 = [1, 2, 3, 5, 7, 8, 9, 10, 11]
arr2 = [1, 2, 4, 8, 9, 11]

res = list(filter(lambda x: x in arr2, arr1))
print(res)



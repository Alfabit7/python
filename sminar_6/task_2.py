# 41)Напишите программу на Python для поиска пересечения двух заданных массивов с помощью Lambda, filter.
arr1 = [1, 2, 3, 5, 7, 8, 9, 10, 11]
arr2 = [1, 2, 4, 8, 9, 11]

res = list(filter(lambda x: x in arr2, arr1))
print(res)


# 43)Имеется список id сотрудников из 10 элементов, каждый id - случайное число от 1 до 100 (сделать с помощью list_comprehension)
# Имеется список имен сотрудников из 10 элементов(вручную)

# Сопоставьте каждому имени сотрудника его id по порядку, и выведите получившийся список кортежей.
# Отсортировать список по возрастанию id.

# Выведете имена сотрудников, получившие нечетное id.

# Решить с помощью zip, filter, lambda

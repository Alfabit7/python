# 43)Имеется список id сотрудников из 10 элементов, каждый id - случайное число от 1 до 100 (сделать с помощью list_comprehension)
# Имеется список имен сотрудников из 10 элементов(вручную)
# Сопоставьте каждому имени сотрудника его id по порядку, и выведите получившийся список кортежей.
# Отсортировать список по возрастанию id.

# Выведете имена сотрудников, получившие нечетное id.
# Решить с помощью zip, filter, lambda


import random
idPeople = [random.randint(1, 100) for i in range(11)]
arrName = ['Сергей1', 'Сергей2', 'Сергей3', 'Сергей4', 'Сергей5',
           'Сергей6', 'Сергей7', 'Сергей8', 'Сергей9', 'Сергей10']
print()
result = list(zip(idPeople, arrName))
print(result)
print()

# Сортируем массив по id и в новый записываем только нечетные id
result = list(filter(lambda x: True if x[0] % 2 != 0 else False, sorted(
    result, key=lambda x: x[0])))

print('Выводим только имена')
for indx, name in enumerate(result):
    print(name[1], end=' ')

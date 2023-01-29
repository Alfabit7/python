# import sorting
# import view


# def sort_names():
#     with open("worker_list.txt", "r") as file:
#         lst = file.readlines()
#         lst_with_lst = []
#         for line in lst:
#             a = line.strip().split(",")
#             lst_with_lst.append(a)
#         lst_with_lst = sorted(lst_with_lst, key=lambda x: x[1])
#         string_ = ""
#         for worker in lst_with_lst:
#             res = ",".join(worker)
#             string_ += res+"\n"
#     with open("worker_list.txt", "w") as file:
#         file.write(string_)


# def sort_id():
#     with open("worker_list.txt", "r") as file:
#         lst = file.readlines()
#         lst_with_lst = []
#         print(lst_with_lst)
#         for line in lst:
#             a = line.strip().split(",")
#             lst_with_lst.append(a)

#         lst_with_lst = sorted(lst_with_lst, key=lambda x: x[0])
#         string_ = ""
#         for worker in lst_with_lst:
#             res = ",".join(worker)
#             string_ += res+"\n"
#     with open("worker_list.txt", "w") as file:
#         file.write(string_)


# Задание: Создать телефонный справочник с возможностью импорта и экспорта данных.
# Модуль контроллер
# Модуль для импорта(ввода данных)
# Модуль для экспорта(вывод данных)
# Строка содержит id,имя,фамилию,номер телефона, комментрий - символ разделитель на выбор(можно использовать пробел или запятые) + файл с хранением этих строк
# *Добавить сортировку по имени или по id
# *Добавить вывод только имени и фамилии


# def start():
#     while True:
#         op = view.get_op()
#         if op == 1:
#             view.add_worker()
#         elif op == 2:
#             view.print_table()
#         elif op == 3:
#             view.print_only_name()
#         elif op == 4:
#             sorting.sort_names()
#         elif op == 5:
#             sorting.sort_id()
#         elif op == 6:
#             break


# def get_op():
#     op = int(input(
#         "1 - добавить пользователя \n 2 - вывести таблицу \n 3 - вывести только имя и фамилию \n 4 - отсортировать по именам \n 5 - отсортировать по id\n 6 - выход\n"))
#     return op

# def add_worker():
#     id = input()
#     name = input()
#     lastname = input()
#     number = input()
#     comments = input()
#     line = f"{id},{name},{lastname},{number},{comments}\n"
#     with open("worker_list.txt","a") as file:
#         file.write(line)
#     print("сохранено!")

# def print_table():
#     with open("worker_list.txt","r") as file:
#         for line in file.readlines():
#             print(line,end="")

# def print_only_name():
#     with open("worker_list.txt","r") as file:
#         lst = file.readlines()
#         for line in lst:
#             a = line.split(",")
#             print(f"Имя - {a[1]}, Фамилия - {a[2]}")


# import controller
# controller.start()

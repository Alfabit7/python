# Проверяет, что введено число, а не текст
# def InputNumbers(inputText):
#     is_OK = False
#     while not is_OK:
#         try:
#             number = int(input(f"{inputText}"))
#             is_OK = True
#         except ValueError:
#             print('Ошибка. Требуется ввод числа')
#     return number

# Функция бинарного поиска элемента по сортированному списку
myList = [1, 2, 3, 4, 5, 6, 25, 47, 4, 7]


def BynarySearch(arr: list, searchNumber: int):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2
        guess = arr[mid]
        if guess == searchNumber:
            return mid
        elif guess > searchNumber:
            end = mid-1
        else:
            start = mid+1
    return None


a = BynarySearch(myList, 4)
print(f'Индекс элемента {myList[a]} равен {a} ')
# END  Функция бинарного поиска элемента по сортированному списку

# import random
# # arrTuple = set()
# # while len(arrTuple) != 10:
# #     arrTuple.add(random.randint(0, 45))
# # print(arrTuple)
# # print(len(arrTuple))

# def GenerateRandomList():
#     arrTuple = set(random.randint(0, 15) for i in range(20))

# print(arrTuple)

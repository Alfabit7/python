
# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#    *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
a = float(input("Введите вещественное число: "))
if round(a, 0) == round(a, 8):
    print("нет")
else:
    print(int(a*10)-int(a)*10)
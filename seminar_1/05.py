# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

a = int(input())
if (a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30 != 0:
    print("условие выполняется")
else:
    print("условие не выполняется")

# n = float(input())
# print(int(n*10%10))
# n = input()
# a = n.split(".")
# print(a[1][0])

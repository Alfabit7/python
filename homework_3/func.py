# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# *Пример:*
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
# def dec_to_bin(num, result = ""):
#     if num == 0:
#         return result[::-1]
#     result += str(num%2)
#     return dec_to_bin(num//2,result)
#
#
# n = int(input())
#
# if n!=0:
#     print(dec_to_bin(n))
# else:
#     print(0)

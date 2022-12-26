# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math

number_pi = list(str(math.pi))
user_random = list(
    input('Введите число в диапазоне от 0.0000000001 до 0.1: '))
two_start_charts_number_pi = 2
d = int(len(user_random[2:]))+two_start_charts_number_pi
number_pi = ('').join(number_pi[:d])
print(number_pi)

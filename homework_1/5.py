# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# x b - x a) 2 + (y b - y a) 2
import math

a = [int(input('Введите координату x точки А ')),
     int(input('Введите координату Y точки А '))]
b = [int(input('Введите координату x точки B ')),
     int(input('Введите координату Y точки B '))]
result = math.sqrt(pow((b[0]-a[0]), 2) + pow((b[1]-a[1]), 2))
print(round.ceil(result, 2))

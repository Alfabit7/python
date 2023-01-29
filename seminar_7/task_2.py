import view
import math_operator


def start():
    type = view.get_type()
    if type:
        a, b = view.get_value_int()
    else:
        a, b = view.get_value_complex()

    math_operator.init(a, b)
    sign = view.get_sign(type)
    res = "ошибка знака"
    if sign == "+":
        res = math_operator.summ()
    elif sign == "-":
        res = math_operator.diff()
    elif sign == "*":
        res = math_operator.multi()
    elif sign == "/":
        res = math_operator.dellen()
    elif sign == "//":
        res = math_operator.cel_del()
    elif sign == "%":
        res = math_operator.proc_del()

    view.out_res(res)


x = 0
y = 0


def init(a, b):
    global x, y
    x = a
    y = b


def summ():
    return x+y


def multi():
    return x*y


def diff():
    return x-y


def dellen():
    return x/y


def cel_del():
    return x//y


def proc_del():
    return x % y


def get_type():
    type = int(input("ВВеди тип. 0 - комплексные, 1 - целые"))
    return type


def get_value_int():
    a = int(input("Введи число"))
    b = int(input("Введи число"))
    return a, b


def get_value_complex():
    a = complex(input("Введи число"))
    b = complex(input("Введи число"))
    return a, b


def get_sign(type):
    if type:
        sign = input()
        if sign in ["+", "-", "/", "%", "*", "//"]:
            return sign
        else:
            print("error input")
    else:
        sign = input()
        if sign in ["+", "-", "/", "*"]:
            return sign
        else:
            print("error input")


def out_res(res):
    print(res)

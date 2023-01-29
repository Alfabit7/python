import mat, in_out

def start():
    type_ = in_out.in_type()
    if type_ == 'целые':
        a = in_out.in_first_int()
        b = in_out.in_second_int()
        f = 0
    else:
        a = in_out.in_first_comp()
        b = in_out.in_second_comp()
        f = 1

    znak = in_out.in_znak()
    res = 0

    if znak == '+':
        res = mat.summ_nums(a, b)
    elif znak == '-':
        res = mat.sub_nums(a, b)
    elif znak == '*':
        res = mat.mult_nums(a, b)
    elif znak == '/':
        res = mat.div_nums(a, b)
    elif type_ == 'комплексные' and (znak == '//' or znak == '%'):
        print("Неверный ввод")
    elif znak == '//':
        res = mat.div_int(a, b)
    elif znak == '%':
        res = mat.div_rem(a, b)
    in_out.out(res)
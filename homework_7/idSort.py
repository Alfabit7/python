import view


def sortUserId(data_base):
    data_base = sorted(data_base, key=lambda x: x[0])
    view.show_database(data_base)
    return data_base

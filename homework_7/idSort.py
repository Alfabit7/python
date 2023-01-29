import view
<<<<<<< HEAD


=======
>>>>>>> 66bdcea59d2ac65161ae56ba5d3662cda6b774eb
def sortUserId(data_base):
    data_base = sorted(data_base, key=lambda x: x[0])
    view.show_database(data_base)
    return data_base

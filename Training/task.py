# Передача аргументов. Сопоставление аргументов по имени и позиции.
# Нельзя использовать изменяемые обьекты в качестве значений по умолчанию.

def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    print(my_list, id(my_list))


def append_to_dict(key, value, my_dict=None):
    if my_dict is None:
        my_dict = {}
    my_dict[key] = value
    print(my_dict)


# append_to_list(77)
# append_to_list(99)
# append_to_list(111)
# append_to_list(111, [])

append_to_dict(10,100)
append_to_dict(20,200)
append_to_dict(20,200,{'a':300})
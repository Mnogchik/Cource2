def task_1(str):
    slovar = {}
    for keys in str:
        if keys>'A' and keys < 'z':
            slovar[keys] = slovar.get(keys, 0) + 1
    return slovar


def task_2(list):
    new_list = set(list)
    count = 0
    for i in new_list:
        count += i
    return count


def task_3(cities):
    str = ''
    for i in range(len(cities)):
        if i != len(cities) - 1:
            str += (cities[i] + ', ')
        else:
            str += (cities[i] + '.')
    return str


def task_4(a, b):
    a = set(a)
    b= set(b)
    c = list(a&b)
    return c

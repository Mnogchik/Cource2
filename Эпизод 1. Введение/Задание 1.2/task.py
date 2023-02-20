import math


# Пример 1
def task_1(a, b):
    if (a > b):
        result_1 = (math.sqrt(a * b) - 3)
    elif (a == b):
        result_1 = (math.log10(2))
    elif (a < b):
        result_1 = ((math.log(a ** 3 + 1)) / b)
    return result_1


# Пример 2
def task_2(a, b):
    if (a < b):
        result_2 = (math.tan(a / b) + 1)
    elif (a == b):
        result_2 = math.tan(-1)
    elif (a > b):
        result_2 = (math.sqrt(a * b - 5) / a)
    return result_2


# Пример 3
def task_3(a, b):
    if (a > b):
        result_3 = math.log10(a * b) + 21
    elif (a == b):
        result_3 = math.tan(-5)
    elif (a < b):
        result_3 = (math.log(3 * (a / b)) + 1)
    return result_3


# Пример 4
def task_4(a, b):
    if (a > b):
        result_4 = math.sqrt(a * b - 1)
    elif (a == b):
        result_4 = math.log10(255)
    elif (a < b):
        result_4 = (math.tan(a - 5) / b)
    return result_4


# Пример 5
def task_5(a, b):
    if (a > b):
        result_5 = (math.log(a / b, math.e) + 31)
    elif (a==b):
        result_5 = math.tan(-25)
    elif (a<b):
        result_5 = (math.cos(a*5-1)/a)
    return result_5


# Пример 6
def task_6(a, b):
    if (a<b):
        result_6 = math.sqrt((b/a)+1)
    elif (a==b):
        result_6 = 5
    elif (a>b):
        result_6 = (math.log10(a**3-5)/b)
    return result_6

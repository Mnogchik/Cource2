# Пример 1
def task_1(n):
    X = 0
    for i in range(1, 11):
        X += 1 / i
    return X


# Пример 2
def task_2(x, n):
    Y = 0
    for i in range(1, 18, 2):
        Y += x / i
    return Y


# Пример 3
def task_3(n):
    Y = 1
    for i in range(1, n + 1):
        Y *= i
    return Y


# Пример 4
def task_4(x, n):
    Z = 1
    for i in range(2, 10):
        Z *= ((x + i) / i)
    return Z


# Пример 5
def task_5(x, n):
    Y = 1
    source_x = x
    for i in range(1, 2):
        x = (source_x * i)
        Y += (x / (i * 2))

    return Y


# Пример 6
def task_6(n):
    Z = 1
    for i in range(2, 21, 2):
        Z *= i
    return Z
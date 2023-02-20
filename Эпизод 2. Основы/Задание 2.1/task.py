
def task_1(N):
    f = 1
    for i in range(2, N + 1):
        f *= i
    return f


def task_2(N):
    otvet = int(((((1+(5**0.5))/2)**(N-1))-(((1-(5**0.5))/2)**(N-1)))/(5**0.5))
    return otvet


def task_3(N):
    a = []
    for i in range(1, N + 1):
        if N % i == 0:
            a.append(i)
    return a

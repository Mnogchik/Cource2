def task_1(list, var):
    index = 0
    for i in range(len(list)):
        if list[i] == var:
            return str(index)
        else:
            index += 1


def task_2(N):
    for i in range(2, N):
        if N%i==0:
            return False
    return True
# Пример 1
def task_1(A):
    sum_plus=0
    for i in range(len(A)):
        if A[i]>0:
            sum_plus+=A[i]
    return sum_plus


# Пример 2
def task_2(A):
    sr_arif = sum(A)/len(A)
    return sr_arif


# Пример 3
def task_3(A):
    sr_arif = sum(A)/len(A)
    sumsum=0
    for i in range(len(A)):
        sumsum+=((A[i]-sr_arif)**2)
    otvet=((sumsum/len(A))**0.5)
    return otvet

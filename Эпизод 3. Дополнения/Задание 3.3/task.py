def task_1(list):
    spis = [0] * 100
    for i in list:
        spis[i] += 1
    return spis.index(max(spis))


def task_2(X, Y):
    flag = False
    for i in X:
        if X.count(i) > 1:
            flag = True
    for i in Y:
        if Y.count(i) > 1:
            flag = True
    if flag:
        return "YES"
    else:
        return "NO"


def task_3(x, y, xc, yc, r):
    if abs(xc - x) > r or abs(yc - y) > r:
        flag = False
    else:
        flag = True
    return flag


def task_4(list):
    count = 0
    for i in range(1, len(list)-1):
        if list[i-1]<list[i]>list[i+1]:
            count+=1
    return count

def task_5(n):
    with open('file.txt') as file:
        str=file.read()
    spis=str.split("\n")
    spis.pop(-1)
    result=[""]*len(spis)
    for i in range(len(spis)):
        for j in spis[i]:
            if j!=' ':
                result[i]+=(chr(ord(j)+n)).lower()
            else:
                result[i]+='b'
    return result

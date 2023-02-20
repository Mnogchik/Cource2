#
def task_1(str):
    return len(str) - str.rindex(' ') - 1


def task_2(str):
    new_str = str.split(' ')
    for i in range(0, len(new_str) - 1, 2):
        new_str[i], new_str[i + 1] = new_str[i + 1], new_str[i]
    new_str = ' '.join(new_str)
    return new_str


def task_3(str):
    count = 0
    new_str = str.split(' ')
    for i in range(len(new_str) - 1):
        if new_str[i][-1] == new_str[i + 1][0]:
            count += 1
    return count

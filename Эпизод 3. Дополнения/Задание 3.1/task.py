def task_1(str):
    dict = {}
    text = str.split(". ")
    text[-1]=(text[-1])[:-1]
    for i in range(len(text)):
        words=text[i].split()
        dict[text[i]]=len(words)

    return dict

def task_2(x1, y1, x2, y2):
    return (((x2-x1)**2+(y2-y1)**2)**0.5)



def flist():
    l = list()

    for i in range(1, 21):
        l.append(i**2)
    t = tuple(l)
    print t

flist()

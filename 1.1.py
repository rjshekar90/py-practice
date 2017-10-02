
def f(x):

    l = []
    if x%7 == 0 and x%5 != 0:
        l.append(str(x))
    return l



print ",".join(filter(f, range(1, 10)))

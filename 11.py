
def even(lst):
    l = []
    for num in (lst):
        num = str(num)
        if int(num[0])%2 == 0 and int(num[1])%2 == 0 and int(num[2])%2 == 0 and int(num[3])%2 == 0:
            l.append(str(num))
        else:
            pass

    print ",".join(l)

even(range(1000, 3001))

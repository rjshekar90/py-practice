

from collections import defaultdict, Counter


def di(str):

    d = defaultdict(int)
    str = str.split(" ")
    for word in str:
        d[word] += 1

    for k, v in d.iteritems():
        return k,v

    return d
print di("hello there there 1 2 3")


from collections import defaultdict

def di(str):
    d = defaultdict(int)
    for word in str:
        if word.isalpha():
            d["letters"] += 1
        elif word.isdigit():
            d["nums"] += 1
        else:
            pass

    return d

print di("hello man 123")

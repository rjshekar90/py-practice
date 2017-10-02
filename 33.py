

def numGen(n):
    for i in range(n+1):
        if i%5 == 0 and i%7 == 0:
            yield i


n = raw_input(">>> ")
l = []
for i in numGen(n):
    values.append(str(i))

print ",".join(values)

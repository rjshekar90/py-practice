

l = []
while True:

    s = raw_input(">>>> ")
    if s:
        l.append(s)
    else:
        break

for sent in l:
    print sent.upper()


s = raw_input(">>>> ").split(" ")
j = sorted(set(s))

for sent in j:
    print "".join(sent),

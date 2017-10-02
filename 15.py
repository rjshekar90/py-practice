
a = raw_input(">>>> ")

n1 = "%s" % (a)
n2 = "%s%s" % (a, a)
n3 = "%s%s%s" % (a, a, a)
n4 = "%s%s%s%s" % (a,a,a,a)

print int(n1)+int(n2)+int(n3)+int(n4)

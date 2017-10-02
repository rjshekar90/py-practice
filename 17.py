
import sys
netamount = 0

while True:
    l = raw_input(">>> ")
    if l:
        l = l.split(" ")

        op = l[0]
        val = int(l[1])

        if op == "D":
            netamount += val
        elif op == "W":
            netamount -= val
        else:
            pass

    else:
        break

print netamount

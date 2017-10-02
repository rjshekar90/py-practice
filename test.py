
# print [(x,y) for x in [1,2,3] for y in [2,3,4] if x==y]



'''
ques = ["hello", "Raja"]
ans = ["world", "Shekar"]

for i, j in zip(ques, ans):
    print i, j
'''

'''
import sys
netAmount = 0
while True:
    s = raw_input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print netAmount

'''

def reverse(s):
    l = []
    s = s.split(" ")
    #print s
    for i in s:
        l.append(i[::-1])

    #return "".join(str(l))

    for x in l:
        print x,

reverse("hello world")

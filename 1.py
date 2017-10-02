
def div(lists):

     l = []

     for i in range(len(lists)):
         if lists[i]%7 == 0 and lists[i]%5 != 0:
             l.append(str(lists[i]))

     return ",".join(l)

print div(range(2000, 3201))

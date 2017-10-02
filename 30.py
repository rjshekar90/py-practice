

l = [1,2,3,4,5,6,7,8,9,10]

#y = filter(lambda x: x%2 == 0, l)

y = map(lambda x : x**2, filter(lambda x: x%2 == 0, l))
print y

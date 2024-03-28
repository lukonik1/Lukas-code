x = [1]
print (x[0])
x.append(1)
print (x[0] + x[1])
x.append(x[0] + x[1])
del x[0]
while not x[1] > 1000000000000000000000000000000000000:
    print (x[0] + x[1])
    x.append(x[0] + x[1])
    del x[0]




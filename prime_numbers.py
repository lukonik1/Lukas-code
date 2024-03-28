x = 2
y =[2]
z = False
while x < 1000:
    z = False
    for number in y:
        if x % number == 0:
            z = True
        else:
            pass
    if not z:
        y.append(x)
        x += 1
    else:
        x += 1
print(y)

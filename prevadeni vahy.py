vaha = float (input ("vaha: "))
vaha_kg = vaha / 2.2
vaha_lb = vaha/ 0.45
kglb = input ("(K)g or (L)b: ")
if kglb.upper() == 'K':
    print ("vaha v librach: " + str(vaha_lb))
if kglb.upper() == 'L':
    print ("vaha v kilech: " + str(vaha_kg))


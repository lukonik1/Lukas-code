from random import randint

def prohra(hrac, pocitac):
    print("prohral jsi, " + pocitac + " prebije " + hrac)
def vyhra(hrac, pocitac):
    print("vyhral jsi, " + hrac + " prebije " + pocitac)


t = ["kamen", "nuzky", "papir"]
pocitac = t[randint(0,2)]
hrac = False
while hrac == False:
    hrac = input("kamen, nuzky, papir?: ")
    if hrac == pocitac:
        print("remiza")
    elif hrac == "kamen":
        if pocitac == "papir":
            prohra(hrac, pocitac)
        else:
            vyhra(hrac, pocitac)
    elif hrac == "nuzky":
        if pocitac == "kamen":
            prohra(hrac, pocitac)
        else:
            vyhra(hrac, pocitac)
    elif hrac == "papir":
        if pocitac == "nuzky":
            prohra(hrac, pocitac)
        else:
            vyhra(hrac, pocitac)
    elif hrac == 'exit':
        break
    else:
        print("spatne jsi zadal")
    hrac = False
    pocitac = t[randint(0,2)]







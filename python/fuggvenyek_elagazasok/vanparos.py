def vanParos(x):
    i = 0
    while i < len(x) and not(x[i] % 2 == 0):
        i += 1
    return i < len(x)
         
def ki(vanE):
    if vanE:
        print("Van benne páros!")
    else: 
        print("Nincs benne paros!")

szamok = [5, 2, 3, 7, 13]
vanE = vanParos(szamok)
ki(vanE)
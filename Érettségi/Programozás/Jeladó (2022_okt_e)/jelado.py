def beolvas(o, p, mp, xs, ys):
    fr = open("jel.txt", "r")
    sor = fr.readline()
    while sor != "":
        sor = sor.split()
        o.append(int(sor[0]))
        p.append(int(sor[1]))
        mp.append(int(sor[2]))
        xs.append(int(sor[3]))
        ys.append(int(sor[4]))
        sor = fr.readline()
    fr.close()

def feladat2(xs, ys):
    print("\n2. feladat")
    sorszam = int(input("Adja meg a jel sorszámát! "))
    print("x=" + str(xs[sorszam-1]) + " y=" + str(ys[sorszam-1]))

def eltelt(o1, p1, mp1, o2, p2, mp2):
    ido1 = o1 * 3600 + p1 * 60 + mp1
    ido2 = o2 * 3600 + p2 * 60 + mp2
    return abs(ido1 - ido2)

def f4(o, p, mp):
    print("\n4. feladat")
    utso = len(o) - 1 #utso indexe
    ido = eltelt(o[0], p[0], mp[0], o[utso], p[utso], mp[utso])
    ora = ido // 3600
    ido = ido % 3600
    perc = ido // 60
    mperc = ido % 60
    print("Időtartam: " + str(ora) + ":" + str(perc) + ":" + str(mperc))

# Megadja, hogy az adott elteres szerint hany db jel maradt ki?
def kimaradt(elteres, hanyados):
    if elteres % hanyados == 0:
        return elteres // hanyados - 1
    else:
        return elteres // hanyados

def f7(orak, percek, mpercek, xs, ys):
    fw = open("kimaradt.txt", "w", encoding="utf-8")
    for i in range(1, len(orak)): #2-tol utso-ig
        #i-1-edik es i-edik kozott mennyi telt el?
        idoelteres = eltelt(orak[i-1], percek[i-1], mpercek[i-1], orak[i], percek[i], mpercek[i])
        #idodb: Hany jelzes maradt ki az ido miatt?
        idodb = kimaradt(idoelteres, 300)
        xelteres = abs(xs[i-1] - xs[i])
        xdb = kimaradt(xelteres, 10)
        yelteres = abs(ys[i-1] - ys[i])
        ydb = kimaradt(yelteres, 10)
        
        #Kell-e kivalogatni?
        koorddb = max(xdb, ydb)
        if idodb >= 1 or koorddb >= 1:
            if idodb > koorddb:
                fw.write(str(orak[i]) + " " + str(percek[i]) + " " + str(mpercek[i]) + " időeltérés " + str(idodb) + "\n")
            else:
                fw.write(str(orak[i]) + " " + str(percek[i]) + " " + str(mpercek[i]) + " koordináta-eltérés " + str(koorddb) + "\n")
    fw.close()

def f5(xs,ys):
    minx = min(xs)
    maxx = max(xs)
    miny = min(ys)
    maxy = max(ys)
    print()


def main():
    orak, percek, mpercek, xs, ys = [], [], [], [], []
    beolvas(orak, percek, mpercek, xs, ys)
    feladat2(xs, ys)
    #print(eltelt(2, 15, 20, 3, 30, 15)) #2:15:20-3:30:15
    f4(orak, percek, mpercek)
    f7(orak, percek, mpercek, xs, ys)

main()

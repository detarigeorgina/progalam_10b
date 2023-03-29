def beolvas(d, c, e, i, m):
    fr = open("lista.txt", "r")
    sor = fr.readline().strip()
    while sor != "":
        d.append(sor)
        sor = fr.readline().strip()
        c.append(sor)
        sor = fr.readline().strip()
        e.append(sor)
        sor = fr.readline().strip()
        i.append(int(sor))
        sor = fr.readline().strip()
        m.append(int(sor))
        sor = fr.readline().strip()
    fr.close()
    # print(i)


def ki(n):
    print("\n" + str(n) + ". feladat")


def feladat2(datumok):
    ki(2)
    db = 0
    for i in range(len(datumok)):
        if datumok[i] != "NI":
            db += 1
    print("A listában " + str(db) + " db vetítési dátummal rendelkező epizód van.")


def feladat3(megneztek):
    ki(3)
    db = 0
    for i in range(len(megneztek)):
        if megneztek[i] == 1:
            db += 1
    arany = db / len(megneztek) * 100
    print("A listában lévő epizódok " + str(round(arany, 2)) + "%-át látta.")


def feladat4(idotartamok, megneztek):
    ki(4)
    ido = 0
    for i in range(len(megneztek)):
        if megneztek[i] == 1:
            ido += idotartamok[i]
    nap = ido // (60 * 24) #Hany nap ez az ido?
    ido = ido % (60 * 24) #Mennyi perc marad ami mar egesz napot sem tesz ki?
    ora = ido // 60 #Hany ora marad?
    perc = ido % 60 #Hany perc marad ami mar egesz orat sem tesz ki?
    print("Sorozatnézéssel", nap, "napot", ora, "órát és", perc, "percet töltött.")


def feladat5(datumok, megneztek, epizodok, cimek):
    ki(5)
    date = input("Adjon meg egy dátumot! Dátum= ")
    for i in range(len(datumok)):
        if datumok[i] <= date and megneztek[i] == 0:
            print(epizodok[i] + "\t" + cimek[i])


def hetnapja(ev,ho,nap):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev = ev - 1
        return napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho-1] + nap ) % 7]


def feladat7(datumok, cimek):
    ki(7)
    hetnap = input("adja meg a hét egy napját (pédául cs)! nap = ")
    sorozatok = []
    for i in range(len(datumok)):
        if datumok[i] != "NI" and cimek[i] not in sorozatok:
            darabok = datumok[i].split(".")
            ev = int(darabok[0])
            honap = int(darabok[1])
            nap = int(darabok[2])
            if hetnapja(ev, honap, nap) == hetnap:
                sorozatok.append(cimek[i])
    for i in range(len(sorozatok)):
            print(cimek[i])
    if len(sorozatok) == 0:
        print("Az adott napon nem kerul adasba sorozat.")
    

    def feladat8(cimek, idotartamok):
        fw = open("summa.txt", "w")
        db = 1 #games
        ido = idotartamok[0] #60
        for i in range(1, len(cimek)):
            if cimek[i] != cimek[i-1]:
                fw.write(cimek[i-1] + " " + str(ido) + " " + str(db) + "\n")
                db = 1
                ido = idotartamok[i]
            else:
                db += 1
                ido += idotartamok[i]
        fw.write(cimek[len(cimek)-1], + " " + str(ido) + " " + str(db) + "\n")
        fw.close()


def main():
    datumok = [] #str
    cimek = [] #str
    epizodok = [] #str
    idotartamok = [] #int
    megneztek = [] #int
    beolvas(datumok, cimek, epizodok, idotartamok, megneztek)
    # print(cimek)
    feladat2(datumok)
    feladat3(megneztek)
    feladat4(idotartamok, megneztek)
    feladat5(datumok, megneztek, epizodok, cimek)
    feladat7(datumok, cimek)
    feladat8(cimek, idotartamok)
main()
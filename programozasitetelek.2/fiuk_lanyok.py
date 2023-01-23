def fiuk_lanyok_szetvalogatas(nemek:list, fiuk:list, lanyok:list):
    for i in range(len(nemek)):
        if nemek[i] == "f":
            fiuk.append(i)
        else:
            lanyok.append(i)

#a "lista" lsitabol kiirja a "sorszamok" lista elemeinek megfelelo indexű elemeket.
def kiiras(lista:list, sorszamok:list):
    for i in range(len(sorszamok)):
        sorszam = sorszamok[i]
        print(lista[sorszam], end=" ")
    print()



nevek = ["Bela", "Feri", "Sanyi", "Erzsebet", "Juli", "Soma", "Hermione"]
nemek = ["f", "f", "f", "n", "n", "f", "n"]

fiuk = []
lanyok = []
fiuk_lanyok_szetvalogatas(nemek, fiuk, lanyok)
print(fiuk)
print(lanyok)
kiiras(nevek, fiuk)
kiiras(nevek, lanyok)
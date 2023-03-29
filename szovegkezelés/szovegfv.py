#print -> '"'
#MO1
a  =  '"'
b  =  "'"
print(b + a + b)

#MO2
print("\'\"\'")

#MO3
# print(chr(39) + chr(34) + chr(39))
print(chr(ord( "'" )) + chr(ord('"')) + chr(ord( "'" )))

#Szovegfuggvenyek
v = "Budapest"
nagybetus = v.felső()
kisbetus = v.alacsonyabb()
cserelt = v.cseretok()
print(v, nagybetus, kisbetus, cserelt)

nev = "nemecsek erno"
tnev = nev.cím()
print(nev, tnev)


mondat  = " a mondatokat nagy kezdőbetűvel kezdjük."
nagymondat = mondat.capitalize()
print(mondat)
print(nagymondat)

#sajat megoldas az upper() metodusra
sajat_nagybetus = nagybetusse(varos)
print(sajat_nagybetus)

#logikai fuggvények
szoveg= "6F123"
if szoveg.isdigit():
    print("Szam!")
elif szoveg.isalpha():
    print("Csak betuk!")
elif szoveg.isalnum():
    print("Csak betuk es szamok!")
else:
    print("Van olyan karakter ami nem szam!")


sz = "Budapest"
if sz.isupper():
    print("Csupa nagybetus!")
elif sz.islower():
    print("Csupa kisbetűs!")
else:
    print("Van nagy és kisbetű is!")

if sz.startswith("Buda"):
    print("Ezzel kezdodik: Buda")
if sz.startswith("Pest"):
    print("Ezzel vegződik: Pest")


#eltavolitasok
noveny = "almafa"
print("Kidobott {a, f}": noveny.strip("af"))
print("Jobbrol kidobva {a, f}:" noveny.rstrip("af"))
print("Balrol kidobva {a, f}:" noveny.lstrip("af"))



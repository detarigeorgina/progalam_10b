

#2-től m-ig mnden szamrol eldöntjük, hogy prim-e
m = int(input("m: "))


j = 2
while j <= m:

    n = j 
    primE = True

i = 2 
while i < n and primE:
    if n % i == 0:
        primE == False
    i+= 1

if primE:
    print(j, end=" ")


'''j = 2
while j <= m:
    if m % j == 0:
        j+= 1

j += 1'''


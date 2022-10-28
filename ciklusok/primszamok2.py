

#2-től m-ig mnden szamrol eldöntjük, hogy prim-e
m = int(input("m: "))
print(2, end=" ")


j = 3
while j <= m:

    n = j 
    primE = True

i = 2 
while i < n // 2 and primE:
    if n % i == 0:
        primE == False
    i+= 1

if primE:
    print(j, end=" ")


x = float(input("x: ")) #mennyi a gyok?

#Kezdeti intervallum: [0, x]
bal = 0
jobb = x
print(bal,jobb)

for i in range(50):
    felezo = (bal + jobb) / 2
    if felezo*felezo < x: #jobb interallumban megyunk
        bal = felezo
    else:
        jobb = felezo
    print(bal, jobb)



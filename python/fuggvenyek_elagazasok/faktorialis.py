def fact(n):
    if n < 0:
        return -1
    eredmeny = 1
    for i in range(1, n+1):
        eredmeny = eredmeny * i
    return eredmeny

print(fact(5)) #120
print(fact(8)) #40320
print(fact(-3))

#10 alatt a 3?
#n_alatt_k = fact(10)/(fact(3)*fact(7))
sz = fact(10)
n = fact(3) * fact(7)
n_alatt_k = sz / n
print(n_alatt_k)



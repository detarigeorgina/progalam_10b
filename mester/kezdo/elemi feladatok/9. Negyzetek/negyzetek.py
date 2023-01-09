from math import *

n = int(input())

# akt:aktuálisan hátralévő négyzetek száma 
akt = n
while akt > 0:
    k = int(sqrt(akt))
    print(k, end=" ")
    akt = akt - k*k
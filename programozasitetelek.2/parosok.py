x = [ 7, 3, 4, 2, 1, 0, -8]


y = []
for i in range(len(x)):
    if x[i] % 2 == 0:
        y.append(i)

#kiiras
print(x)
# print(y)
#soszam kiirasa 
for i in range(len(y)):
    print(y[i]+1, end=" ")
    #ertek kiirasa 
    print()
for i in range(len(y)):
    print(x[y[i] ], end=" ")
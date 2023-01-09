n = int (input("n: "))

 for i in range(n, 1001):
    if (1001-i) % n ==0:
        print(1000-i, end=" ") 
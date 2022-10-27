n = int(input("oszalyzat: "))
jo = 1 <= n and n <= 5
while not jo:
    print("nem jo: 1<=n<=5")
    n = int(input("osztalyzat:"))
    jo = 1 <= n and n <= 5
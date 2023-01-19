def ki(n):
    if n % 3 == 0 and n % 7 == 0:
        print(n, "3-mal oszthato es 7-tel oszthato")
    if n % 3 == 0:
        print(n, "3-mal oszthato")
    elif n % 7 == 0:
        print(n, "7-mal oszthato")
    else:
        print(n, "Sem 3-mal sem 7-tel")


ki(12)
ki(14)
ki(13)
ki(21)
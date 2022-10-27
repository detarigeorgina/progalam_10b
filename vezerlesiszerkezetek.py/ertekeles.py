pontszam = int(input("pontszam: "))

if 0 <= pontszam and pontszam <=42:
    print("elegstelen")
elif pontszam <=57:
    print("elegseges")
elif  pontszam <=72:
    print("kozepes")
elif  pontszam <=87:
    print("jo")
else:
    print("jeles")
    
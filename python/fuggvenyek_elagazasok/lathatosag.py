def f():
   global x
   x = 5
   print("Fv-ben:", x)

x = 6
print("Fv elott:", x)
f()
print("Fv utan:", x)
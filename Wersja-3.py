'''a = float(input("a = "))
print(f"Obj szesc V = {a**3}")'''


'''from random import randint
for x in range(10):
    x = randint(1, 500)
    print(x)'''


'''s = 0
i = 0
while True:
    int = input("n or stop: ")
    if int == "stop":
        break
    s += float(int)
    i += 1
print(f"suma = {s}")
print(f"sr ar = {s/i}")'''


'''a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a**2 + b**2 == c**2 or c**2 - a**2 == b**2 or c**2 - b**2 == a**2:
    print("Trojkat jest prostokatny")
elif a == b == c and a**2 + b**2 == c**2 or c**2 - a**2 == b**2 or c**2 - b**2 == a**2:
    print("Trojkat jest prostokatny i rownoboczny")
elif a == b or b == c or a == c and a**2 + b**2 == c**2 or c**2 - a**2 == b**2 or c**2 - b**2 == a**2:
    print("Trojkat jest prostokatny i rownoramienny")
else:
    print("Trojkat nie jest prostokatny")'''


'''k = int(input("Podaj liczbe k:"))
m = int(input("Podaj liczbe m:"))
reszta = k % m
print(f"Reszta z dzielenia {k} przez {m} to {reszta}")'''


k = int(input("Podaj liczbe k:"))
m = int(input("Podaj liczbe m:"))
wynik = k // m
print(f"Wynik dzielenia {k} przez {m} to {wynik}")

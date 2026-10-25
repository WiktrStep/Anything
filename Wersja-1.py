'''import math
r = float(input("r = "))
print(f"V = {4/3*math.pi*r**3}")'''


'''n = input("n = ")
n = int(n)
while n > 0:
    print(f"{n} kocham prodramowac")
    n -= 1'''


'''s = 0
while True:
    int = input("n or stop: ")
    if int == "stop":
        break
    s += float(int)
print(s)'''


'''s = 0
i = 0
while True:
    int = input("n or stop: ")
    if int == "stop":
        break
    s += float(int)
    i += 1
print(s/i)'''


'''n = int(input("n = "))
s = 0
while n > 0:
    s += 2**n
    n -= 1
print(s)'''


from random import randint
i = 6
odp_poprawne = 0
while i > 0:
    n1 = randint(1, 10)
    n2 = randint(1, 10)
    iloczyn = n1*n2
    print(f"Jaki jest iloczyn {n1}*{n2}")
    inp = int(input(": "))
    if inp == n1*n2:
        odp_poprawne += 1
        print("Dobrze")
    else:
        print(f"Zle. Poprawna odpowiedz to {iloczyn}")
    i -= 1
print(f"Cykl sie zakonczyl. Wprowadz dane osobowe")
imie = input("Podaj imie: ")
nazwisko = input("Podaj nazwisko: ")
print(f"Witaj {imie} {nazwisko}. Twoja ocena to {odp_poprawne}")



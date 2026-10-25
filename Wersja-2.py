'''Pp = float(input("Pp = "))
h = float(input("h = "))
print(f"Obj szes V = {1/3*Pp*h}")'''


'''from random import randint
count = 3
while count > 0:
    random_number1 = randint(1, 10)
    random_number2 = int(input("Podaj liczbe: "))
    if random_number1 == random_number2:
        print("Zgadles liczbe")
        break
    else:
        print("Zle. Sprobuj jeszcze raz")
    if count == 1:
        print(f"Nie zgadles liczby {random_number1}. Brak kolejnych prob")
    count -= 1'''


'''number1 = 0
while True:
    number2 = input("Podaj liczbe or wpisz stop: ")
    if number2 == "stop":
        break
    else: 
        if number1 < int(number2):
            number1 = int(number2)
if number1 == 0:
    print("Uzytkownik nie wprowadzil zadnych liczb lub kazda z prowadzonych liczb jest rowna 0")
else:
    print(f"Najwieksza liczba to {number1}")'''


'''a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a**2 + b**2 == c**2 or c**2 - a**2 == b**2 or c**2 - b**2 == a**2:
    print("Trojkat jest prostokatny")
else:
    print("Trojkat nie jest prostokatny")'''


from random import randint
n = int(input("Wprowadz dlugosc odcinka: "))
if n <= 2:
    print("Dlugosc n musi byc wieksza niz 2, aby mozna podzielic na 3 czesci")
else:
    p1 = randint(1, n-1)
    p2 = randint(1, n-1)
    while p1 == p2:
        p2 = randint(1, n-1)
if p1 > p2:
    p1, p2 = p2, p1
odcinek1 = p1
odcinek2 = p2 - p1
odcinek3 = n - p2
print(f"Odcinek 1: {odcinek1}, Odcinek 2: {odcinek2}, Odcinek 3: {odcinek3}")

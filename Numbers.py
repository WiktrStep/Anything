#1. Utwórz pustą listę o nazwie "numbers"
#2. Poproś użytkownika o podanie 5 liczb i dodaj je do listy.
numbers = []
x = 5 
while x > 0:
    k = float(input("Podaj liczbę: "))
    numbers.append(k)
    x -= 1
print(numbers)

numbers = []
for _ in range(5):
    k = float(input("Podaj liczbę: "))
    numbers.append(k)
print(numbers)







#3. Oblicz sumę liczb znajdujących się w liście "numbers".
s = 0
for el in numbers:
    s += el
print(s)

s = 0
i = 0
while i < len(numbers):
    s += numbers[i]
    i += 1
print(s)







#4. Znajdź największą liczbę w liście "numbers".
numbers = [5, 10, -99, -15]
if len(numbers) != 0:
    max_number = numbers[0]
    for el in numbers:
        if el > max_number:
            max_number = el
    print(max_number)
else:
    print("Lista 'numbers' jest pusta.")

numbers = [5, 10, -99, -15]
if len(numbers) != 0:
    max_number = numbers[0]
    i = 0
    while i < len(numbers):
        if numbers[i] > max_number:
            max_number = numbers[i]
        i += 1
    print(max_number)
else:
    print("Lista 'numbers' jest pusta.")


#5. Znajdź najmniejszą liczbę w liście "numbers".
if len(numbers) != 0:
    min_number = numbers[0]
    for el in numbers:
        if el < min_number:
            min_number = el
    print(min_number)
else:
    print("Lista 'numbers' jest pusta.")




#6. Znajdź średnią arytmetyczną liczb w liście "numbers".
if len(numbers) != 0:
    s = 0
    for el in numbers:
        s += el
    average = s / len(numbers)
    print(average)
else:
    print("Lista 'numbers' jest pusta.")






#7. Znajdź ilość liczb parzystych w liście "numbers".
count = 0
for el in numbers:
    if el % 2 == 0:
        count += 1
print(count)







#8. Stwórz nową listę o nazwie "duplicates" zawierającą powtarzające się elementy z listy "numbers".
duplicates = []

for el in numbers:
    if numbers.count(el) > 1 and el not in duplicates:
        duplicates.append(el)

print(duplicates)







#9. Usuń wszystkie powtarzające się elementy z listy "numbers".
unique_numbers = []

for el in numbers:
    if el not in unique_numbers:
        unique_numbers.append(el)

numbers = unique_numbers
print(numbers)  





#10. Stwórz nową listę o nazwie "squares" zawierającą kwadraty liczb z listy "numbers".
squares = []

for el in numbers:
    squares.append(el ** 2)

print(squares)
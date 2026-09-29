# i = 0
# while i < 10:
  #  print(i)
  #  i += 1
  
# i = 0
# print(i)
# i = i + 1
# print(i)
# i = i + 1
# print(i)

# i = 0
# print(i)
# i += 1
# print(i)
# i += 1
# print(i)

# n = int(input())
# while n > 0:
#     if n % 7 == 0:
#         print(f"{n} jest podzielne przez 7")
#     n -= 1

n = int(input())
while n > 0:
    if n % 7 != 0:
        print(f"{n} jest podzielne przez 7")
    n -= 1

ile = 0
n = int(input())
while n > 0:
    if n % 7 == 0:
        ile += 1
    n -= 1
print(ile)
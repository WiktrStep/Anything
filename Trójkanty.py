# import math 
# PI = math.pi
# print(PI)

# print("licze pp kola")
# r = float(input("r = "))
# print(f" dla {r} pp kola = {PI*r**2}")

# print("licze ll prost")
# a = float(input("a = "))
# b = float(input("b = "))
# print(f"pp prost z a={a} b={b} = {a*b}")

# a = float(input("a="))
# b = float(input("b="))
# c = float(input("c="))
# if a + b > c:
#     if c + b > a:
#         if c + a > b:
#             print("Tak")
#         else: 
#             print("Nie")
#     else:
#         print("nie")
# else:
#     print("Nie") 


a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("To jest tr rownoboczny")
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
           print("To jest troj rownoramienny i prostokatny")
        else:
            print("To jest tr rownoramienny")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("To jest tr prostokatny roznoboczny")
    else:
        print("To jest tr roznoboczny")
else:
    print("Nie")
import math
PI = math.pi
print(PI)


print("a - bryly, b - figury plaskie")
inp = input(": ").lower().strip()
if inp == "a":
    print("a - pole powierzchni, b - objetosc")
    inp = input(": ").lower().strip()
    if inp == "a": 
        print("a - szeszcianu, b - prostopadloscianu, c - graniastoslupa, d - ostroslupa, e - waleca, f - stozka, g - kuli")
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input(" a = ")) 
            print(f"pp szescianu = {6*a**2}")
        elif inp == "b":
            a = float(input(" a ="))
            b = float(input(" b ="))
            c = float(input(" c ="))
            print(f"pp prostopadloscianu {a} {b} {c} = {2*a*b + 2*a*c + 2*b*c}")
        elif inp == "c":
            Pp = float(input(" Pp ="))
            Pb = float(input(" Pb ="))
            print(f"pp graniastoslupa {Pp} {Pb} = {2*Pp + Pb}")
        elif inp == "d":
            Pp = float(input(" Pp ="))
            h = float(input(" h ="))
            print(f"pp ostroslupa {Pp} {h} = {Pp + h}")
        elif inp == "e":
            r = float(input(" r ="))
            h = float(input(" h ="))
            print(f"pp walca {r} {h} = {2*PI*r**2 + 2*PI*r*h}")
        elif inp == "f":
            r = float(input(" r ="))
            l = float(input(" l ="))
            print(f"pp stozka {r} {l} = {PI*r**2 + PI*r*l}")
        elif inp == "g":
            r = float(input(" r ="))
            print(f"pp kuli {r} = {4*PI*r**2}")
        else:
            print("nie ma takiej komendy")
    elif inp == "b": 
        print("a - szeszcianu, b - prostopadloscianu, c - graniastoslupa, d - ostroslupa, e - waleca, f - stozka, g - kuli")
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input(" a = ")) 
            print(f"obj szescianu = {a**3}")
        elif inp == "b":
            a = float(input(" a ="))
            b = float(input(" b ="))
            c = float(input(" c ="))
            print(f"obj prostopadloscianu {a} {b} {c} = {a*b*c}")
        elif inp == "c":
            Pp = float(input(" Pp ="))
            h = float(input(" h ="))
            print(f"obj graniastoslupa {Pp} {h} = {Pp*h}")
        elif inp == "d":
            Pp = float(input(" Pp ="))
            h = float(input(" h ="))
            print(f"obj ostroslupa {Pp} {h} = {Pp*h/3}")
        elif inp == "e":
            r = float(input(" r ="))
            h = float(input(" h ="))
            print(f"obj walca {r} {h} = {PI*r**2*h}")
        elif inp == "f":
            r = float(input(" r ="))
            h = float(input(" h ="))
            print(f"obj stozka {r} {h} = {PI*r**2*h/3}")
        elif inp == "g":
            r = float(input(" r ="))
            print(f"obj kuli {r} = {4/3*PI*r**3}")
        else:
            print("nie ma takiej komendy")
    else:
        print("nie ma takiej komendy")
elif inp == "b":
    print("a - obwod, b - pole")
    inp = input(": ").lower().strip()
    if inp == "a":
        print("a - kwadratu, b - prostokata,  c - rownolegloboku, d - trapezu,  e - trojkata, f - trojkata rownobocznego, g - kola, h - rombu")
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input(" a = ")) 
            print(f"obw kwadratu = {4*a}")
        elif inp == "b":
            a = float(input(" a ="))
            b = float(input(" b ="))
            print(f"obw prostokata {a} {b} = {2*a + 2*b}")
        elif inp == "c":
            a = float(input(" a ="))
            b = float(input(" b ="))
            print(f"obw rownolegloboku {a} {b} = {2*a + 2*b}")
        elif inp == "d":
            a = float(input(" a ="))
            b = float(input(" b ="))
            c = float(input(" c ="))
            d = float(input(" d ="))
            print(f"obw trapezu {a} {b} {c} {d} = {a + b + c + d}")
        elif inp == "e":
            a = float(input(" a ="))
            b = float(input(" b ="))
            c = float(input(" c ="))
            print(f"obw trojkata {a} {b} {c} = {a + b + c}")    
        elif inp == "f":
            a = float(input(" a ="))
            print(f"obw trojkata rownobocznego {a} = {3*a}")
        elif inp == "g":
            r = float(input(" r ="))
            print(f"obw kola {r} = {2*PI*r}")
        elif inp == "h":
            a = float(input(" a ="))
            print(f"obw rombu {a} = {4*a}")
        else:
            print("nie ma takiej komendy")
    elif inp == "b":
        print("a - kwadratu, b - prostokata,  c - rownolegloboku, d - trapezu,  e - trojkata, f - trojkata rownobocznego, g - kola, h - rombu")
        inp = input("inp: ").lower().strip()
        if inp == "a":
            a = float(input(" a = ")) 
            print(f"pole kwadratu = {a**2}")
        elif inp == "b":
            a = float(input(" a ="))
            b = float(input(" b ="))
            print(f"pole prostokata {a} {b} = {a*b}")
        elif inp == "c":
            a = float(input(" a ="))
            h = float(input(" h ="))
            print(f"pole rownolegloboku {a} {h} = {a*h}")
        elif inp == "d":
            a = float(input(" a ="))
            b = float(input(" b ="))
            h = float(input(" h ="))
            print(f"pole trapezu {a} {b} {h} = {(a + b)*h/2}")
        elif inp == "e":
            a = float(input(" a ="))
            h = float(input(" h ="))
            print(f"pole trojkata {a} {h} = {a*h/2}")
        elif inp == "f":
            a = float(input(" a ="))
            print(f"pole trojkata rownobocznego {a} = {math.sqrt(3)/4*a**2}")
        elif inp == "g":
            r = float(input(" r ="))
            print(f"pole kola {r} = {PI*r**2}")
        elif inp == "h":
            a = float(input(" a ="))
            h = float(input(" h ="))
            print(f"pole rombu {a} {h} = {a*h}")
        else:
            print("nie ma takiej komendy")
    else:
        print("nie ma takiej komendy")
else:
    print("nie ma takiej komendy")

        
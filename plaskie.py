import math
math.pi

def plaskie()->None:
    while True:
        print("a -- pp fig plaskich")
        print("b -- obw fig plaskich")
        print("e -- Exsit ")
        inp = input().lower().strip()
        if inp == "a":
            jakie_pp() 
        elif inp == "b":
            jakie_obw()
        elif inp == "e":
            print("Exsit")
            break





def pp_kwadratu(a:float)->float:
    return a**2

def pp_porstokata(a:float, b:float)->float:
    return a*b

def pp_rownolegloboku(a:float, h:float)->float:
    return a*h

def pp_trojkata(a:float, h:float)->float:
    return a*h/2

def pp_trapezu(a: float, b:float, h:float)->float:
    return (a+b)*h/2

def pp_kola(r: float)->float:
    return math.pi*r**2

def pp_trrownobocznego(a:float)->float:
    return (math.sqrt(3)/4)*a**2

def pp_romb(a:float, h:float)->float:
    return a*h


def legenda_pp()->None:
    print("a -- pp_kwadratu")
    print("b -- pp_porstokata")
    print("c -- pp_rownolegloboku")
    print("d -- pp_trojkata")
    print("e -- pp_trapezu")
    print('f -- pp_kola')
    print("g -- pp_trrownobocznego")
    print("h -- pp_romb")
    print("m -- Exsit")


def jakie_pp()->None:
    while True:
        legenda_pp()
        inp = input().lower().strip()
        if inp == "m":
            print("Exsit")
            break
        elif inp == "a":
            a = float(input("a = "))
            print(f"dla {a} pp_kwadratu = {pp_kwadratu(a)}")
        elif inp == "b": 
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"dla {a} {b} pp_porstokata = {pp_porstokata(a,b)}")
        elif inp == "c":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"dla {a} {h} pp_rownolegloboku = {pp_rownolegloboku(a,h)}")
        elif inp == "d":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"dla {a} {h} pp_trojkata = {pp_trojkata(a, h)}")
        elif inp == "e":
            a = float(input("a = "))
            b = float(input("b = "))
            h = float(input("h = "))
            print(f"dla {a} {b} {h} pp_trapezu = {pp_trapezu(a, b, h)}")
        elif inp == "f":
            r = float(input("r = "))
            print(f"dla {r} pp_kola = {pp_kola(r)}")
        elif inp == "g":
            a = float(input("a = "))
            print(f"dla {a} pp_trrownobocznego = {pp_trrownobocznego(a)}") 
        elif inp == "h":
            a = float(input("a = "))
            h = float(input("h = "))
            print(f"dla {a} {h} pp_romb = {pp_romb(a, h)}")






            

# -----------------------------------------------------------------------------
def obw_kwadaru(a:float)->float:
    return 4*a

def obw_prostokata(a:float, b:float)->float:
    return 2*a+2*b

def obw_rownolegloboku(a:float, b:float)->float:
    return 2*a+2*b

def obw_trojkata(a:float, b:float, c:float)->float:
    return a+b+c

def obw_trapezu(a:float, b:float, c:float, d:float)->float:
    return a+b+c+d

def obw_kola(r:float)->float:
    return 2*math.pi*r

def obw_trrownobocznego(a:float)->float:
    return 3*a

def obw_romb(a:float)->float:
    return 4*a

def legenda_obw()->None:
    print("a -- obw_kwadaru")
    print("b -- obw_prostokata")
    print("c -- obw_rownolegloboku")
    print("d -- obw_trojkata")
    print("e -- obw_trapezu")
    print("f -- obw_kola")
    print("g -- obw_trrownobocznego")
    print("h -- obw_romb")
    print("m -- Exsit")


def jakie_obw()->None:
    while True:
        legenda_obw()
        inp = input().lower().strip()
        if inp == "m":
            print("Exsit")
            break
        elif inp == "a":
            a = float(input("a = "))
            print(f"dla {a} obw_kwadratu = {obw_kwadaru(a)}")
        elif inp == "b": 
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"dla {a} {b} obw_prostokata = {obw_prostokata(a,b)}")
        elif inp == "c":
            a = float(input("a = "))
            b = float(input("b = "))
            print(f"dla {a} {b} obw_rownolegloboku = {obw_rownolegloboku(a,b)}")
        elif inp == "d":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"dla {a} {b} {c} obw_trojkata = {obw_trojkata(a, b, c)}")
        elif inp == "e":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            d = float(input("d = "))
            print(f"dla {a} {b} {c} {d} obw_trapezu = {obw_trapezu(a, b, c, d)}")
        elif inp == "f":
            r = float(input("r = "))
            print(f"dla {r} obw_kola = {obw_kola(r)}")
        elif inp == "g":
            a = float(input("a = "))
            print(f"dla {a} obw_trrownobocznego = {obw_trrownobocznego(a)}")
        elif inp == "h":
            a = float(input("a = "))
            print(f"dla {a} obw_romb= {obw_romb(a)}")

# -------------------------------------------------------------------------------


plaskie()

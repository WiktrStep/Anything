from time import time


x = ["a", "b", "c"]

i = 0 
while i < len(x):
    time.sleep(1)
    print (f"{i} ----- {x[i]}")
    i += 1


print("=================================")


i = 0
while i != len(x):
    time.sleep(1)
    print (f"{i} ----- {x[i]}")
    i += 1


print("=================================")


for el in x:
    print(el)

for i in range(len(x)):
    print(f"{i} ----- {x[i]}")

for i, v in enumerate(x):
    print(f"{i} ----- {v}")


print("=================================")


x.append("6")
x.append("6")
x.append("6")
print(x)

x = []
for _ in range(3):
    x.append("6")
print(x)

x = []
for i in range(3):
    x.append(i)
print(x)


for i in range(100):
    if i % 2 == 0:
        print(i)


x = []
i = 0
while i < 10:   
    x.append(2**i)
    i += 1

x = []
i = 0
while i != 10:
    x.append(2**i)
    i += 1

for i in range(10):
    x.append(2**i)
print(x)




x = 10
y = x
y -= 10
print(x)
print(y)


x = [[]]
y = x.copy
y.append(67)
y[0].append(67)
print(x)
print(y)


x = []
y = x
y.append(67)
print(x)
print(y)




from copy import deepcopy
x = [[]]
y = deepcopy(x)
y.append(67)
y[0].append(67)
print(x)
print(y)




x = [1, 2, 3, "a", 23.3232, True, False, None]
x.copy()
y = [[], {}, ()]
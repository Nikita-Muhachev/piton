import math
x = float(input("x="))
y = float(input("y="))
if ( math.sqrt(x * x + y * y) <= 1 and ((x + 2) ** 2 + y * y) <= 2):
    print("точка входит в закрашенную область")
else:
    print("точка не входит в закрашенную область")

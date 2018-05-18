import math
r = float(input("r="))
R = float(input("R="))
x = float(input("x="))
y = float(input("y="))
if (math.sqrt(x * x + y * y) > r and math.sqrt(x * x + y * y) < R):
    print("точка входит в закрашенную область")
else:
    print("точка не входит в закрашенную область")

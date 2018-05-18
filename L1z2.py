import math
t=float(input("t="))
r=float(input("r="))
y=float(input("y="))
w=((4*t**3)+math.log(r,math.e))/(math.e**(y+r)+7.2*math.sin(r))
print(w)
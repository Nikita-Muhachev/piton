import math
c=9
x=float(input("x="))
b=x+c*c
a=(abs(b+c))**(1/3)
y=math.cos(b)**2+b*math.cos(a*a)**4
print("b=",b," a=",a," y=",y)

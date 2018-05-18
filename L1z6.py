import math
i = 1
while i == 1:
    A = int(input("введите сторону A: "))
    B = int(input("введите сторону B: "))
    C = int(input("введите сторону C: "))
    if A + B >= C and A + C >= B and B + C >= A:
         i = 0
    else:
        print("триугольника с такими сторонами не существует, попробуйте ещё раз")
MEDIAN_A = 0.5*math.sqrt((2*B)**2+(2*C)**2-A**2)
MEDIAN_B = 0.5*math.sqrt((2*A)**2+(2*C)**2-B**2)
MEDIAN_C = 0.5*math.sqrt((2*C)**2+(2*C)**2-C**2)
print("MEDIANA_A =", MEDIAN_A," MEDIANA_B =",MEDIAN_B," MEDIANA_C = ",MEDIAN_C)

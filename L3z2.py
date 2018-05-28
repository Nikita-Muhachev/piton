import math
k = int(input("k="))
p = 1
for n in range(-3,k):
    p = p * ((n + 2) * abs(n - 4) / math.factorial(n + 3))
print(p)
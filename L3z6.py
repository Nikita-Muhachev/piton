import math
n=int(input("n="))
s=0
for i in range(0,n):
    s=s+math.sin(2*i+1)/2*i+1
print(s)
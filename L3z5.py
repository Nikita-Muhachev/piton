f1=0
f2=1
for i in range (0,18):
    f0=f1
    f1=f1+f2
    f2=f0
print(f1)
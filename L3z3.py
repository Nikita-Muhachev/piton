p=int(input("p="))
q=int(input("q="))
pp= []
qp=[]
for i in range(1, p):
    if p % i == 0:
        k = 0
        for j in range(2, i):
            if i % j == 0:
              k = k + 1
    if k==0:
        pp.append(i)
        k=1
for i in range(1, q):
    if p % i == 0:
        k = 0
        for j in range(2, i):
            if i % j == 0:
              k = k + 1
    if k==0:
        qp.append(i)
        k=1
for i in range(1,len(pp)):
    for j in range(1, len(qp)):
        if pp[i]==qp[j]:
            print(pp[i])

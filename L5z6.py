mas={}
n=int(input("n="))
for i in range(0,n):
    for j in range(0,n):
       print("введите ",i+1," эллимент",j+1," строки")
       mas[i,j]=int(input())
k=0
for i in range(0,n):
    for j in range(0,n):
        if i!=j:
            if mas[i,j]==mas[j,i]:
               k+=1
if k==n*(n-1):
    print("массив симметричный")
else:
    print("массив не симметричный")
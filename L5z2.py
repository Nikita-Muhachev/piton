mas=[]
for i in range(0,9):
    print("введите ",i+1," эллимент")
    m=int(input())
    mas.append(m)
print(mas)
i=0
sum=0
while mas[i]>=0:
 sum+=mas[i]
 i+=1
print("sum=",sum," kol elementov =",i)
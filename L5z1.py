mas=[]
for i in range(0,19):
    print("введите ",i+1," эллимент")
    m=float(input())
    mas.append(m)
print(mas)
for i in range (0,len(mas)):
      if mas[i]==min(mas):
         a=i
      if mas[i] == max(mas):
         b=i
print(abs(a-b)-1)

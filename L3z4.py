n = 0
while (n >1000 or n<1):
   n = int(input("введите n от 1 до 1000 "))
   if n >1000 or n<1:
       print("ошибка ввода")
m = int(input("m="))
print((n//m)**2)

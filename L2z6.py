n = 1
while n == 1:
    a = input("введите четырёхзначное число: ")
    if len(a) == 4 and a.isdigit(): #проверка на число
        n = 0
    else:
        print("не коректный ввод")
print("a) = " , (int(a[1]) + int(a[0]) == int(a[2]) + int(a[3])) , "\n\rb) = " , (int(a[1]) + int(a[0]) + int(a[2]) + int(a[3])) % 7 == 0)

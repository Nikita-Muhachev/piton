x = int(input("x="))
y = int(input("y="))
z = int(input("z="))
print(((x % 5 == 0) and not(y % 5 == 0) and not(z % 5 == 0))or(not(x % 5 == 0) and (y % 5 == 0) and not(z % 5 == 0) or(not(x % 5 == 0) and not(y % 5 == 0) and (z % 5 == 0))))


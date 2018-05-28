mas = [10101010, 101010, 101010101, 101010, 1001]
print(mas)
for i in range(0, len(mas)):
    if mas[i] == max(mas):
        ma = i
    if mas[i] == min(mas):
        mi = i
mas[ma], mas[mi] = mas[mi], mas[ma]
print(mas)
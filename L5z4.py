mas = [[1, 3, 5, 5, 3],
      [1, 6, 1, 5, 6],
      [6, 5, 1, 6, 5],
      [1, 3, 2, 1, 3],
      [6, 1, 1, 3, 5]]
pr = 1
for i in range(0, len(mas)):
    pr *= mas[0][i]
print(pr)
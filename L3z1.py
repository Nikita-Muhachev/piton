N = 0
while (N <= 2):
  N = int(input("введите N>2 "))
  if N <= 2:
      print("ошибка ввода ")
B = 0
A = 0
while B <= A:
  A = float(input("введите А "))
  B = float(input("введите B >A "))
  if B <= A:
      print("ошибка ввода")
print((B - A) / N)

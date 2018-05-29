class IlovePyton(object):
    def __init__(self,a,x,y):
        self.a = a
        self.x = x
        self.y = y
class doljn(IlovePyton):
    def __init__(self, x,z):
        self().__init__(x)
        self.z=z
    def bolshe(self):
        if self.z=="программист" or self.z=="Программист":
            return self.x*1.2
        else: return "не программист"

a = input("введите имя: ")
x = int(input("Введите оклад: "))
y = int(input("Введите год рождения: "))
z = input("введите должность: ")

cab=doljn(x,z)
cub = IlovePyton(a,x,y)
print(cab.bolshe())
class IlovePyton(object):
    def __init__(self,a,x,y,z):
        self.a = a
        self.x = x
        self.y = y
        self.z = z
class doljn(IlovePyton):
    def bolshe(self):
        if self.z=="программист" or self.z=="Программист":
            return self.x*1.2
        else: return self.x

a = input("введите имя: ")
x = float(input("Введите оклад (руб): "))
y = int(input("Введите год рождения: "))
z = input("введите должность: ")

cub = IlovePyton(a,x,y,z)
cab=doljn
print("оклад на должности ",z," составляет ",cab.bolshe(cub)," руб")

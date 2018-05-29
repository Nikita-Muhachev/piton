class IlovePyton(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
class class2(IlovePyton):
    def jopa(self):
        if x<y:
            return x*z
        else:
            return y*z

z = float(input("Введите z: "))
x = int(input("Введите x: "))
y = int(input("Введите y: "))

cub = IlovePyton(x,y,z)
cab=class2
print(cab.jopa(cub))
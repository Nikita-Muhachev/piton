class IlovePyton(object):
    """Class"""
    def __init__(self, x,y):
        """Constructor"""
        self.x = x
        self.y = y
    def poschetat(self):
        if (self.x > self.y):
            return self.y**2
        else:
            return self.x**2

x = int(input("Введите X: "))
y = int(input("Введите Y: "))


cub = IlovePyton(x,y)

print(cub.poschetat())
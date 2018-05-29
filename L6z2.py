class IlovePyton(object):
    def __init__(self,a,x,y):
        self.a = a
        self.x = x
        self.y = y
    def poschetat(self):
        return 2018-self.y
    def ostalos(self):
        if 2018-self.y>=50:
            return "0"
        else:
            return (50-2018-self.y)*365
a = input("введите имя: ")
x = int(input("Введите оклад: "))
y = int(input("Введите год рождения: "))

cub = IlovePyton(a,x,y)
print("вам ",cub.poschetat()," лет    осталось жить ",cub.ostalos()," дней")
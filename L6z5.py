class Q(object):
    def __init__(self,naz,chis,gol):
        self.naz = naz
        self.chis = chis
        self.gol = gol
    def Q_resh(self):
        return chis*0.3+gol*0.7
class Qp(object):
    def __init__(self,P):
        self.P=P
    def Qp_resh(self):
        if self.P<=Q1:
            return Q1*1.2
        else: return Q1*0.8

naz = input("введите название партии: ")
chis = int(input("Введите численность партии: "))
gol = float(input("Введите процент голосов на последних выборах: "))
Q1=Q(naz,chis,gol).Q_resh()
print("качество Q = ",Q1)

P = int(input("Введите колличество члнов партии в прошлом году: "))
Q2=Qp(P).Qp_resh()
print("качество Qp = ",Q2)




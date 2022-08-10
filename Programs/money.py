'''
Create a Money class and initialize it with rupees and paise.
1. Make a method addMoney which should take two money object and add them. 
   E.g.- (2 rupees and 50 paise)+(3 rupees and 70 paise) is (6 rupees and 20 paise)
2. Make a method displayMoney which should print the money.
3. Make a method displayRupees which should display the total rupees in the mpney. 
'''

class Money():
    def __init__(self,rupees,paise):
        self.rupees = rupees
        self.paise = paise

    def addTime(m1,m2):
        m3 = Money(0,0)
        if m1.paise + m2.paise > 100 :
           m3.rupees = (m1.paise + m2.paise)// 100
        m3.rupees = m1.rupees + m2.rupees + m3.rupees
        m3.paise = (m1.paise + m2.paise) -(((m1.paise + m2.paise)//100)*100)
        return m3

    def displayMoney(self):
       print("Money =",self.rupees,"Rupees and",self.paise,"Paise")
      
    def displayRupees(self):
       print("Rupees =",self.rupees)

    def displayPaise(self):
       print("Paise =",self.paise)

a = Money(2,60)
b = Money(3,60)
m = Money.addTime(a,b)
m.displayMoney()
m.displayRupees()
m.displayPaise()
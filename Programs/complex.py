# Add two complex numbers

class Complex():
    def __init__(self,real,img):
        self.real = real
        self.img = img
    
    def addNumbers(c1,c2):
        c3 = Complex(0,0)
        c3.real = c1.real + c2.real
        c3.img = c1.img + c2.img
        return c3

    def display(self):
        print("Addition of two Complex numbers = ",self.real,"+",self.img,"i")

c1 = Complex(5,10)
c2 = Complex(4,5)
c = Complex.addNumbers(c1,c2)
c.display()
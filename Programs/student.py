class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def setAge(self,age):
        self.age = age

    def setMarks(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    def getDetails(self):
        print("Student Details : " , self.name ,self.id , self.age, self.m1 , self.m2 , self.m3)

S= Student("Rishi", 101)
S.setAge(24)
S.setMarks(90,80,95)
S.getDetails()
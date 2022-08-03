class Student():
    def __init__(self,sname,sid,sage):
        self.sname=sname
        self.sage=sage
        self.sid = sid
class Marks():
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

class Result(Student,Marks):
    def __init__(self,sname,sid,sage,m1,m2,m3):
        Student.__init__(self,sname,sid,sage)
        Marks.__init__(self,m1,m2,m3)

    def percentage(self):
        per = (self.m1+self.m2+self.m3)/3

        if (per >= 90):
            print("Name : ",self.sname, "\nAge : ",self.sage, "\nId : ",self.sid,"\nGrade A")
        elif (per>= 80 and per< 90):
            print("Name : ",self.sname, "\nAge : ",self.sage, "\nSales : ",self.sid,"\nGrade B")
        else:
            print("Name : ",self.sname, "\nAge : ",self.sage, "\nSales : ",self.sid,"\nGrade C")

obj=Result("Rishi",101,23,95,35,95)
obj.percentage()

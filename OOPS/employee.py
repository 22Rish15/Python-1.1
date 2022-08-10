class Employee:
    def __init__(self,name,age,id,sal):
        self.ename=name
        self.eage=age
        self.eid=id
        self.esal=sal
    
    def display(self):
        print(self.ename,self.eage,self.eid,self.esal)


for i in range(2):
    name = input()
    age = int(input())
    id = int(input())
    sal = int(input())
    emp = Employee(name,age,id,sal)
    emp.display()
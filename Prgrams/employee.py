class employee():
    def __init__(self,name,age):
        self.name=name
        self.age=age

class sale():
    def __init__(self,sales):
        self.sales=sales

class total_salary(sale,employee):
    def __init__(self,name,age,sales,salary):
        employee.__init__(self,name,age)
        sale.__init__(self,sales)
        self.salary=salary

    def show(self):
        if (self.sales > 10000):
            com = self.sales * 0.05
            print("Name : ",self.name, "\nAge : ",self.age, "\nSales : ",self.sales,"\nSalary : ",com + self.salary)
        elif (self.sales > 5000 & self.sales < 9999):
            com = self.sales * 0.03
            print("Name : ",self.name, "\nAge : ",self.age, "\nSales : ",self.sales,"\nSalary : ",com + self.salary)
        else:
            com = self.sales * 0.02
            print("Name : ",self.name, "\nAge : ",self.age, "\nSales : ",self.sales,"\nSalary : ",com + self.salary)

obj=total_salary("Rishi",23,60000,10000)
obj.show()

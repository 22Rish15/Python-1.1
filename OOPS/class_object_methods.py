class Student:
    def getData(self):
        self.sname = input()
        self.sid = int(input())
        self.sage = input()

    def putData(self):
        print(self.sname,self.sid)

S = Student()
S.getData()
S.putData()

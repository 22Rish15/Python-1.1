class Human:
    s1 = 'human'

    def __init__(self,name,age):
        self.name = name
        self.age = age

Rishi = Human('Rishi',24)
Shivani = Human('Shivani',23)

print("Rishi is a {}".format(Rishi.__class__.s1))
print("Shivani is also a {}".format(Shivani.__class__.s1))

print("{} is {} years old".format(Rishi.name,Rishi.age))
print("{} is {} years old".format(Shivani.name,Shivani.age))
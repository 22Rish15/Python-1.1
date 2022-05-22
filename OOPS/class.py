from traceback import print_tb


class Person:
    'This is a person class'
    age = 18

    def greet(self):
        print("Hello")

harry = Person()

print(Person.greet)

print(harry.greet)

harry.greet()
print(Person)
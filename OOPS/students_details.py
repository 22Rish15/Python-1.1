# Python code to demonstrate how parent constructors are called.

# parent class
class Student:

		# __init__ is known as the constructor		
		def __init__(self, name, id):
				self.name = name
				self.id = id
		def display(self):
				print(self.name)
				print(self.id)

# child class
class Details( Student ):		
		def __init__(self, name , id, course, year):	
				self.course = course
				self.year = year
				print(course,"\n",year)
				# invoking the __init__ of the parent class
				Student.__init__(self, name, id)
				
a = Details("Rishi", 101,"MCA", 2021)
a.display()
class Student:

    #default constructors
    def __init__(self):
        
        pass

    #parameterized cnstructor
    def __init__(self,name, marks): #argument
       self.name = name
       self.marks = marks
       print(self)
       print("adding new student in database..")

s1 = Student("Supriya Kumari",97)
print(s1.name,s1.marks)

s2 = Student()
print(s2.name)

class Car:
    color = "blue"
    brand = "mercedes"
car1 = Car()
print(car1.color)
print(car1.brand )
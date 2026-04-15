# python Object_oriented Programming

class Employee:
 
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

         #method fullname
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Supriya','Kumari',70000) #instances of class

emp_2 = Employee('Sanoj','Kumar',80000)

# print(emp_1)
# print(emp_2) 

# emp_1.first = 'Supriya'
# emp_1.last = 'Kumari'
# emp_1.email = 'Supriya@kumari.com'
# emp_1.pay = 50000

# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@kumari.com'
# emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

print(Employee.fullname(emp_1))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.__dict__)
print(Employee.__dict__)
#class Variables

Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_1.raise_amount)

emp_1.raise_amount = 1.06
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps) 
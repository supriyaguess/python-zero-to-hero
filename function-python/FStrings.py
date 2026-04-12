# Person = {'name': 'Supriya','age':23}
# sentence = 'My name is {0} and I am {1} years old.'.format(Person['name'],Person['age'])
# print(sentence)

# sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(Person)
# print(sentence)

# tag = 'h1'
# text = 'This is a headline'

# sentence ='<{0}>{1}</{0}>'.format(tag,text)
# # print(sentence)


# class person():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# P1 = person('Jack','33')

# sentence = 'My name is {name} and I am {0.}'


#  What is an f-string?

# f-string = formatted string (Python 3.6+)

#  It lets you insert variables inside a string easily.

name = "Sanoj"
print(f"My name is {name}") # clean + readable

# Why use f-string
# Old ways 

print("My name is " + name)
print("My name is {}".format(name))

# Basic Syntax
# f"some text {variable}" #

#4. Multiple Variables
name = "Sanoj"
age = 22

print(f"My name is {name} and I am {age} years old")

# Expressions inside f-string 🔥

#You can do calculations inside {}

a = 5
b = 10

print(f"Sum is {a + b}")

#6. Functions inside f-string
def square(n):
    return n * n

print(f"Square is {square(4)}")

#7. Formatting numbers
#Float formatting
pi = 3.14159
print(f"Value of pi: {pi:.2f}")

#Padding / width
num = 7
print(f"{num:05}")

#8. Align text
text = "Hi"

print(f"{text:<10}")  # left
print(f"{text:>10}")  # right
print(f"{text:^10}")  # center

#9. Debugging trick (VERY IMPORTANT )
x = 10
print(f"{x=}")

#10. Using quotes inside f-string
name = "Sanoj"
print(f'My name is "{name}"')
#11. Multiline f-string
name = "Sanoj"
age = 22

print(f"""
Name: {name}
Age: {age}
""")

#12. Escape curly braces
print(f"{{Hello}}")

for i in range(1,11):
    sentance = 'The value is {}' .format(i)
    print(sentance)
for i in range(1,11):
    sentance = 'The value is {:02}' .format(i)
    print(sentance)

pi = 3.14159265
sentance = 'Pi is equal to {:.3f}'.format(pi)
print(sentance)

sentance = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentance)

import datetime
my_date = datetime.datetime(2026,9,24,12,30,45)

sentance = '{:%B %d %Y}'.format(my_date)
print(sentance)

#March 01, 2026

# MARCH 01, 2026 fell on a {} and was the 061 day of the year.

sentance = '{0:%B %d %Y} fell on a {0:%A} and was the {0:%j} day of the year '.format(my_date)
print(sentance)
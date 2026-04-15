# namedtuple is a lightweight onject that works like a normal tuple 
# but it is more readable 

from collections import namedtuple
color = namedtuple('color', ['red', 'green', 'blue'])
# tuple is unchangeable
Color = color(55, 155, 255)
print(Color.red)

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
p.x        # 10
p.y        # 20
p[0]       # 10 (index access)
print(p._asdict())
p2 = p._replace(x=100)
print(p2)
print(Point._fields) #Get field names

#Create from iterable
p = Point._make([10, 20])
print(p)

#Default values (advanced)
Point = namedtuple('Point', ['x', 'y'], defaults=[0, 0])

p = Point()
print(p)
# Point(x=0, y=0)

#Rename invalid fields
Point = namedtuple('Point', ['x', 'class'], rename=True)
# becomes ('x', '_1')

print(tuple(p))

#14. Check type
print(isinstance(p, tuple))  # True
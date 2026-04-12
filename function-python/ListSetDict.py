num = [1,2,3,4,5,6,7,8,9,10]

# I want 'n for each 'n in nums
my_list = []
for n in num:
   my_list.append(n)
print(my_list)

my_list = [n for n in num ]
print(my_list)

#I want 'n*n' for each 'n' in nums
my_list = []
for n in num:
   my_list.append(n*n)
print(my_list)
my_list = [n*n for n in num]
print(my_list)

# Using a map + lambda
my_list =  map(lambda n: n*n, num) #map() Applies function to each element of list map(func, list)
print(my_list) # lambda n: n*n → takes n, returns square. (simple function)

# I want 'n for each 'n' in nums if 'n' is even
my_list = []
for n in num:
   if n%2 == 0:
      my_list.append(n)
print(my_list)

my_list = [n for n in num if n%2 == 0]
print(my_list)
 
#Using a filter + lambda
my_list = filter(lambda n: n%2 == 0, num)
print(my_list)

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
   for num in range(4):
      my_list.append((letter,num))
print(my_list)

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

#DICTIONARY Comprehensions
names = ['Bruce','Clark','Peter','Logan','Wade']
heros = ['batman','Superman','Spiderman','Wolverine','Deadpool']


#I want a dict{'name':'name'} for each name , hero in zip(names,heroes)
my_dict = {}
for name, hero in zip(names,heros):
   my_dict[name] = hero
print(my_dict)
my_dict = {name: hero for name, hero in zip(names,heros) if name != 'Peter'}
print(my_dict)

#SET Comprehensions
nums = [1,1,2,1,3,4,3,5,5,6,7,8,7,9,9]

my_set = set()
for n in nums:
   my_set.add(n)
print(my_set)
my_set = {n for n in nums}
print(my_set)

# Generator Expressions

# I want to yield 'n*n' for each 'n' in nums 
numR = [1,2,3,4,5,6,7,8,9,10]

def gen_func(numR):
   for n in nums:
      yield n*n

      my_gen = (n*n for n in nums)

my_gen = gen_func(numR)

for i in my_gen:
   print(i)

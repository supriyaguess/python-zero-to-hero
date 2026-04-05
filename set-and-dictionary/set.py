collection = {1,2,2,2,"hello","world","world",4}

print(collection)
print(len(collection)) # total number of items

#empty Set
empty_set = set() #empt set ; syntax 
print(type(empty_set))
empty_set.add(1)
empty_set.add(2)
empty_set.add(5)
empty_set.add(2)
print(empty_set.pop())
empty_set.remove(2)
empty_set.add((1,2,3)) #tuple

print(empty_set)
empty_set.clear()
print(len(empty_set))
#empty_set.remove(7) #gives error
#empty_set.add([1,2,3]) #tuple ->error

set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2)) #{1,2,3,4}
print(set1.intersection(set2)) # {2,3} 
print(set1)
print(set2)
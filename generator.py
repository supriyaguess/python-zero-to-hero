#A generator is a function that yields values one by one instead of returning all at once
# def square_numbers(nums):
#     result = []
#     for i in nums:
#        result.append(i*i) #this is a normal function (list-based)
#     return result

# my_nums = square_numbers([1,2,3,4,5])
# print(my_nums). 

#Creates a list Stores all values in memory Returns [1, 4, 9, 16, 25]

def square_numbers(nums):
    for i in nums:
       yield (i*i)
    
my_nums = square_numbers([1,2,3,4,5])
print(my_nums)
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))



for num in my_nums:
    print(num)
g  = (x*x for x in range(5))

for i in g:
    print(i)

Nums = (X*X for X in [1,2,3,4,5])

print(list(Nums))

for num in Nums:
   print(num)
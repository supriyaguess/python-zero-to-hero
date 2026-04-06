# #print from 100 to 1
# i = 1
# while i <= 100:
#     print(i)
#     i += 1


#print from 100 to 1
# i = 100
# while i >= 1:
#     print(i)
#     i -= 1


# table of any numver that user will give
# n = int(input("enter number : "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1

# square of any number
# i = 1
# while i <= 10:
#     print(i*i)
#     i += 1

nums = [1,4,9,16,25,36,49,64,81,100]
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4]) #... print(nums[len(nums)])
i = 0
while i < len(nums):
    print(nums[i])
    i += 1

tup = (1,4,16,25,36,49,64,81,100)
x  = 36

i = 0
while i < len(tup):
    if(tup[i] == x):
        print("Found at index" , i)
        break
    else:
        print("finding...")
    i += 1

print("end of loop")

s = 0
while s <= 5:
    if(s == 3):
        s += 1
        continue
    print(s)
    s += 1

x = 1
while x <= 10:
    if(x%2 == 0):
        x += 1
        continue #skip
    print(x)
    x += 1

#factorial of first n numbers
n = 5
fact = 0
while i <= n:
    fact *= i
    i += 1

print("total sum =", fact)
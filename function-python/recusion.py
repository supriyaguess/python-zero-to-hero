def show(a):
    if(a == 0):
        return
    print(a)
    show(a-1)
show(5) #Recursive function

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n*fact(n-1)
    
print(fact(7))

# def sum_cal(x):
#     if(x == 0):
#         return
#     print(x)
#     sum_cal(x-1) + sum_cal(x)

# sum_cal(5)

f = open("demo.txt","a+")
# data = f.read(5)
# print(data)  
# print(type(data))
# line1 = f.readline()
# print(line1)

f.write("\n I will move to reactjs. 123")
f.close()
file = open("sample.txt", "w")
f.close( )
with open("demo.txt","r") as f:
    data =  f.read()
    print(data)

    with open("demo.txt","w") as f:
        f.write("new data")

import os
os.remove("sample.txt")
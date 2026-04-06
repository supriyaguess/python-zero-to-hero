vaggies = ["potato", "brinjal","ladyfinger","cucumber"]

for val in vaggies:
    print(val) 
tup = (1,2,3,4,2,8,9)
for num in tup:
    print(num)

str = "SupriyaKumari"
  
for char in str:
    if(char == 'a'):
        break
    print(char)
else:
    print("END")
list = (1,4,9,16,25,36,49,64,81,100,49)
x= 49

idx = 0
for el in list:
    if(el == x):
       print("number found at idx",idx)
       break 
    idx += 1
    

    #range start from 0 by default and increment by 1 by default


seq = print(range(5))


for i in range(10): #rnge(stop)
    print(i)

for i in range(2,10): #rnge(start,stop)
    print(i)
for i in range(2,10,2): #rnge(start,stop,step)
    print(i)

for i in range(2,101,2):
    print(i)
for i in range(1,101,2):
    print(i)

#practice Questions
#Q1 Print numbers from 1 to 100
for i in range(100):
    print(i) 

#Q2 Print numbers from 100 to 1
for i in range(100,1,-1):
    print(i)

#Q3 print multiplication table of n
n = int(input("enter number : "))

for i in range(1,11):
    print(n*i)

    for i in range(5):
        pass

if i > 5:
    pass # will do some useful work in future 

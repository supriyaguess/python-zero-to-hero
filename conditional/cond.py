# age = 21
# if(True):
#     print("can vote")
#     print("can drive")

# light = "green"

# if(light == "red"):
#     print("stop")
# elif(light == "green"):
#     print("go")
# elif(light == "yellow"):
#     print("look")

# print("end of code")

# num = 5

# if(num > 2):
#     print("greater than 2")

marks = int(input("enter students marks : "))

if(marks >= 90):
       grade = "A"
elif(marks >= 80 and marks < 90):
       grade = "B"
elif(marks >= 70 and marks <80):
       grade = "C"
else:
       grade = "D"
print("grade of the student ->", grade)
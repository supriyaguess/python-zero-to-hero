info = {
    "key" : "value",
    "subjects" : ["python","C","Java"],
    "topics" : ("dict","set"),
    "name" : "supriya",
    "learning": "coding",
    "is_adult" : True,
    "marks" : 94.4
}

print(type(info))
print(info["is_adult"]) #this is how i can get value of any key 
info["name"] = "Sanoj"
info["surname"] = "Pandit"
print(info)

null_dict = {}
null_dict["name"] = "SupriyaKumari"
print(null_dict) 

#nested Dictionary
student  = {
    "name" : "priyanka chopra",
    "subjects" : {
        "phy" :97, 
        "chem" : 98,
        "math" : 95
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])

print(student.keys())
print(list(student.keys()))
print(len(list(student.keys())))
print(list(info.values())) 
pairs = list(student.items())
print(pairs[0])

student.update({"city" : "delhi"}) # can put multiple key values
print(student)
print("BEFORE")
#print(student["name2"]) #if we write wrong key the itll return error whih may cause futher cide give error 
print("AFTER")
print(student.get("name")) # but   it not return any error --> None but itll not stop whole code just that line reprenst None

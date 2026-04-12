#create a new file "practice.txt" using python.add the following data in it
#Hii everyone 
#we are learning filr I/O
#using java
#i like programming in JAVA
# with open("practice.txt","w") as f:
#     f.write("Hii everyone\n we are learning file  I/O")
#     f.write("using java\n i like programming in JAVA")


# WAF that replace all occurances of "JAVA" with "python" in above file.

with open("practice.txt","r") as f:
    data = f.read()
    new_data = data.replace("Java","Python")
    print(new_data)

    with open("practice.txt", "w") as f:
        f.write(new_data)

        #     Search if the word "learning" exists in file or not
def check_word():
    word = "learning "
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else: 
        print("not found")

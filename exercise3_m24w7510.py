f_read = open("student.txt","r")
print("Original students:")
print(f_read.read())

f=open("student.txt","a")
std_name = ""
print("Please enter the student name to append student.txt file and you can input the value q to quit the program!\n")
while std_name != "q":
    std_name = input("Enter the name: ")    
    if std_name != "q": f.write(f"student name: {std_name}\n")
    else: break
    
f.close()
f_read=open("student.txt","r")
print("Updated students:")
print(f_read.read())

input_file = input("Enter file name to save 5 students name: ")
counter = 1
student_name={}
while counter <= 5:
    student_name[counter]=input("Enter the student Name:")
    counter+=1
f = open(input_file,"w")
for k,v in student_name.items():
    print("student name:",v)
    f.write(f"student name: {v}\n")
f.close()
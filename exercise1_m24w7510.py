import os
class Student():
    def __init__(self,name):
        self.name = name
    def __str__(self):
        f"[{self.name}]"

def wirte_file(input_file,student_name):
    with open(input_file, "w") as file:
        for student in student_name.value():
                file.write(f"{student}:\n")
        else:
                file.write(f"Error!\n")
        print(f"\nGenerated the statistics file with name : {input_file}")

def main():
    input_file = input("Enter file name to save 5 students name: ")
    counter = 1
    student_name={}
    while counter <= 5:
        student_name=input("Enter the student Name:")
        counter+=1

    print(student_name.values())    
    #wirte_file(input_file,student_name)


#if __name__ =="__main__":
main()
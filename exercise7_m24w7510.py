class student():
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def __str__(self):
        return f'[{self.name},{self.grade}]'
def f_write(students,file):
    #file="grades.txt"
    f_w= open(file,"w")    
    for w in students.values():
        f_w.write(f"Name: {w.name}, Grade: {w.grade}\n")

def main():
    students={}
    counter = 1
    flag ="y"
    while flag != "n":
        input_stdname = input("Enter Student Name:")
        input_stdgrade = input("Enter Student Grade:")
        students[counter]=student(input_stdname,input_stdgrade)
        counter +=1
        flag=input("Do you want to add more data?(y/n)")
    for v in students.values():
        print("Name: ",v.name,",Grade: ",v.grade)       
    f_write(students,"grades.txt")

main()

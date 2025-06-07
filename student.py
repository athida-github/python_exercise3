# Student Class initializing the student info attributes and string format to return
class student():
    def __init__(self,student_id, first_name, last_name):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"[{self.student_id},{self.first_name},{self.last_name}]"
    
# Creating a Dictionary to Store Students
students ={}

# implementing the functions

def add_student():
    std_id = input("Enter Student Id: ")
    if std_id in students:
       print ("Your input student id is already exit and please another else!")
       #std_id = input("Enter Student Id: ")
    else:
       f_name = input("First Name: ")
       l_name = input("Last Name: ")
       new_std = student(std_id,f_name,l_name)
       students[std_id]=new_std
    print(new_std.first_name,new_std.last_name,"has been added to the student list!")

def list_student():
   for x in students.values():
      print (x.first_name)

def remove_student(std_id):   
   if std_id in students:
      students.pop(std_id)
   else: print("This student id: ",std_id,"is not existing in the list!")
   print("Id ",std_id,"removed from the list!")
        

      
def main():
    print("Manage Student List Program\n")
    print("===========================\n")
    
    print("'add' - Create a new student")
    print("'remove' - Removes a student by id")
    print("'list' - List all students")
    print("'exit' - Quits the application")
    keyword_opt = input("Input the operation keyword from the following menu iteams:")

    while keyword_opt is not 'exit':
        if keyword_opt == 'add':
            add_student()
        elif keyword_opt == 'remove':
            std_id = input("Input the student that want to remove from the list: ")
            remove_student()
        elif keyword_opt == 'list':
            list_student()
    keyword_opt = input("Input the operation keyword from the following menu iteams:")   
       

if __name__ == "__main__":
 main()

# Student Class initializing the student info attributes and string format to return
class Student:
    def __init__(self, student_id, first_name, last_name):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"[{self.student_id}, {self.first_name}, {self.last_name}]"

# Creating a Dictionary to Store Students
students = {}

# Functions
def add_student():
    std_id = input("Enter Student ID: ")
    if std_id in students:
        print("The student ID already exists. Please enter another!")
    else:
        f_name = input("First Name: ")
        l_name = input("Last Name: ")
        new_std = Student(std_id, f_name, l_name)
        students[std_id] = new_std
        print(f"{new_std.first_name} {new_std.last_name} has been added to the student list!")

def list_students():
    if students:
        print("\nCurrent Students:")
        for student in students.values():
            print("Student_id:",student.student_id,",Name: ",student.first_name,student.last_name)
    else:
        print("\nNo students in the list.")

def remove_student(std_id):
    if std_id in students:
        removed_student = students.pop(std_id)
        print(f"{removed_student.first_name} {removed_student.last_name} (ID: {std_id}) has been removed from the list.")
    else:
        print(f"Student ID {std_id} does not exist in the list!")

def main():
    print("Student Management Program")
    print("===========================")
    
    menu = """
'add' - Create a new student
'remove' - Remove a student by ID
'list' - List all students
'exit' - Quit the application
"""
    print(menu)
    
    while True:
        keyword_opt = input("\nEnter an operation keyword: ").strip().lower()
        
        if keyword_opt == 'add':
            add_student()
        elif keyword_opt == 'remove':
            std_id = input("Enter the student ID to remove: ")
            remove_student(std_id)
        elif keyword_opt == 'list':
            list_students()
        elif keyword_opt == 'exit':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again!")
            print(menu)

if __name__ == "__main__":
    main()

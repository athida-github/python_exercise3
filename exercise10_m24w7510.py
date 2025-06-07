class Task:
    def __init__(self):
        self.task_dec = [] 

    def __str__(self):
        return f"[{', '.join(self.task_dec)}]"

    def add_task(self, task):
        self.task_dec.append(task)
        print(f"Task added: {task}")

    def view_tasks(self):
        idx=1
        if not self.task_dec:
            print("No tasks to display.")
        else:
            print("\nTo-Do List:")
            for task in self.task_dec:
                print(f"{idx}. {task}")
                idx+=1

    def save_to_file(self, file="todo.txt"):
        with open(file, "w") as f_write:
            for task in self.task_dec:
                f_write.write(task + "\n")
        print(f"Tasks saved to {file}.")

    def load_tasks(self, file="todo.txt"):
        try:
            with open(file, "r") as f_read:
                self.task_dec = [line.strip() for line in f_read]
            print(f"Tasks loaded from {file}.")
        except FileNotFoundError:
            print(f"{file} not found. No tasks loaded.")


def main():
    task_manager = Task()
    print("To-Do List Application")
    print("=======================")

    menu = """
1. Add a task
2. View tasks
3. Save tasks
4. Load tasks
5. Exit
"""

    while True:
        print(menu)
        try:
            menu_no = int(input("Enter your choice: "))
            if menu_no == 1:
                task_desc = input("Enter task: ")
                task_manager.add_task(task_desc)
            elif menu_no == 2:
                task_manager.view_tasks()
            elif menu_no == 3:
                task_manager.save_to_file()
            elif menu_no == 4:
                task_manager.load_tasks()
            elif menu_no == 5:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

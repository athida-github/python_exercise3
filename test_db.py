import sqlite3
connection = sqlite3.connect('example.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    age INTEGER NOT NULL,
    grade REAL NOT NULL,
    is_studying INTEGER NOT NULL DEFAULT 1
)
''')
connection.commit()
class Student:
  def __init__(self, name, email, age, grade, is_studying, id = None):
        self.id = id
        self.name = name
        self.email = email
        self.age = age
        self.grade = grade
        self.is_studying = is_studying

  def save_to_db(self):
      cursor.execute('''
      INSERT INTO students (name, email, age, grade, is_studying)
      VALUES (?, ?, ?, ?, ?)
      ''', (self.name, self.email, self.age, self.grade, 1 if self.is_studying == True else 0 ))
      connection.commit()

  def __str__(self):
    return f"({self.id}, {self.name}, {self.email}, {self.age}, {self.grade}, {self.is_studying})"
student1 = Student("Alice", "alice3@email.com", 20, 85, True)
student1.save_to_db()
def fetch_students():
  students_from_db = cursor.execute('SELECT * FROM students').fetchall() # raw results
  students = []
  for student in students_from_db:
    students.append(
        Student(
            student[1], # name
            student[2], # email
            student[3], # age
            student[4], # grade
            True if student[1] == 1 else False, # is_studying -> converting integer to boolean
            student[0] # id
            )
        )

  for student in students:
    print(student)

  print("---------")
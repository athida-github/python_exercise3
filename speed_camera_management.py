import sqlite3
import csv

# Database connection
connection = sqlite3.connect('test.db')
cursor = connection.cursor()

# Speed Camera Entry Object
class SpeedCameraEntry:
    def __init__(self, registration_number, speed, date, over_limit):
        self.registration_number = registration_number
        self.speed = speed
        self.date = date
        self.over_limit = over_limit

    def __str__(self):
        return f'{self.registration_number},{self.speed},{self.date},{self.over_limit}'

    # Add entry to the database
    def add_entry(self):
        cursor.execute('''
        INSERT INTO camera_entries_tbl (registration_number, speed, date, over_limit)
        VALUES (?, ?, ?, ?)
        ''', (self.registration_number, self.speed, self.date, self.over_limit))
        connection.commit()


# Database schema creation
cursor.execute('DROP TABLE IF EXISTS camera_entries_tbl')
cursor.execute('''
    CREATE TABLE camera_entries_tbl (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        registration_number TEXT,
        speed INTEGER,
        date TEXT,
        over_limit TEXT
    )
''')

# View all entries in the database
def view_all_entry():
    camera_entries_db = cursor.execute('SELECT * FROM camera_entries_tbl').fetchall()
    camera_entries = [
        SpeedCameraEntry(
            entry[1], 
            entry[2], 
            entry[3], 
            bool(entry[4]))
        for entry in camera_entries_db
    ]
    for entry in camera_entries_db:
        print(entry)
    print('-------------')
# data update
def update_entry(id, registration_number, speed, date, over_limit):
    cursor.execute('''
    UPDATE camera_entries_tbl
    SET registration_number = ?, speed = ?, date = ?, over_limit = ?
    WHERE id = ?
    ''', (registration_number, speed, date, over_limit, id))
    connection.commit()
#data entry delete
def delete_entry(id):
    cursor.execute('DELETE FROM camera_entries_tbl WHERE id = ?', (id,))
    connection.commit()
    print(f"Entry with ID {id} deleted successfully.")

def export_to_csv(filename='speed_violations.csv'):
    entries = cursor.execute('SELECT * FROM camera_entries_tbl where over_limit=1').fetchall()
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Registration Number', 'Speed', 'Date', 'Over Limit'])
        writer.writerows(entries)
    print(f"Data exported to {filename} successfully.")

def main():
    # Menu-Driven Program
    print('Speed Camera Management System')
    menu = '''
        1. Add a new entry.
        2. View all entries.
        3. Update an entry.
        4. Delete an entry.
        5. Export a report of speed violations to a CSV file.
        6. Exit.
    '''
    print(menu)

    # Test: Adding an entry and viewing it
    while True:
        try:
           menu_no = int(input("Enter your choice: "))
           if menu_no == 1:
               registration_number = int(input("Enter Registration number :"))
               speed = int(input("Enter Speed :"))
               date = input("Enter Date :")
               over_limit = input("Enter Over Limit (True/False): ").strip().lower() == 'true'
               entry = SpeedCameraEntry(registration_number, speed, date, over_limit)
               entry.add_entry()
               print("Entry successfully submitted!")
                    # Test: Adding an entry and viewing it entry = SpeedCameraEntry(1001, 100, '2025-01-01', True)
           elif menu_no == 2:
               view_all_entry()

           elif menu_no == 3:
               print("To Update the data")
               id=int(input("Enter id : "))
               registration_number = int(input("Enter Registration number :"))
               speed = int(input("Enter Speed :"))
               date = input("Enter Date :")
               over_limit = input("Enter Over Limit (True/False): ").strip().lower() == 'true'
               update_entry(id,registration_number,speed,date,over_limit)
               print("Entry Successfully Updated!")

           elif menu_no == 4:
               id = int(input("Enter the respective id number to delete: "))
           elif menu_no==5:
               export_to_csv()               
        except ValueError:
            print("Invalid input. Please enter a number.")
            delete_entry(id)


if __name__ == "__main__":
    main()

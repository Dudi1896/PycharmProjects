import sqlite3


class PhoneBook:
    def __init__(self):
        self.file = "phonebook.db"
        self.pb_database = sqlite3.connect(self.file)
        self.cursorObj = self.pb_database.cursor()
        self.phone_records = ("""CREATE TABLE PHONEBOOK
                (NAME VARCHAR(20) NOT NULL,
                ADDRESS VARCHAR(9) NOT NULL);""")

    def create_db(self):
        self.cursorObj.execute(self.phone_records)
        print(f"Database {self.file} has been formed.")

    def insert_db(self):
        full_name = input('Full Name:')
        phone_number = input('Phone Number:')
        self.cursorObj.execute("""
            INSERT INTO PHONEBOOK(NAME, ADDRESS)
            VALUES (?,?)
            """, (full_name, phone_number))
        self.pb_database.commit()
        print(f"values have been inserted")

    def delete_db(self):
        self.cursorObj.execute("DROP TABLE PHONEBOOK")
        print("Table has been deleted")

    def display_db(self):
        print("|FULL NAME | PHONE NUMBER |")
        for row in self.cursorObj.execute('SELECT * FROM PHONEBOOK'):
            print(row)

    def update_db(self):
        old_name = input("Type the name of user row you want to update: ")
        update_name = input("Input New Name: ")
        update_phone = input("Input new phone number: ")
        self.cursorObj.execute('''UPDATE PHONEBOOK SET NAME = (?) WHERE NAME=(?)''', (update_name, old_name))
        self.cursorObj.execute('''UPDATE PHONEBOOK SET ADDRESS = (?) WHERE NAME=(?)''', (update_phone, old_name))
        print('\nUpdating completed\n')
        self.display_db()


def main():
    while True:
        new_pb_db = PhoneBook()
        print("|---------------------------Menu------------------------------|\n"
              "|Commands:  1 - Create New DataBase   2 - Insert new Row      |\n"
              "|           3 - Display ALL Rows      4 - Update single Row   |\n"
              "|           5 - Delete Database       6 - Exit                |\n")

        user_input = int(input("Enter value: "))

        if user_input == 1:
            new_pb_db.create_db()
        elif user_input == 2:
            new_pb_db.insert_db()
        elif user_input == 3:
            new_pb_db.display_db()
        elif user_input == 4:
            new_pb_db.update_db()
        elif user_input == 5:
            new_pb_db.delete_db()
        elif user_input == 6:
            new_pb_db.pb_database.close()
            quit(f"Database connection has been closed, good bye")

    # except sqlite3.Error as error:
    #     print("Database phonebook.db FAILED to form!", error)


# Execute the main function.
if __name__ == '__main__':
    main()

import mysql.connector as mysql
from tabulate import tabulate 

try:
    conn = mysql.connect(
        host="localhost",
        user="root",
        password="1949",
        database="data"
    )
    if conn.is_connected():
        print("Connected to MySQL database")
        cursor = conn.cursor() 
    else:
        print("Connection failed")
except mysql.connector.Error as err:
    print(f"Error: {err}")

def add_studentrecord():
    s_id = int(input("Enter student id: "))
    sname = input("Enter name: ")
    s_class = input("Enter class: ")
    section = input("Enter section: ")
    father_name = input("Enter father's name: ")
    mother_name = input("Enter mother's name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    address = input("Enter address: ")
    phone_no = input("Enter phone no.: ") 
    sql = "INSERT INTO studentrecords (id, sname, fathername, mothername, DOB, address, contact, class, section) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (s_id, sname, father_name, mother_name, dob, address, phone_no, s_class, section)
    cursor.execute(sql, val)
    conn.commit()
    print(" Details added successfully.")

def add_smark():
    s_id = int(input("Enter student id: "))
    physics = int(input("Enter physics marks: "))
    chemistry = int(input("Enter chemistry marks: "))
    english = int(input("Enter english marks: "))
    maths = int(input("Enter maths marks: "))
    computer = int(input("Enter computer marks: "))
    ai = int(input("Enter ai marks: "))
    sql = "INSERT INTO smark (id, physics, chemistry, english, math, cs, ai) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (s_id, physics, chemistry, english, maths, computer, ai)
    cursor.execute(sql, val)
    conn.commit() 
    print(" MARKS added successfully.")


# View details
def view_studentrecord():
    s_id = int(input("Enter student id to view record: "))
    sql = "SELECT * FROM studentrecords WHERE id = %s"
    cursor.execute(sql, (s_id,)) # Fixed tuple syntax
    row = cursor.fetchall()
    if row:
        # print("s_id | sname | s_class | section | father_name | mother_name | dob | address | phone_no")
        # print(row)
        print(tabulate(row, headers=["s_id" , "sname" , "s_class" , "section" , "father_name" , "mother_name" , "dob" , "address" , "phone_no"]))
    else:
        print("No record found.")
    
#to fix report card pending issue
def report_card():
    s_id = int(input("Enter student id to view report card: "))
    sql = "SELECT * FROM smark WHERE id = %s"
    cursor.execute(sql, (s_id,))
    row = cursor.fetchone()
    
    if row: 
      #  print(" s_id  physics  chemistry  english  maths  computer  ai")
       # print(row)
        print(tabulate([row], headers=["s_id" , "physics" , "chemistry" , "english" , "maths" , "computer" , "ai"]))
        total = sum(row[1:])
        print("Total:", total)
        Percentage = total / 6
        print("Percentage:", Percentage)
        print("Pass" if Percentage >= 33 else "Fail")
        if total >= 270:
            print("Grade: A")
        elif total >= 240:
            print("Grade: B")
        elif total >= 210:
            print("Grade: C")
        else:
            print("Grade: D")
    else:
        print("No marks found for this ID.")

def ranklist():
    s_class = input("Enter class: ")
    s_section = input("Enter section: ")
    sql = "SELECT smark.id, sname, (physics + chemistry + english + math + cs + ai) AS total_marks, ROUND((physics + chemistry + english + math + cs + ai)/6,2) FROM smark JOIN studentrecords on studentrecords.id = smark.id where class= %s and section = %s ORDER BY total_marks DESC"
    cursor.execute(sql, [s_class,s_section])
    rows = cursor.fetchall()
    # print(rows)
    if rows:
        print(tabulate(rows, headers=["ID" , "Name" , "Marks" , "Percentage"]))
    else:
        print("No records found")

def delete_studentrecord():
    s_id = int(input("Enter student id to delete record: "))
    sql = "DELETE FROM studentrecords WHERE id = %s"
    cursor.execute(sql, (s_id,))
    conn.commit()
    print(" STUDENT RECORD DELETED successfully.")


def delete_smark():
    s_id = int(input("Enter student id to delete marks: "))
    sql = "DELETE FROM smark WHERE id = %s"
    cursor.execute(sql, (s_id,))
    conn.commit()
    print(" STUDENT MARKS DELETED successfully.")
    

def update_studentrecord():
    s_id = int(input("Enter student id to update record: "))
    print("Enter new details:")
    sname = input("Enter name: ")
    s_class = input("Enter class: ")
    section = input("Enter section: ")
    father_name = input("Enter father's name: ")
    mother_name = input("Enter mother's name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    address = input("Enter address: ")
    phone_no = input("Enter phone no.: ") 
    sql = "UPDATE studentrecords SET sname=%s, fathername=%s, mothername=%s, DOB=%s, address=%s, contact=%s, class=%s, section=%s WHERE id=%s"
    val = (sname, father_name, mother_name, dob, address, phone_no, s_class, section, s_id)
    cursor.execute(sql, val)
    conn.commit()
    print(" STUDENT  RECORD UPDATE successfully.")


def update_smark():
    s_id = int(input("Enter student id to update marks: "))
    print("Enter new marks:")
    physics = int(input("Enter physics marks: "))
    chemistry = int(input("Enter chemistry marks: "))
    english = int(input("Enter english marks: "))
    maths = int(input("Enter maths marks: "))
    computer = int(input("Enter computer marks: "))
    ai = int(input("Enter ai marks: "))
    sql = "UPDATE smark SET physics=%s, chemistry=%s, english=%s, math=%s, cs=%s, ai=%s WHERE id=%s"
    val = (physics, chemistry, english, maths, computer, ai, s_id)
    cursor.execute(sql, val)
    conn.commit()
    print(" STUDENT MARKS UPDATE successfully.")

while True:
    print("+--------------------+")
    print("|    Operations      |")
    print("+--------------------+")
    print("| 1. add             |")
    print("| 2. view            |")
    print("| 3. update          |")
    print("| 4. delete          |")
    print("| 5. Exit            |")
    print("+--------------------+")
    try:
        choice = int(input("Enter a no. 1-5: "))
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 5.")
        continue    
    if choice == 1:
        print("+-----------------+")
        print("|        add      |")
        print("+-----------------+")
        print("| 1. studentrecords|")
        print("| 2. studentmarks |")
        print("+-----------------+")
        sub_choice = int(input("Enter a no. 1-2: "))
        if sub_choice == 1:
            add_studentrecord()
        else:
            add_smark()    
            
    elif choice == 2:
        print("+-----------------+")
        print("|       view      |")
        print("+-----------------+")
        print("| 1. studentrecord|")
        print("| 2. reportcard   |")
        print("| 3. ranklist     |")
        print("+-----------------+")
        sub_choice = int(input("Enter a no. 1-3: "))
        if sub_choice == 1:
            view_studentrecord()
        elif sub_choice == 2:
            report_card()
        else:
            ranklist()
            
    elif choice == 3:
        print("+-----------------+")
        print("|      update     |")
        print("+-----------------+")
        print("| 1. studentrecord|")
        print("| 2. studentmarks |")
        print("+-----------------+")
        sub_choice = int(input("Enter a no. 1-2: "))
        if sub_choice == 1:
            update_studentrecord()
        else:
            update_smark()  
            
    elif choice == 4:  
        print("+-----------------+")
        print("|      delete     |")
        print("+-----------------+")
        print("| 1. studentrecord|")
        print("| 2. studentmarks |")
        print("+-----------------+")
        sub_choice = int(input("Enter a no. 1-2: "))
        if sub_choice == 1:
            delete_studentrecord()
        else:
            delete_smark()     
            
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

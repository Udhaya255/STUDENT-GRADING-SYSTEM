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
               print("underprocessing")   
            
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
            
#############################################################################################################################
import mysql.connector
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1949",
        database="data"
    )
    if conn.is_connected():
       print("Connected to MySQL database")
    else:
       print("Connection failed")
except mysql.connector.Error as err:
    print(f"Error: {err}")
cursor = conn.cursor()
def add_studentrecord():
    s_id=int(input("Enter student id: "))
    sname = input("Enter name: ")
    s_class=input("Enter class: ")
    section=input("Enter section: ")
    father_name=input("Enter father's name: ")
    mother_name=input("Enter mother's name: ")
    dob=input("Enter date of birth (YYYY-MM-DD): ")
    address=input("Enter address: ")
    phone_no=input("Enter phone no.: ") 
    sql = "INSERT INTO studentrecord (s_id, sname, father_name, mother_name, dob, address, phone_no, s_class, section) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (s_id, sname, father_name, mother_name, dob, address, phone_no, s_class, section)
    cursor.execute(sql, val)
    conn.commit()

def add_smark():
    s_id=int(input("Enter student id: "))
    physics=int(input("Enter physics marks: "))
    chemistry=int(input("Enter chemistry marks: "))
    english=int(input("Enter english marks: "))
    maths=int(input("Enter maths marks: "))
    computer=int(input("Enter computer marks: "))
    ai=int(input("Enter ai marks: "))
    sql = "INSERT INTO smark (s_id, physics, chemistry, english, maths, computer, ai) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (s_id, physics, chemistry, english, maths, computer, ai)
    cursor.execute(sql, val)
    conn.commit() 
def view_studentrecord():
    s_id = int(input("Enter student id to view record: "))
    sql = "SELECT * FROM studentrecord WHERE s_id = %s"
    cursor.execute(sql, (s_id),)
    row = cursor.fetchone()
    print("s_id | sname | s_class | section | father_name | mother_name | dob | address | phone_no")
    print(row)
    

def report_card():
    s_id = int(input("Enter student id to view report card: "))
    sql = "SELECT * FROM smark WHERE s_id = %s"
    cursor.execute(sql, (s_id,))
    row = cursor.fetchone()
    print(" s_id  physics  chemistry  english  maths  computer  ai")
    print(row)
    total = sum(row[1:])
    print("Total:", total)
    Percentage= total / 6
    print("Percentage:", Percentage)
    print( "Pass" if Percentage >= 33 else "Fail")
    if total >= 270:
        print("Grade: A")
    elif total >= 240:
        print("Grade: B")
    elif total >= 210:
        print("Grade: C")
    else:
        print("Grade: D")
def ranklist():
    sql = "SELECT s_id, (physics + chemistry + english + maths + computer + ai) AS total_marks FROM smark ORDER BY total_marks DESC"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(rows)
def delete_studentrecord():
    s_id = int(input("Enter student id to delete record: "))
    sql = "DELETE FROM studentrecord WHERE s_id = %s"
    cursor.execute(sql, (s_id,))
    conn.commit()
def delete_smark():
    s_id = int(input("Enter student id to delete marks: "))
    sql = "DELETE FROM smark WHERE s_id = %s"
    cursor.execute(sql, (s_id,))
    conn.commit()        

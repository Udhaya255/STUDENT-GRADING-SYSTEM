while True:
    print("+--------------------+")
    print("|    Operations      |")
    print("+--------------------+")
    print("| 1. add             |")
    print("| 2. view            |")
    print("| 3. update          |")#
    print("| 4. delete          |")#
    print("| 5. Exit            |")
    print("+--------------------+")
        
    choice = int(input("Enter a no. 1-5: "))
    if choice == 1:
        print("| adding operations |")
        print("| 1. student detail |")
        print("| 2. mark entry     |")
        
        sub_choice = int(input("Enter your choice (1-2): "))
        if sub_choice == 1:
            add_student()
        elif sub_choice == 2:
            mark_entry()
        
        else:
            print("Invalid choice in submenu.")
    elif choice == 2:
        print("| 1. student detail |")
        print("| 2. mark           |")
        
        sub_choice = int(input("Enter your choice (1-2): "))
        if sub_choice == 1:
            view_student()
        elif sub_choice == 2:
            view_marks()
        
        else:
            print("Invalid choice in submenu.")
    elif choice == 3:
        print("| 1. update student detail |")
        print("| 2. mark update           |")
        
        sub_choice = int(input("Enter your choice (1-2): "))
        if sub_choice == 1:
            print("Update student detail")# 
        elif sub_choice == 2:
            print("Update mark ")  #         
        elif sub_choice == 3:
            print("Returning to main menu...")
        else:
            print("Invalid choice in submenu.")
    elif choice == 4:
        print("| 1. delete student detail |")
        print("| 2. mark delete           |")
        
        sub_choice = int(input("Enter your choice (1-2): "))
        if sub_choice == 1:
            print("Delete student detail ") #
        elif sub_choice == 2:
            print("Delete mark ")           #
        
        else:
            print("Invalid choice in submenu.")
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
##############################################################################################################################################################################        
def add_student():
    f= open("student.txt", "a")
    a= int(input("Enter the number of students to add: "))
    for i in range(a):
        name = input("Enter student name: ")
        roll_no = input("Enter roll number: ")
        class_name = input("Enter class name: ")
        extra = input("Enter extra information: ")
        f.write(f"{name} {roll_no} {class_name} {extra}\n")
    f.close() 
def mark_entry():
    f = open("marks.txt", "a")
    a = int(input("Enter the number of students to add marks for: "))
    for i in range(a):
        roll_no = input("Enter roll number: ")
        print("Enter subject and marks in the format 'subject marks':")
        grade=input("enter subject and marks: ")
        f.write(f"{roll_no} {grade}\n")
    f.close()
    print("Marks added successfully.")    
def view_student():
    f= open("student.txt", "r")
    s=input("enter the name of student to view: ")
    for line in f:
        word=line.split()
        if word[0] == s:
            print("Student details:", line)
            return
    print("Student not found.")
    f.close()
def view_marks(): 
    f= open("marks.txt", "r")
    n=input("enter the roll no. of student to view: ")
    for line in f:
        roll_no=line.split()
        if roll_no[0] == n:
            print("Student MARKS:", line)
            return
    print("Student not found.")
    f.close()
    

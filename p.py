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
        
    choice = int(input("Enter a no. 1-5: "))
    if choice == 1:
        print("| adding operations |")
        print("| 1. student detail |")
        print("| 2. mark entry     |")
        print("| 3. exit           |")
        sub_choice = int(input("Enter your choice (1-3): "))
        if sub_choice == 1:
            print(" student detail  ")
        elif sub_choice == 2:
            print(" mark entry ")
        elif sub_choice == 3:
            print("Returning to main menu...")
        else:
            print("Invalid choice in submenu.")
    elif choice == 2:
        print("| 1. student detail |")
        print("| 2. mark           |")
        print("| 3. exit           |")
        sub_choice = int(input("Enter your choice (1-3): "))
        if sub_choice == 1:
            print("View student detail ")
        elif sub_choice == 2:
            print("View mark ")
        elif sub_choice == 3:
            print("Returning to main menu...")
        else:
            print("Invalid choice in submenu.")
    elif choice == 3:
        print("| 1. update student detail |")
        print("| 2. mark update           |")
        print("| 3. exit                  |")
        sub_choice = int(input("Enter your choice (1-3): "))
        if sub_choice == 1:
            print("Update student detail")
        elif sub_choice == 2:
            print("Update mark ")
        elif sub_choice == 3:
            print("Returning to main menu...")
        else:
            print("Invalid choice in submenu.")
    elif choice == 4:
        print("| 1. delete student detail |")
        print("| 2. mark delete           |")
        print("| 3. exit                  |")
        sub_choice = int(input("Enter your choice (1-3): "))
        if sub_choice == 1:
            print("Delete student detail ")
        elif sub_choice == 2:
            print("Delete mark ")
        elif sub_choice == 3:
            print("Returning to main menu...")
        else:
            print("Invalid choice in submenu.")
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

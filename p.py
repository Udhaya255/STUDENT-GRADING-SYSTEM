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
        print("| 1. student detail |")
        print("| 2. mark entry     |")
        print("| 3. exit           |")
    elif choice == 2:
        print("| 1. student detail |")
        print("| 2. mark           |")
        print("| 3. exit           |")
    elif choice == 3:
        print("| 1. update student detail |")
        print("| 2. mark update           |")
        print("| 3. exit                  |")
    elif choice == 4:
        print("| 1. delete student detail |")
        print("| 2. mark delete           |")
        print("| 3. exit                  |")
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

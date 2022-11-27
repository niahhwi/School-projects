def menu():
    print("Make a selection")
    print("1. Add student")
    print("2. Quit")

menu()
selection = int(input("Enter 1 or 2:"))
while selection != 2:
    if selection == 1:
        student_name = input("Please enter your name ")
        v_num = input("Please enter your V-number ")
        grade = input("Please enter your grade")

        lst = str([student_name, v_num, grade])

        with open('roster.txt','a') as file:
            file.write(lst)
            file.write("\n")
            file.read
        menu()
        selection = int(input("Enter 1 or 2:"))
    
    else:
        print("You have quit")
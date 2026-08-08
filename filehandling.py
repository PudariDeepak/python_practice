def add_student():
    sid = input("Enter the student id: ")
    name = input("Enter the student name: ")
    course = input("Enter the student course: ")
    with open("students.txt","a") as file:
        file.write(f"{sid},{name},{course}\n")
    print("Students added sucessfully.")


def update_student():
    id = input("Enter the id for updating student details: ")
    with open("students.txt","r") as file:
        lines = file.readlines()

    is_found = False
    with open("students.txt","w") as file:
        for line in lines:
            details = line.strip().split(",")
            if(details[0] == id):
                is_found = True
                name = input("Enter the updated name: ")
                course = input("Enter the updated course: ")
                file.write(f"{id},{name},{course}\n")
            else:
                file.write(line)
        if(is_found):
            print("Student details updated sucessfully.")
        else:
            print("Student not found.")

def delete_student():
    id = input("Enter id for delete details: ")
    with open("students.txt","r") as file:
        lines = file.readlines()
    is_found = False
    with open("students.txt","w") as file:
        for line in lines:
            details = line.strip().split(",")
            if details[0] != id:
                file.write(line)
            else:
                is_found = True
    if(is_found == False):
        print("Student not found")
    else:
        print("Student deleted successfully.")

def view_student():
    with open("students.txt","r")  as file:
        lines = file.readlines()

        print("--------student details--------")
        for line in lines:
            details = line.strip().split(",")
            print(f"| {details[0]}   | {details[1]}   | {details[2]}")


def run():
    while True:
        print("1) add_student")
        print("2) update_student")
        print("3) delete_student")
        print("4) view_student")
        print("5) exit")

        opt = input("Choose one option: ")
        if opt=="1":
            add_student()
            print("Press enter for continue....")
        elif opt == "2":
            update_student()
            print("Press enter for continue....")
        elif opt == "3":
            delete_student()
            print("Press enter for continue....")
        elif opt == "4":
            view_student()
            print("Press enter for continue....")
        elif opt == "5":
            print("Thank you,You are exited")
            break
        else:
            print("Choose correct option")
run()
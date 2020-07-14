import csv


student_fields = ['id', 'name',  'email', 'deposited', 'due', 'graduated']
student_database = 'students.csv', 'graduated_student.csv'


def display():
    print("1. About Course")
    print("2. Add New Student")
    print("3. View Students")
    print("4. Delete Student")
    print("5. Refund Deposit")


def course_inquiry():
    with open("Course.txt", 'r') as f:
        data = f.read()
    print(data)
    input("Press any key to continue")
    return


def add_student():
    student_data = []
    for i in student_fields:
        value = input("Enter " + i + ": ")
        student_data.append(value)

    with open('students.csv', "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return


def view_students():
    global student_fields
    global student_database

    with open('students.csv', "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for j in student_fields:
            print(j, end='\t |')

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")


def delete_student():

    global student_fields
    global student_database
    update = []

    a = input("Want to delete the students record who hasn't completed training? ")
    if a == "Yes":
        with open('students.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                update.append(row)
                for fields in row:
                    if fields == "No":
                        update.remove(row)
        with open('student.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(update)
        print("deleted successfully")
    else:
        print("Sorry! you must type Yes to continue")

    input("Press any key to continue")


def refund_deposit():

    global student_fields
    global student_database
    refund=[]
    a = input("Want to see the Records of student who will get refund?")
    if a == "Yes":
        with open('students.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                for fields in row:
                    if fields == "Yes":
                        refund.append(row)
        with open('graduated_student.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(refund)
        print("The record of graduated  student from IT Academy has been stored in graduated_student.csv. Thank you!! .")
    else:
        print("Try entering other key from display")

    input("Press any key to continue")


while True:
    display()

    choice = input("Enter your choice: ")
    if choice == '1':
        course_inquiry()
    elif choice == '2':
        add_student()
    elif choice == '3':
        view_students()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        refund_deposit()
    else:
        break


import csv


student_fields = ['id', 'name',  'email', 'deposited', 'remaining' ]
student_database = 'students.csv'


def display():
    print("1. About Course")
    print("2. Add New Student")
    print("3. View Students")


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

    with open(student_database, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return


def view_students():
    global student_fields
    global student_database

    with open(student_database, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for j in student_fields:
            print(j, end='\t |')

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

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
    else:
        break


from student import Student

students = dict()


def choices():
    print(students)
    try:
        print(
            '''
Enrollment System
1. Add Student
2. View Students
3. Exit
            '''
        )
        user_input = int(input("Enter your choice: "))
        match user_input:
            case 1:
                add_student()
            case 2:
                view_student()
            case 3:
                print("Goodbye!")
            case default:
                print("Choice invalid. Please try again.")
                choices()
    except ValueError:
        print("Invalid input. Please try again.")
        choices()


def delete_or_update_choice(full_name):
    try:
        print('''
Modify Student Information
1. Update Student Information
2. Delete Student Information
3. Go Back
4. Exit
        ''')
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                update_student(students[full_name.title()])
            case 2:
                delete_student(full_name)
            case 3:
                return choices()
            case 4:
                print("Goodbye!")
            case default:
                delete_or_update_choice(full_name)
    except ValueError:
        print("Invalid input. Please try again.")
        delete_or_update_choice(full_name)


def delete_student(full_name):
    students.pop(full_name.title())
    print(full_name.title(), "has been deleted.")
    choices()


def update_student(student):
    try:
        old_name = student.get_full_name().title()
        new_full_name = input("Enter new full name: ").title()

        if old_name == new_full_name or new_full_name not in students:
            new_age = int(input("Enter new age: "))
            new_gender = input("Enter new gender: ")
            new_email_address = input("Enter new email address: ")
            student.set_full_name(new_full_name)
            student.set_age(new_age)
            student.set_gender(new_gender)
            student.set_email_address(new_email_address)
            students[new_full_name] = students[old_name] # a = full_name b = old_name,
            if old_name != new_full_name:
                students.pop(old_name)
            print()
            print("Student information updated!")
            print("Student Name:", student.get_full_name())
            print("Student Age:", student.get_age())
            print("Student Gender:", student.get_gender())
            print("Student Email Address:", student.get_email_address())
            print()
            choices()
        else:
            print("Student exists already.")
            update_student(student)
    except ValueError:
        print("Invalid input. Please try again.")
        update_student(student)


def add_student():
    full_name = input("Enter student's full name: ").title()
    if full_name in students:
        print("Student exists already.")
        # add_student()
        choices()
    else:
        age = int(input("Enter student's age: "))
        gender = input("Enter user's gender: ")
        email_address = input("Enter user's email address: ")
        student = Student(full_name, age, gender, email_address)
        students[full_name.title()] = student
        print("Student successfully added!")
        choices()


def view_student():
    if len(students) == 0:
        print("No students enrolled yet!")
        return choices()
    full_name = input("Enter student's full name: ").title()
    if full_name in students:
        student = students[full_name.title()]
        print("Full Name:", student.get_full_name().title())
        print("Age:", student.get_age())
        print("Gender:", student.get_gender())
        print("Email Address:", student.get_email_address())
        delete_or_update_choice(full_name)
    else:
        print("Student not found.")
        choices()


if __name__ == '__main__':
    choices()

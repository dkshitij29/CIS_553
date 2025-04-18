from account import Account
from student import Student
from course import Course
from workflow import student_menu, finance_menu

def main():
    # Setup Accounts and Student
    acc_student = Account("kshitij", "pass123", role_access="student")
    acc_finance = Account("finance", "adminpass", is_finance=True, role_access="finance")
    student = Student("Kshitij", financial_aid_eligible=True, has_scholarship=False, account=acc_student)

    # Course Catalog
    courses = [
        Course("C101", "Python Basics", 100),
        Course("C102", "Web Dev", 120),
        Course("C103", "AI Foundations", 200),
    ]

    # Main Menu
    while True:
        print("\nCourse Management System")
        print("1. Student Login")
        print("2. Finance Team Login")
        print("0. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            student_menu(student, courses)
        elif choice == "2":
            finance_menu(courses)
        elif choice == "0":
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    main()

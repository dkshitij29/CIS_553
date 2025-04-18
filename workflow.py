def student_menu(student, courses):
    while True:
        print(f"\nStudent Menu - {student.name}")
        print("1. View All Courses")
        print("2. Search Courses")
        print("3. Enroll in a Course")
        print("4. Drop a Course")
        print("5. Pay for a Course")
        print("0. Back to Main Menu")

        choice = input("Select an option: ")
        if choice == "1":
            for c in courses:
                print(f"{c.course_id}: {c.name} - ${c.price}")
        elif choice == "2":
            keyword = input("Enter keyword to search: ")
            student.search_courses(keyword, courses)
        elif choice == "3":
            cid = input("Enter course ID: ")
            selected = next((c for c in courses if c.course_id == cid), None)
            if selected:
                selected.enroll(student)
        elif choice == "4":
            cid = input("Enter course ID: ")
            selected = next((c for c in courses if c.course_id == cid), None)
            if selected:
                selected.drop(student)
        elif choice == "5":
            cid = input("Enter course ID: ")
            selected = next((c for c in courses if c.course_id == cid), None)
            if selected:
                student.pay_for_courses(selected.price)
        elif choice == "0":
            break
        else:
            print("Invalid input.")

def finance_menu(courses):
    print("\nFinance Dashboard")
    total = 0
    for c in courses:
        rev = c.revenue()
        print(f"{c.name}: {len(c.enrolled_students)} students, Revenue = ${rev}")
        total += rev
    print(f"\nTotal Revenue: ${total}")

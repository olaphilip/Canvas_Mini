from userClass import User
from studentClass import Student
from instructorClass import Instructor
from adminClass import Admin
from courseClass import Course
from xxxUtility import authenticate

def main():
    attempts = 5
    while True:
        print("1. Login as Student")
        print("2. Login as Instructor")
        print("3. Login as Admin")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if authenticate(username, password, "student"):
                student = Student(username, username, username, password)
                while True:
                    print("Login Successful")
                    student.view_enrolled_courses()
                    choice = input("Press 1 to Logout: ")
                    if choice == "1":
                        break
                    else:
                        print("Invalid choice. Please press 1 to logout.")
            else:
                attempts -= 1
                print(f"Invalid username or password. Please try again. ({attempts}/5 attempts remaining)")
                if attempts <= 0:
                    print("Maximum attempts reached. Exiting.")
                    break

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if authenticate(username, password, "instructor"):
                instructor = Instructor(username, username, username, password)
                while True:
                    instructor.view_assigned_courses()
                    choice = input("Press 1 to Logout: ")
                    if choice == "1":
                        break
                    else:
                        print("Invalid choice. Please press 1 to logout.")
            else:
                attempts -= 1
                print(f"Invalid username or password. Please try again. ({attempts}/5 attempts remaining)")
                if attempts <= 0:
                    print("Maximum attempts reached. Exiting.")
                    break

        elif choice == "3":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if authenticate(username, password, "admin"):
                admin = Admin(username, password)
                while True:
                    print("1. View All Students")
                    print("2. View All Instructors")
                    print("3. View All Courses")
                    print("4. View All Enrollments")
                    print("5. Add a Course")
                    print("6. Add a new Student")
                    print("7. Add a new Instructor")
                    print("8. Enroll a Student in a Course")
                    print("9. Logout")
                    choice = input("Choose an option: ")
                    if choice == "1":
                        admin.view_all_students()
                    elif choice == "2":
                        admin.view_all_instructors()
                    elif choice == "3":
                        admin.view_all_courses()
                    elif choice == "4":
                        admin.view_all_enrollments()
                    elif choice == "5":
                        course_number = input("Enter course number: ")
                        course_title = input("Enter course title: ")
                        instructor_username = input("Enter instructor username: ")
                        admin.add_course(course_number, course_title, instructor_username)
                    elif choice == "6":
                        student_username = input("Enter student username: ")
                        student_password = input("Enter student password: ")
                        student_first_name = input("Enter student first name: ")
                        student_last_name = input("Enter student last name: ")
                        admin.add_student(student_username, student_password, student_first_name, student_last_name)
                    elif choice == "7":
                        instructor_username = input("Enter instructor username: ")
                        instructor_password = input("Enter instructor password: ")
                        instructor_first_name = input("Enter instructor first name: ")
                        instructor_last_name = input("Enter instructor last name: ")
                        admin.add_instructor(instructor_username, instructor_password, instructor_first_name, instructor_last_name)
                    elif choice == "8":
                        student_username = input("Enter student username: ")
                        course_number = input("Enter course number: ")
                        admin.enroll_student(student_username, course_number)
                    elif choice == "9":
                        break
                    else:
                        print("Invalid choice. Please choose a valid option.")
            else:
                attempts -= 1
                print(f"Invalid username or password. Please try again. ({attempts}/5 attempts remaining)")
                if attempts <= 0:
                    print("Maximum attempts reached. Exiting.")
                    break

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
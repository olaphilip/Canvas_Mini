import csv
from tabulate import tabulate

def authenticate(username, password, role):
    if role == 'student':
        with open('students.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    return True
    elif role == 'instructor':
        with open('instructors.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    return True
    elif role == 'admin':
        with open('admins.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username and row[1] == password:
                    return True
    return False

def view_enrolled_courses(username):
    with open('enrollments.csv', 'r') as file:
        reader = csv.reader(file)
        enrolled_courses = [[row[1], row[2], row[3]] for row in reader if row[0] == username]
        print("Enrolled Courses:")
        print(tabulate(enrolled_courses, headers=["Course Number", "Course Title", "Instructor Username"], tablefmt="grid"))

def view_assigned_courses(username):
    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        assigned_courses = [[row[0], row[1]] for row in reader if row[2] == username]
        print("Assigned Courses:")
        print(tabulate(assigned_courses, headers=["Course Number", "Course Title"], tablefmt="grid"))

def view_all_courses():
    with open('courses.csv', 'r') as file:
        reader = csv.reader(file)
        all_courses = [row for row in reader]
        print(tabulate(all_courses, headers=['Course Number', 'Course Title', 'Instructor Username']))

def view_all_students():
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        all_students = [row for row in reader]
        print(tabulate(all_students, headers=['Username', 'Password', 'First Name', 'Last Name', 'Role']))

def view_all_instructors():
    with open('instructors.csv', 'r') as file:
        reader = csv.reader(file)
        all_instructors = [row for row in reader]
        print(tabulate(all_instructors, headers=['Username', 'Password', 'First Name', 'Last Name', 'Role']))

def view_all_enrollments():
    with open('enrollments.csv', 'r') as file:
        reader = csv.reader(file)
        all_enrollments = [row for row in reader]
        print(tabulate(all_enrollments, headers=['Student Username', 'Course Number', 'Course Title', 'Instructor Username']))

def add_student(username, password, first_name, last_name):
    with open('students.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password, first_name, last_name])

def add_instructor(username, password, first_name, last_name):
    with open('instructors.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password, first_name, last_name])

def add_course(course_number, course_title, instructor_username):
    with open('courses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([course_number, course_title, instructor_username])

def enroll_student(username, course_number):
    with open('enrollments.csv', 'r') as enrollments_file:
        enrollments_reader = csv.reader(enrollments_file)
        enrollments = [row for row in enrollments_reader]
        for enrollment in enrollments:
            if enrollment[0] == username and enrollment[1] == course_number:
                print("Student already enrolled in this course.")
                return
    with open('courses.csv', 'r') as courses_file:
        courses_reader = csv.reader(courses_file)
        course_info = [row for row in courses_reader if row[0] == course_number]
        if course_info:
            course_title = course_info[0][1]
            instructor_username = course_info[0][2]
            with open('enrollments.csv', 'a', newline='') as enrollments_file:
                enrollments_writer = csv.writer(enrollments_file)
                enrollments_writer.writerow([username, course_number, course_title, instructor_username])
                print(f"{username} has been enrolled in {course_number}.")
        else:
            print("Course not found")
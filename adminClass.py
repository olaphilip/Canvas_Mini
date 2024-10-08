from courseClass import Course
from xxxUtility import add_student, add_instructor, view_all_students, view_all_instructors, view_all_courses, enroll_student, view_all_enrollments

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.courses = []

    def view_all_students(self):
        view_all_students()

    def view_all_instructors(self):
        view_all_instructors()

    def view_all_courses(self):
        view_all_courses()

    def view_all_enrollments(self):
        view_all_enrollments()

    def add_course(self, course_number, course_title, instructor_username):
        self.courses.append(Course.add_course(course_number, course_title, instructor_username))
        print(f"Course {course_number} added successfully.")

    def enroll_student(self, student_username, course_number):
        self.courses.append(enroll_student(student_username, course_number))

    def add_student(self, username, password, first_name, last_name):
        add_student(username, password, first_name, last_name)
        print("User account created successfully.")

    def add_instructor(self, username, password, first_name, last_name):
        add_instructor(username, password, first_name, last_name)
        print("User account created successfully.")
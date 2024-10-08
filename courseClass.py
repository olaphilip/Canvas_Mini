from xxxUtility import add_course, enroll_student

class Course:
    def __init__(self, course_number, course_title, instructor_username):
        self.course_number = course_number
        self.course_title = course_title
        self.instructor_username = instructor_username
        self.enrolled_students = []

    @classmethod
    def add_course(cls, course_number, course_title, instructor_username):
        return add_course(course_number, course_title, instructor_username)
    
    def enroll(self, student_username):
        return enroll_student(student_username, self.course_number)
from xxxUtility import view_enrolled_courses

class Student:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def view_enrolled_courses(self):
        return view_enrolled_courses(self.username)
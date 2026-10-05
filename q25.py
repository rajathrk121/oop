class Student():
    def __init__(self,student_id,name):
        self.student_id=student_id
        self.name=name
        self.courses={}

class Course():
    def __init__(self,c_id,c_name):
        self.course_id=c_id
        self.course_name=c_name

class SMS():
    def __init__(self):
        self.student={}
        self.course={}

    def add_student(self):
        s_id=input("Enter Student id: ")
        s_name=input("Enter name of the student: ")

        self.student[s_id]=s_name
        print("Student added successfully...")

    def add_course(self):
        c_id=input("Enter course id: ")
        c_name=input("Enter course name: ")
        self.course[c_id]=c_name
        print("Course added successfully...")

    def assign_course(self):
        s_id=input("Enter student id: ")
        c_id=input("Enter course name: ")
        if s_id not in self.student:
            print("Student Not Found.....")
            return
        if c_id not in self.course:
            print("Course not found")
            return
        self.student[s_id].course[c_id]=None
        



        
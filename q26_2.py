class Student:
    def __init__(self,name,id):
        self.name=name
        self.s_id=id

class course:
    def __init__(self,name,c_id):
        self.course_name=name
        self.course_id=c_id

class SMS():
    def __init__(self):
        self.student={}
        self.course={}

    def add_student(self):
        s_name=input("Enter name of the student: ")
        s_id =input("Enter student id: ")
        self.student[s_id] = {
            'name': s_name,
            'course': []
        }
        print("Student added successfully...")

    def add_course(self):
        c_name=input("Enter course name: ")
        c_id=input("Enter course id: ")
        self.course[c_id]=c_name

    def course_assign(self):
        s_id=input("Enter student id: ")
        c_id=input("Enter course id: ")

        if s_id in self.student and c_id in self.course:
            self.student[s_id]["course"].append(c_id)
            print("Course assigned successfully...") 
        else: 
            print("Student or course not found check entered student id and course id")

    def display_student(self):
        for i in self.student:
            print("Student ID:", i)
            print("Name:", self.student[i]["name"])

            for c_id in self.student[i]["course"]:
                print("Course: ", self.course[c_id])

            print()
        print()

    def search_student(self):
        id=input("Enter id of the student: ")
        if id not in self.student:
            print("No student Found...")
        else:
            print(self.student[id])
sms = SMS()
while True:
    print("1. Add Student \n2. Add Course \n3. Assign COurse \n4. Display Student \n5. Search Student")

    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            sms.add_student()
        case 2:
            sms.add_course()
        case 3:
            sms.course_assign()
        case 4:
            sms.display_student()
        case 5:
            sms.search_student()
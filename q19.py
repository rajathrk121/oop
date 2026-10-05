class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display(self):
        print("Name of the Student: ",self.name)
        print("Age: ",self.age)

class additional(Student):
    def __init__(self, name, age,course,address):
        super().__init__(name, age)
        self.course=course
        self.address=address

    def student_details(self):
        print("Course: ",self.course)
        print("Address: ",self.address)

s1=additional("Rajath",20,"BCA","Ramanilyam")

s1.display()
s1.student_details()
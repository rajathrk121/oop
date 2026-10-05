class Student():
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course

    def __str__(self):
        return f"Student name:{self.name}  age:{self.age}  course:{self.course}"

stu=Student("Rajath",20,'BCA')

print(stu)
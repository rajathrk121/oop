class exam():
    def __init__(self):
        self.Grade="0"

    def mark(self):
        mark1=int(input("Enter mark of Maths: "))
        mark2=int(input("Enter mark of CS: "))
        mark3=int(input("Enter mark lof Physics: "))

        Total_mark=mark1+mark2+mark3
        print('Total Mark: ',Total_mark)
        Average=Total_mark/3
        print('Average: ',Average)

        if mark1>100 or mark1<0:
            print("Invalid mark !!! Please enter a valid mark...")
        elif mark1 >= 90 :
            self.Grade='A'
            print("Maths: ",self.Grade,"GRADE")
        elif mark1>=80:
            self.Grade='B'
            print('Maths: ',self.Grade,"GRADE")
        elif mark1>=70:
            self.Grade='C'
            print('Maths: ',self.Grade,"GRADE")
        elif mark1>=60:
            self.Grade='D'
            print('Maths: ',self.Grade,"GRADE")
        elif mark1>=50:
            self.Grade='E'
            print('Maths: ',self.Grade,"GRADE")
        else:
            self.Grade='F'
            print('Maths: ',self.Grade,"GRADE")
            print("Fail")
        print()

        if mark2>100 or mark2<0:
            print("Invalid mark !!! Please enter a valid mark...")
        elif mark2 >= 90 :
            self.Grade='A'
            print("CS: ",self.Grade,"GRADE")
        elif mark2>=80:
            self.Grade='B'
            print('CS: ',self.Grade,"GRADE")
        elif mark2>=70:
            self.Grade='C'
            print('CS: ',self.Grade,"GRADE")
        elif mark2>=60:
            self.Grade='D'
            print('CS: ',self.Grade,"GRADE")
        elif mark2>=50:
            self.Grade='E'
            print('CS: ',self.Grade,"GRADE")
        else:
            self.Grade='F'
            print('CS: ',self.Grade,"GRADE")
            print("Fail")

        print()

        if mark3>100 or mark3<0:
            print("Invalid mark !!! Please enter a valid mark...")
        elif mark3 >= 90 :
            self.Grade='A'
            print("Physics: ",self.Grade,"GRADE")
        elif mark3>=80:
            self.Grade='B'
            print('Physics: ',self.Grade,"GRADE")
        elif mark3>=70:
            self.Grade='C'
            print('Physics: ',self.Grade,"GRADE")
        elif mark3>=60:
            self.Grade='D'
            print('Physics: ',self.Grade,"GRADE")
        elif mark3>=50:
            self.Grade='E'
            print('Physics: ',self.Grade,"GRADE")
        else:
            self.Grade='F'
            print('Physics: ',self.Grade,"GRADE")
            print("Fail")
        


exam_=exam()
exam_.mark()
        


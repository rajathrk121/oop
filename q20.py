class salary():
    def __init__(self):
        self.salary=0

    def display(self):
        print("Salary: ",self.salary)

class fulltime(salary):
    def __init__(self):
        super().__init__()
        self.salary=40000
        

    def full_time(self):
        print("Full-Time salary: ",self.salary)

class partime(salary):
    def __init__(self):
        super().__init__()
        self.time=int(input("Enter your working hours: "))
        self.amount=300

    def cal_salary(self):
        self.salary=self.time*self.amount

    def part_time(self):
        print("Your partime salary is: ",self.salary)

print("1. Full Time Employee")
print("2. Part Time Employee")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        f1 = fulltime()
        f1.full_time()

    case 2:
        p1 = partime()
        p1.cal_salary()
        p1.part_time()

    case _:
        print("Invalid choice")

# f1 = fulltime()
# f1.full_time()

p1 = partime()
p1.cal_salary()
p1.part_time()
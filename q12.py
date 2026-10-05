class employee():
    def __init__(self):
        self.salary=50000

    def sal_hike(self):
        sal=int(input("Enter the percentage to be increased: "))
        new_sal=self.salary+(self.salary*sal/100)
        print("New Salary after hike: ",new_sal)

emp1_=employee()

emp1_.sal_hike()

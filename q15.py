class employee():
    def __init__(self):
        self.salary=int(input("Enter your current salary: "))

    def view_salary(self):
        print("Your salary is: ",self.salary)

    def update_salary(self):
        new_salary=int(input("Enter your new salary: "))
        self.salary=new_salary
        print("Your updated salary is: ",self.salary)

    def menu(self):
        print("1. View Salary \n2.Update Salary \n3. Exit")
        action=int(input('Enter the action: '))
        if action ==1:
            self.view_salary()
        elif action==2:
            self.update_salary()
        elif action==3:
            print("Program exiting...")
            exit()
            
        
        else:
            print("Invalid action !!! \nEnter a valid action")

emp1=employee()
emp1.menu()
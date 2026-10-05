class job:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def __str__(self):
        return f"Employee details \nName: {self.name} Id: {self.id} Salary: {self.salary}"
    

emp1=job("Rajath",7,100000)
print(emp1)
        
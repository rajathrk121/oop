class hospital():
    def __init__(self):
        self.name="Rajath"
        self.age=20
        self.address="Ramanilayam Thiruvallur"
        self.pincode=673541

    def patientcheck(self):
        name=input("Enter the name of the person : ")
        age=int(input("Enter age: "))

        if name==self.name and age==self.age:
            print("---Match found--- \n",self.name ,'\n',self.age ,'\n',self.address ,'\n',self.pincode)
        else:
            print("\nMatch not found!!! \nCheck entered details carefully...")

pat1=hospital()

pat1.patientcheck()
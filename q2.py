class car():
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def __str__(self):
        return f"{self.brand} {self.model} : {self.price}"

car1=car("Toyota","Fortuner",4800000)
car2=car("BMW","530D","2CR")
car3=car("Renault","Duster",800000)

print('\n',car1,'\n',car2,'\n',car3)
        
class vehicle:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print("Brand: ",self.brand)
        print("Model: ",self.model)
        print("Price: ",self.price)

class car(vehicle):
    def __init__(self, brand, model, price,seat):
        super().__init__(brand, model, price)
        self.seat=seat

    def car_feature(self):
        print("Number of seats: ",self.seat)

class bike(vehicle):
    def __init__(self, brand, model, price,engine_cc):
        super().__init__(brand, model, price)
        self.engine=engine_cc

    def bike_feature(self):
        print("Engine CC: ",self.engine)

car1=car('Hyundai','Creta',1200000,5)
car1.display()
car1.car_feature()
print()
bike1=bike('RE','Himalaya 411',375000,411)
bike1.display()
bike1.bike_feature()
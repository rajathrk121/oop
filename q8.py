class store:
    def __init__(self):
        self.mobiles = {}


    def mob(self):
        for i in range(5):
            mob=input(f"Enter the name of the phone {i+1} :")
            price=int(input("Enter price of the phone: "))

            self.mobiles[mob]=price

        for mob,price in self.mobiles.items():
            if price >20000:
                print("Price of the phone above 20000 is \n",mob,price)

store1=store()

store1.mob()

    
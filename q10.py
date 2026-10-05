class store():
    def __init__(self):
        self.product={}

    def prod(self):
        Name = input("Enter product name: ")
        Price=int(input("Enter price: "))
        quantity = int(input("Enter item quantity"))

        self.product[Name]=Price,quantity

        Total_price=Price*quantity

        print("Total price: ",Total_price)

store1=store()

store1.prod()
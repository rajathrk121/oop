class payment():
    def __init__(self,amount):
        self.amount=amount

    def process_payment(self):
        print("Payment Successfull")

class UPI(payment):
    def process_payment(self):
        print("UPI Payment: ",self.amount)

class Card(payment):
    def process_payment(self):
        print("Card Payment: ",self.amount)

class Cash(payment):
    def process_payment(self):
        print("Cash Payment: ",self.amount)
amount=int(input("Enter the amount: "))

print("1. UPI \n2. Card \n3. Cash")

choice=int(input("Enter your choice: "))

match choice:
    case 1:
        Payment=UPI(amount)
    case 2:
        Payment=Card(amount)
    case 3:
        Payment=Cash(amount)
    case _:
        print("Invalid choice!!! \nEnter a valid choice...")
        exit()

Payment.process_payment()


    
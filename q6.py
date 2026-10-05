class bank:
    def __init__(self):
        
        self.balance=1000

    def depo(self):
        d_amount=int(input("Enter deposit amount: "))
        self.balance+=d_amount
        print(f"{d_amount} deposited successfullyyy...")

    def withd(self):
        w_amount=int(input("Enter withdraw amount: "))
        if w_amount<=self.balance:
            self.balance-=w_amount
            print(f"{w_amount} withdrawn successfully")
        else:
            print("Insufficient balance!!!")

        

    def bal(self):
        print(f'Available balance: {self.balance}')

    # def __str__(self):
        # return f"Bank Account Status -> Available Balance: {self.balance}"

b=bank()

b.depo()
b.withd()
b.bal()
        
        
class bank():
    def __init__(self):
        self.balance=1000

    def deposit(self):
        dep_amount=int(input("Enter deposit amount: "))
        self.balance+=dep_amount
        print("New balance: ",self.balance)

    def withdraw(self):
        with_amount=int(input("Enter withdraw amount: "))
        if with_amount>self.balance:
            print("Insufficient Balance!!!")
        else:
            self.balance-=with_amount
            print("New Balance: ",self.balance)

    def checkbalance(self):
        print("Current Balance: ",self.balance)

    def menu(self):
        print('1. Deposit \n2. Withdraw \n3. Check Balance')
        self.action=int(input("Enter the action: "))
        if self.action==1:
            self.deposit()
        elif self.action==2:
            self.withdraw()
        elif self.action==3:
            self.checkbalance()
        else:
            print("Invalid action!!!!!")

    
bank1=bank()
bank1.menu()
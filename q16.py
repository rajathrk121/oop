class user():
    def __init__(self):
        self.password="Rajath@123"

    def pass_upda(self):
        passw=input("Enter current password:")
        if passw==self.password:
            new_pass=input("Enter new password: ")
            self.password=new_pass
            print("Password updated...")
        else:
            print("Password incorrect!!! Check entered password...")

user1=user()
user1.pass_upda()

    
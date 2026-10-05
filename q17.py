class animal:
    def __init__(self):
        pass
    def cat(self):
        print("Meowww")
    def cow(self):
        print("Mmaahhhh")
    def dog(self):
        print("Bow bow")
    def menu(self):
        print("1. Cat \n2.Cow \n3. Dog")
        choice=int(input("Enter your choice: "))
        match choice:
            case 1:
                self.cat()
            case 2:
                self.cow()
            case 3:
                self.dog()
            case _:
                print("Enter a valid choice...")

a1=animal()
a1.menu()

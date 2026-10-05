class store:
    def __init__(self):
        self.title=input("Enter the title of the book: ")
        self.author= input("Enter the name of the author: ")
        self.price=int(input("Enter the price of the book: "))

    def display(self):
        print("Title of the book : ", self.title)
        print('Author of the book is: ',self.author)
        print("Price of the book: ",self.price)

str1=store()

str1.display()




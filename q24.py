class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        book = input("Enter book name: ")
        self.books.append(book)
        print("Book added successfully")

    def register_member(self):
        member = input("Enter member name: ")
        self.members.append(member)
        print("Member registered successfully")

    def borrow_book(self):
        book = input("Enter book name to borrow: ")

        if book in self.books:
            self.books.remove(book)
            print("Book borrowed successfully")
        else:
            print("Book is not available")

    def return_book(self):
        book = input("Enter book name to return: ")
        self.books.append(book)
        print("Book returned successfully")

    def display_books(self):
        if len(self.books) == 0:
            print("No books available")
        else:
            print("Available Books:")
            for book in self.books:
                print(book)


library = Library()

while True:
    print("\n--- Library Management ---")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        library.add_book()

    elif choice == 2:
        library.register_member()

    elif choice == 3:
        library.borrow_book()

    elif choice == 4:
        library.return_book()

    elif choice == 5:
        library.display_books()

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
# Class of Library
# Register Users name by
# Lend
# return
# add
# del
# check what books are available
# Library on our name : elderny
# Create a main function with while loop inserted

#EXTRA -> Create a dictionary and store value of users who have lended the books and who...
def secret_key():
    import random
    key = random.randint(1000,58123)
    Secret_key = key
    return Secret_key
class Library():
    def __init__(self, book_list, library):
        self.list_data = {}
        self.book_list = book_list
        self.library = library

        for books in self.book_list:
            self.list_data[books] = None

    def display_book(self):
        for index, book in enumerate(self.book_list):
            print(f"{index}:{book}")

    def lend_book(self, book, user):
        if book in self.book_list:
            if self.list_data[book] is None:
                self.list_data[book] = user
            else:
                print(f"Sorry this book is already lended by {self.lend_data[book]}")
        else:
            print("You have written wrong book name")

    def return_book(self, book, user):
        if book in self.list_data:
            if self.list_data[book] is not None:
                self.list_data.pop(book)
            else:
                print("Book hasn't been lended yet")
        else:
            print("The Book isn't in the list")

    def add(self, book):
        self.book_list.append(book)
        self.list_data[book] = None # to make sure it has None value
    def remove(self, book):
        self.book_list.remove(book)
        self.list_data.pop(book)
def main():
    book_list = ["Choas", "run to death", "crazy"]
    library = "elderny"
    elderny = Library(book_list, library)
    End = False
    Secret_Code = secret_key()
    print(f"Welcome to the library of {library}, Type 'd' to check books, 'l' to lend books, 'r' to return books, 'a' to add books, "
          f"'del' to delete books and 'q' to quit the program")
    while (End == False):
        _ask = input("Type your text (d,l,r,a,del,q): ").lower()
        if _ask == "q":
            End = True
            print("Program Closed")
        elif _ask == "d":
            print("These books are in our Library")
            elderny.display_book()
        elif _ask == "l":
            _name = input("Please Type your Name: ")
            _book = input("Type Your Book Name To lend: ")
            elderny.lend_book(_book, _name)
            print(f"Book: {_book}, lended successfully\n")
        elif _ask == "r":
            _book = input("Type Your Book Name To Return: ")
            _name = input("Type Your Name: ")
            elderny.return_book(_book, _name)
            print(f"book: {_book}, returned successfully\n")
        elif _ask == "a":
            _book = input("Type Name of the Book You Want To Add: ")
            elderny.add(_book)
            print(f"book: {_book}, added successfully\n")
        elif _ask == "del":
            print("Your Secret key is: ", Secret_Code)
            _pass = int(input("Please Type the Secret key: "))
            if _pass == Secret_Code:
                _book = input("Type The Name of Book You Want To Remove: ")
                if _book in book_list:
                    elderny.remove(_book)
                    print(f"Book {_book}, has been deleted Successfully")
            else:
                print("Wrong Secret Code")


if __name__ == "__main__":
    main()
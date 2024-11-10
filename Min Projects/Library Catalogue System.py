class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def check_out(self):
    
        if self.available:
            self.available = False
            print(f"You have checked out '{self.title}' by {self.author}.")
        else:
            print(f"'{self.title}' is currently unavailable.")

    def return_book(self):
    
        if not self.available:
            self.available = True
            print(f"You have returned '{self.title}' by {self.author}.")
        else:
            print(f"'{self.title}' was not checked out.")

    def display_info(self):
    
        status = "Available" if self.available else "Checked out"
        print(f"Title: '{self.title}', Author: {self.author}, Status: {status}")


class LibraryCatalog:
    def __init__(self):
        self.books = []  # List to hold book instances

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' by {book.author} to the catalog.")

    def display_all_books(self):
        print("\nLibrary Catalog:")
        for book in self.books:
            book.display_info()

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None


if __name__ == "__main__":
    catalog = LibraryCatalog()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
    book2 = Book("1984", "George Orwell")
    book3 = Book("To Kill a Mockingbird", "Harper Lee")

    catalog.add_book(book1)
    catalog.add_book(book2)
    catalog.add_book(book3)

    catalog.display_all_books()

    book_to_check_out = catalog.find_book("1984")
    if book_to_check_out:
        book_to_check_out.check_out()

    catalog.display_all_books()

    book_to_return = catalog.find_book("1984")
    if book_to_return:
        book_to_return.return_book()

    catalog.display_all_books()

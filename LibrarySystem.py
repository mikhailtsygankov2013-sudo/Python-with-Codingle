class Book:
    is_borrowed = False
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def borrow(self):
        is_borrowed = True
        print("Book",self.title,"by",self.author,"is borrowed")
    def return_book(self):
        is_borrowed = False
        print("Book",self.title,"by",self.author,"is returned")

book1 = Book("Harry Potter","Jackie Rolin")
book2 = Book("Atomic habits","James Clear")
book3 = Book("The art of letting go","Nick")

book1.borrow()
book2.borrow()
book3.borrow()

book1.return_book()
book2.return_book()
book3.return_book()

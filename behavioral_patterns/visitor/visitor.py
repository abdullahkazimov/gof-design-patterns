from abc import ABC, abstractmethod

class Visitor(ABC):

    @abstractmethod
    def visit_book(self, book):
        pass

    @abstractmethod
    def visit_journal(self, journal):
        pass

class Product(ABC):

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

class Book(Product):
    def __init__(self, title, price, author, pages):
        self.title = title
        self.price = price
        self.author = author
        self.pages = pages

    def accept(self, visitor: Visitor):
        return visitor.visit_book(self)

class Journal(Product):
    def __init__(self, title, price, author, pages):
        self.title = title
        self.price = price
        self.author = author
        self.pages = pages

    def accept(self, visitor: Visitor):
        return visitor.visit_journal(self)
    
class TaxCalculator(Visitor):

    def visit_book(self, book: Book):
        return book.price * book.pages
    
    def visit_journal(self, journal: Journal):
        return journal.price * journal.pages

class CostCalculator(Visitor):

    def visit_book(self, book: Book):
        return book.price * book.pages + 2.50
    
    def visit_journal(self, journal: Journal):
        return journal.price * journal.pages + 3.50

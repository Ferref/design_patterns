from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator

# Concrete collection class that implements the Iterable interface
class BookCollection(Iterable):
    def __init__(self):
        self._books = []  # Internal storage for books

    def add_book(self, book: str) -> None:
        # Method to add a book to the collection
        self._books.append(book)

    def __iter__(self) -> Iterator:
        # Return an instance of the iterator
        return BookIterator(self)

    # Additional methods can be added here to manipulate the collection

# Concrete iterator class that implements the Iterator interface
class BookIterator(Iterator):
    def __init__(self, collection: BookCollection):
        self._collection = collection  # Collection to iterate through
        self._index = 0  # Current index of the iterator

    def __iter__(self) -> 'BookIterator':
        return self  # Iterator itself is the iterator

    def __next__(self) -> str:
        if self._index < len(self._collection._books):
            book = self._collection._books[self._index]  # Get the current book
            self._index += 1  # Move to the next index
            return book
        else:
            raise StopIteration  # Stop iteration if no more elements

# Client code that uses the BookCollection and its iterator
if __name__ == '__main__':
    # Create a book collection
    my_books = BookCollection()
    my_books.add_book("The Catcher in the Rye")
    my_books.add_book("To Kill a Mockingbird")
    my_books.add_book("1984")
    
    # Use the iterator to print out the books in the collection
    for book in my_books:
        print(book)
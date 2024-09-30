from function import Search
from book import Book, BookCollection


class Library:
    def __init__(self) -> None:
        self.collection = BookCollection()

    def search(self, key: str, value: str | int) -> list[Book]:
        return Search().search(self.collection.books, key, value)

    def add(self, book: Book) -> None:
        self.collection.add_book(book)

    def remove(self, key: str, value: str | int) -> None:
        books_to_remove = self.search_by(key, value)
        self.collection.remove_book(books_to_remove)

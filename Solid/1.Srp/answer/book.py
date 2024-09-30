from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    publication_year: int


class BookCollection:
    def __init__(self) -> None:
        self.books = []

    @property
    def total_number_of_books(self) -> int:
        return len(self.books)

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, books: list[Book]) -> None:
        self.books = [b for b in self.books if b not in books]

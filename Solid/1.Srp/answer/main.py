from library import Library
from book import Book


if __name__ == "__main__":
    lib = Library()

    lib.add(book=Book("Clean Code", "Edric Cao", 2023))
    lib.add(book=Book("Design Pattern", "Edric Cao", 2022))

    print(lib.search(key="title", value="Clean  Code"))

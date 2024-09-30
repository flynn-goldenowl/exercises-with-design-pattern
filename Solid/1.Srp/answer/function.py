from book import Book


class Search:
    def __init__(self) -> None:
        self.methods = {
            "title": self._search_by_title,
            "author": self._search_by_author,
            "publication_year": self._search_by_publication_year,
        }

    def _search_by_title(self, books: list[Book], title: str) -> list[Book]:
        return [b for b in books if b.title == title]

    def _search_by_author(self, books: list[Book], author: str) -> list[Book]:
        return [b for b in books if b.author == author]

    def _search_by_publication_year(
        self, books: list[Book], publication_year: int
    ) -> list[Book]:
        return [b for b in books if b.publication_year == publication_year]

    def search(self, books: list[Book], key: str, value: str | int):
        return self.methods[key](books, value)

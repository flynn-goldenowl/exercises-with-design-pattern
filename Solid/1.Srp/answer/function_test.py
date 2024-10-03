import unittest
from book import Book
from function import Search

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.books = [
            Book(title="Clean Code", author="Edric Cao", publication_year=2001),
            Book(title="Design Pattern", author="Edric Cao", publication_year=2002),
        ]
        self.search = Search()

    def test_search_by_title(self):
        result = self.search._search_by_title(self.books, "Clean Code")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "Clean Code")

    def test_search_by_author(self):
        result = self.search._search_by_author(self.books, "Edric Cao")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].author, "Edric Cao")

    def test_search_by_publication_year(self):
        result = self.search._search_by_publication_year(self.books, 2002)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].publication_year, 2002)

    def test_search(self):
        result = self.search.search(self.books, "title", "Design Pattern")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "Design Pattern")

if __name__ == "__main__":
    unittest.main()

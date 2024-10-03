import unittest
from book import Book
from library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book(title="Clean Code", author="Edric Cao", publication_year=2001)
        self.book2 = Book(title="Design Pattern", author="Edric Cao", publication_year=2002)

    def test_add(self):
        self.library.add(self.book1)
        self.assertEqual(len(self.library.collection.books), 1)

    def test_search(self):
        self.library.add(self.book1)
        result = self.library.search("title", "Clean Code")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "Clean Code")

    def test_remove(self):
        self.library.add(self.book1)
        self.library.add(self.book2)
        self.library.remove("title", "Clean Code")
        self.assertEqual(len(self.library.collection.books), 1)
        self.assertEqual(self.library.collection.books[0].title, "Design Pattern")

if __name__ == "__main__":
    unittest.main()

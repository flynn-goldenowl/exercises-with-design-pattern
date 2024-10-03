import unittest
from book import Book, BookCollection

class TestBookCollection(unittest.TestCase):
    def setUp(self):
        self.collection = BookCollection()
        self.book1 = Book(title="Clean Code", author="Edric Cao", publication_year=2001)
        self.book2 = Book(title="Desisgn Pattern", author="Edric Cao", publication_year=2002)

    def test_add_book(self):
        self.collection.add_book(self.book1)
        self.assertEqual(self.collection.total_number_of_books, 1)

    def test_remove_book(self):
        self.collection.add_book(self.book1)
        self.collection.add_book(self.book2)
        self.collection.remove_book([self.book1])
        self.assertEqual(self.collection.total_number_of_books, 1)
        self.assertEqual(self.collection.books[0], self.book2)

    def test_total_number_of_books(self):
        self.assertEqual(self.collection.total_number_of_books, 0)
        self.collection.add_book(self.book1)
        self.assertEqual(self.collection.total_number_of_books, 1)

if __name__ == "__main__":
    unittest.main()

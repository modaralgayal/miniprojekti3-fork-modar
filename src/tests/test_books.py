import unittest
from book import add_book, get_books
# from unittest.mock import Mock, ANY
import test_db

class MockBook:
    def __init__(self, title, author, year, publisher, url):
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.url = url

    

class TestBook(unittest.TestCase):
    def setUp(self):

        self.book = MockBook()
        self.connection = test_db.connect()
        self.book.add_book("Test book", "Test author", "1", "test publisher" "test url")
        

    def TestGetBooks(self):
        kirja_lista = self.book.get_books()
        self.assertEqual(kirja_lista[0], "Test book")
        

         
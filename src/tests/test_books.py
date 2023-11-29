import unittest
from reference import add_book, get_books
from db import db
import app

    

class TestBook(unittest.TestCase):
    def setUp(self):
        add_book("Test book", "Test author", 1, "test publisher", "test url", db)
        

    def test_get_books(self):
        kirja_lista = get_books(db)
        self.assertEqual(kirja_lista[0], ("Test book","Test author", 1, "test publisher", "test url"))
        

         
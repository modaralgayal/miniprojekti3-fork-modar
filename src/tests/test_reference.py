import unittest
import reference
from db import db
import app

class TestReference(unittest.TestCase):
    def setUp(self):
        reference.initialize_test_database(db)
        

    def test_get_books(self):
        reference.add_book("Test book", "Test author", 1, "Test publisher", "test url", db)
        books = reference.get_books(db)
        self.assertEqual(books[0], (1, "Test book","Test author", 1, "Test publisher", "test url"))
        self.assertEqual(len(books), 1)


    def test_get_articles(self):
        reference.add_article("Test article", "Test author", 2, "Test journal", "Test url", db)
        articles = reference.get_articles(db)
        self.assertEqual(articles[0], (1,"Test article", "Test author", 2, "Test journal", "Test url"))
        self.assertEqual(len(articles), 1)
    

    def test_get_inproceedings(self):
        reference.add_inproceeding("Test inproceeding", "Test author", 3, "Test url", db)
        inproceedings = reference.get_inproceedings(db)
        self.assertEqual(inproceedings[0], (1,"Test inproceeding", "Test author", 3, "Test url"))
        self.assertEqual(len(inproceedings), 1)
    
    
    def test_delete_book(self):
        reference.delete_book(1, db)
        books = reference.get_books(db)
        self.assertEqual(books, [])
    

    def test_delete_article(self):
        reference.delete_article(1, db)
        articles = reference.get_articles(db)
        self.assertEqual(articles, [])


    def test_delete_inproceeding(self):
        reference.delete_inproceeding(1, db)
        inproceedings = reference.get_inproceedings(db)
        self.assertEqual(inproceedings, [])
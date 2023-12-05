import unittest
import reference
from db import db
import app

class TestReference(unittest.TestCase):
    def setUp(self):
        reference.initialize_test_database(db)
        reference.add_book("Test book", "Test author", 1, "Test publisher", "test url", db)
        reference.add_article("Test article", "Test author", 2, "Test journal", "Test url", db)
        reference.add_inproceeding("Test inproceeding", "Test author", 3, "Test url", db)
        

    def test_get_books(self):
        books = reference.get_books(db)
        self.assertEqual(books[0], (1, "Test book","Test author", 1, "Test publisher", "test url"))
        self.assertEqual(len(books), 1)


    def test_get_articles(self):
        articles = reference.get_articles(db)
        self.assertEqual(articles[0], (1,"Test article", "Test author", 2, "Test journal", "Test url"))
        self.assertEqual(len(articles), 1)
    

    def test_get_inproceedings(self):
        inproceedings = reference.get_inproceedings(db)
        self.assertEqual(inproceedings[0], (1,"Test inproceeding", "Test author", 3, "Test url"))
        self.assertEqual(len(inproceedings), 1)
    
    
    def test_delete_book(self):
        self.assertEqual(len(
            reference.get_books(db)), 1)
        reference.delete_book(1, db)
        self.assertEqual(
            reference.get_books(db), [])
    

    def test_delete_article(self):
        self.assertEqual(len(
            reference.get_articles(db)), 1)
        reference.delete_article(1, db)
        self.assertEqual(
            reference.get_articles(db), [])


    def test_delete_inproceeding(self):
        self.assertEqual(len(
            reference.get_inproceedings(db)), 1)
        reference.delete_inproceeding(1, db)
        self.assertEqual(
            reference.get_inproceedings(db), [])
    
    def test_get_data(self):
        test_result = reference.get_data(db)
        self.assertEqual(len(test_result), 3)

'''
    def test_template_book(self):
        books = reference.get_books(db)
        book_result = reference.template_books(books[0])
        self.assertEqual(book_result, 
            '@book{Test book1,- title = "Test book",- author = "Test author",year = 1,publisher = "Test publisher",url = "test url",\n}\n\n')
'''
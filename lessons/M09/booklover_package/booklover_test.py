import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def setUp(self):
        """Set up a BookLover instance for testing."""
        self.book_lover = BookLover("Alice", "alice@example.com", "Fiction")
    
    def test_add_book(self):
        """Test adding a book and checking if it exists."""
        self.book_lover.add_book("The Great Gatsby", 5)
        self.assertTrue(self.book_lover.has_read("The Great Gatsby"))
    
    def test_has_read(self):
        """Test checking if a book has been read."""
        self.book_lover.add_book("1984", 4)
        self.assertTrue(self.book_lover.has_read("1984"))
        self.assertFalse(self.book_lover.has_read("Moby Dick"))
    
    def test_num_books_read(self):
        """Test counting the number of books read."""
        self.book_lover.add_book("To Kill a Mockingbird", 5)
        self.book_lover.add_book("Brave New World", 4)
        self.assertEqual(self.book_lover.num_books_read(), 2)
    
    def test_fav_books(self):
        """Test getting favorite books with a rating of 4 or higher."""
        self.book_lover.add_book("The Catcher in the Rye", 4)
        self.book_lover.add_book("Lord of the Flies", 5)
        self.book_lover.add_book("The Road", 3)
        favs = self.book_lover.fav_books()
        self.assertEqual(len(favs), 2)
    
    def test_no_duplicate_books(self):
        """Test that duplicate books are not added."""
        self.book_lover.add_book("The Hobbit", 5)
        self.book_lover.add_book("The Hobbit", 5)  # Should not add a second time
        self.assertEqual(self.book_lover.num_books_read(), 1)

if __name__ == "__main__":
    with open("booklover_results.txt", "w") as f:
        runner = unittest.TextTestRunner(f, verbosity=2)
        unittest.main(testRunner=runner)

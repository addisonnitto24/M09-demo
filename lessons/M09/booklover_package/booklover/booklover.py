import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=None):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list if book_list is not None else pd.DataFrame({'book_name': [], 'book_rating': []})

    def add_book(self, book_name, rating):
        """ Adds a book to the book list if it is not already present. """
        if book_name in self.book_list['book_name'].tolist():  # Convert to list before checking
            print(f"'{book_name}' is already in the book list.")
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1

    def has_read(self, book_name):
        """ Checks if the book has been read. """
        return book_name in self.book_list['book_name'].values

    def num_books_read(self):
        """ Returns the total number of books read. """
        return len(self.book_list)

    def fav_books(self):
        """ Returns a list of books with a rating of 4 or higher. """
        return self.book_list[self.book_list['book_rating'] >= 4]

    
# Part 1: Create an empty dictionary for the book inventory
inventory = {}

# Example of adding a book to the inventory
def add_book(isbn, title, author, price, genres):
    inventory[isbn] = (title, author, price, genres)

# Adding some example books
add_book("978-3-16-148410-0", "The Great Gatsby", "F. Scott Fitzgerald", 10.99, {'classic', 'novel'})
add_book("978-1-56619-909-4", "To Kill a Mockingbird", "Harper Lee", 7.99, {'classic', 'drama'})
add_book("978-0-7432-7356-5", "1984", "George Orwell", 8.99, {'dystopian', 'political'})
# Part 3: Function to update the price of a book
def update_price(isbn, new_price):
    if isbn in inventory:
        title, author, _, genres = inventory[isbn]  # Unpack the existing details
        # Create a new tuple with the updated price
        inventory[isbn] = (title, author, new_price, genres)
        return True  # Indicate that the update was successful
    else:
        return False  # Indicate that the ISBN was not found

# Example usage
print(update_price("978-3-16-148410-0", 12.99))  # Should update the price of "The Great Gatsby"
print(inventory["978-3-16-148410-0"])  # Check the updated details
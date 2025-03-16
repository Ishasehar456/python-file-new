# Part 2: Function to search books by author
def search_by_author(author):
    results = []
    for isbn, details in inventory.items():
        title, book_author, price, genres = details
        if book_author.lower() == author.lower():  # Case insensitive search
            results.append((isbn, title))
    return results

# Example usage
print(search_by_author("Harper Lee"))  # Should return the ISBN and title of "To Kill a Mockingbird"
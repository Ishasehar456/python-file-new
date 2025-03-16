# Part 4: Function to standardize book genres
def standardize_genres():
    for isbn, details in inventory.items():
        title, author, price, genres = details
        # Clean up genres: convert to lowercase and trim spaces
        cleaned_genres = {genre.strip().lower() for genre in genres}
        # Update the inventory with the cleaned genres
        inventory[isbn] = (title, author, price, cleaned_genres)

# Example usage
standardize_genres()
print(inventory)  # Check the updated genres
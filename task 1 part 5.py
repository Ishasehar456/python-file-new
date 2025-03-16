# Part 5: Function to display the inventory
def display_inventory():
    print(f"{'ISBN':<25} {'Title':<30} {'Author':<25} {'Price':<10} {'Genres'}")
    print("=" * 100)
    for isbn, details in inventory.items():
        title, author, price, genres = details
        genres_str = ', '.join(genres)  # Convert the set of genres to a string
        print(f"{isbn:<25} {title:<30} {author:<25} {price:<10} {genres_str}")

# Example usage
display_inventory()
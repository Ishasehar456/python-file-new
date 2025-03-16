# Part 6: Function to list all book titles
def list_all_books():
    titles = [details[0] for details in inventory.values()]  # Extract titles from the inventory
    return sorted(titles)  # Return the sorted list of titles

# Example usage
print(list_all_books())  # Should print a sorted list of all book titles
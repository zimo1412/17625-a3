from typing import List
import inventory_client


def get_book_titles(
    client: inventory_client.InventoryClient, 
    ISBNs: List[str]
) -> List[str]:
    """Get the titles of the books by ISBNs.
    
    Args:
        client: The inventory client.
        ISBNs: The list of ISBNs.
        
    Returns:
        The list of titles. If a book is not found, the title is None.
    """
    titles = []
    for ISBN in ISBNs:
        book = client.get_book(ISBN)
        titles.append(book.title if book else None)
    return titles


if __name__ == "__main__":
    client = inventory_client.InventoryClient()
    ISBNs = ["1234", "5678", "999"]
    titles = get_book_titles(client, ISBNs)
    print(titles)

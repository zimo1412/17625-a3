import unittest
from unittest.mock import MagicMock

import inventory_client
from get_book_titles import get_book_titles


mock_client = MagicMock()
mock_client.get_book.side_effect = [
    MagicMock(title="Book 1"),
    MagicMock(title="Book 2"),
    None,
]
ISBNs = ["1234", "5678", "999"]
expected_titles = [
    "Book 1",
    "Book 2",
    None,
]


class TestGetBookTitles(unittest.TestCase):

    def test_get_book_titles_mock_client(self, mock_client=mock_client):
        titles = get_book_titles(mock_client, ISBNs)
        self.assertEqual(titles, expected_titles)
    
    def test_get_book_titles_live_server(self):
        client = inventory_client.InventoryClient()
        titles = get_book_titles(client, ISBNs)
        self.assertEqual(titles, expected_titles)

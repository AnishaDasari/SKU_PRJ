"""
Unit Tests for Main Script and Utility Functions

This module contains unit tests for the main script and utility functions used in the SKU API project.

Classes:
    - TestMainScript: Unit tests for the main script.
    - TestUtils: Unit tests for utility functions.
"""

import json
import unittest
from unittest.mock import patch
from src.main import main
from src.utils import filter_records, count_records, save_to_file


class TestMainScript(unittest.TestCase):
    """
    Unit tests for the main script.
    """

    @patch('main.get_all_skus')
    def test_main_script(self, mock_get_all_skus):
        """
        Test the main script function.

        Mocks the API response and datetime to test the main script's functionality.
        """
        # Mock API response
        mock_get_all_skus.return_value = [
            {"sku": "berliner", "description": "Jelly donut", "price": "2.99", "createdAt": 1609459200},  # Jan 1, 2021
            {"sku": "croissant", "description": "Butter croissant", "price": "1.99", "createdAt": 1640995200},
            # Jan 1, 2022
            {"sku": "baguette", "description": "French baguette", "price": "3.49", "createdAt": 1662531200}
            # Jan 1, 2023
        ]

        # Mock datetime
        with patch('main.datetime') as mock_datetime:
            mock_datetime.return_value.timestamp.return_value = 1640995200  # Jan 1, 2022
            # Call main function
            main()

        # Assert that the count is correct
        self.assertEqual(mock_get_all_skus.call_count, 1)


class TestUtils(unittest.TestCase):
    """
    Unit tests for utility functions.
    """

    def test_filter_records(self):
        """
        Test the filter_records utility function.
        """
        records = [
            {"sku": "berliner", "description": "Jelly donut", "price": "2.99", "createdAt": 1609459200},  # Jan 1, 2021
            {"sku": "croissant", "description": "Butter croissant", "price": "1.99", "createdAt": 1640995200},
            # Jan 1, 2022
            {"sku": "baguette", "description": "French baguette", "price": "3.49", "createdAt": 1662531200}
            # Jan 1, 2023
        ]
        date_threshold = 1640995200  # Jan 1, 2022

        filtered_records = filter_records(records, date_threshold)

        self.assertEqual(len(filtered_records), 2)
        self.assertIn(records[1], filtered_records)
        self.assertIn(records[2], filtered_records)

    def test_count_records(self):
        """
        Test the count_records utility function.
        """
        records = [
            {"sku": "berliner", "description": "Jelly donut", "price": "2.99", "createdAt": 1609459200},
            {"sku": "croissant", "description": "Butter croissant", "price": "1.99", "createdAt": 1640995200},
            {"sku": "baguette", "description": "French baguette", "price": "3.49", "createdAt": 1662531200}
        ]

        count = count_records(records)

        self.assertEqual(count, 3)

    def test_save_to_file(self):
        """
        Test the save_to_file utility function.
        """
        records = [
            {"sku": "berliner", "description": "Jelly donut", "price": "2.99", "createdAt": 1609459200},
            {"sku": "croissant", "description": "Butter croissant", "price": "1.99", "createdAt": 1640995200}
        ]
        filename = 'test_records.json'

        save_to_file(records, filename)

        with open(filename, 'r') as file:
            saved_records = json.load(file)

        self.assertEqual(records, saved_records)


if __name__ == '__main__':
    unittest.main()

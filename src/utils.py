"""
Utils Script for SKU API CRUD Operations

This script contains utility functions for performing operations on SKU records,
including filtering, counting, and saving records to a file.

Functions:
    - filter_records(records, date_threshold): Filter records based on the createdAt field.
    - count_records(records): Count the number of records.
    - save_to_file(records, filename): Save records to a JSON file.
"""

import json

def filter_records(records, date_threshold):
    """
    Filter records based on the createdAt field.

    Args:
        records (list): List of records to filter.
        date_threshold (float): Unix timestamp representing the minimum date threshold.

    Returns:
        list: Filtered records created on or after the date threshold.
    """
    try:
        # Filter records based on the createdAt field
        filtered_records = [record for record in records if float(record['createdAt']) >= date_threshold]
        return filtered_records
    except (KeyError, ValueError) as e:
        # Handle exceptions if the createdAt field is missing or not a valid float
        print(f"Error filtering records: {e}")
        return []

def count_records(records):
    """
    Count the number of records.

    Args:
        records (list): List of records to count.

    Returns:
        int: Number of records.
    """
    return len(records)

def save_to_file(records, filename):
    """
    Save records to a JSON file.

    Args:
        records (list): List of records to save.
        filename (str): Name of the file to save records to.
    """
    try:
        # Save records to a JSON file
        with open(filename, 'w') as file:
            json.dump(records, file, indent=4)
        print(f"Records saved to {filename} successfully!")
    except Exception as e:
        # Handle exceptions if there's an error while saving records to the file
        print(f"Error saving records to {filename}: {e}")

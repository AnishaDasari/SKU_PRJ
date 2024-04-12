"""
API Client for SKU CRUD Operations

This module provides functions to interact with the SKU API for performing CRUD operations
such as creating, reading, updating, and deleting SKUs.

Functions:
    - get_all_skus(): Retrieve all SKUs from the API.
    - get_sku_by_id(sku_id): Retrieve a specific SKU by its ID from the API.
    - create_sku(sku_data): Create a new SKU using the provided data via the API.
    - update_sku(sku_id, sku_data): Update a specific SKU by its ID using the provided data via the API.
    - delete_sku(sku_id): Delete a specific SKU by its ID from the API.
"""

import requests

# API Endpoint
BASE_URL = "https://1ryu4whyek.execute-api.us-west-2.amazonaws.com/dev/skus"


def get_all_skus():
    """
    Retrieve all SKUs from the API.

    Returns:
        list: List of all SKUs retrieved from the API.
    """
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to get SKUs:", response.text)
            return None
    except requests.exceptions.RequestException as e:
        print("Error getting SKUs:", e)
        return None


def get_sku_by_id(sku_id):
    """
    Retrieve a specific SKU by its ID from the API.

    Args:
        sku_id (str): ID of the SKU to retrieve.

    Returns:
        dict: Retrieved SKU data.
    """
    try:
        url = f"{BASE_URL}/{sku_id}"
        response = requests.get(url)
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Failed to get SKU with ID {sku_id}:", response.text)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error getting SKU with ID {sku_id}:", e)
        return None


def create_sku(sku_data):
    """
    Create a new SKU using the provided data via the API.

    Args:
        sku_data (dict): Data of the SKU to create.

    Returns:
        dict: Created SKU data.
    """
    try:
        response = requests.post(BASE_URL, json=sku_data)
        response.raise_for_status()
        if response.status_code == 201:
            print("SKU created successfully!")
            return response.json()
        else:
            print("Failed to create SKU:", response.text)
            return None
    except requests.exceptions.RequestException as e:
        print("Error creating SKU:", e)
        return None


def update_sku(sku_id, sku_data):
    """
    Update a specific SKU by its ID using the provided data via the API.

    Args:
        sku_id (str): ID of the SKU to update.
        sku_data (dict): Updated data of the SKU.

    Returns:
        dict: Updated SKU data.
    """
    try:
        url = f"{BASE_URL}/{sku_id}"
        response = requests.put(url, json=sku_data)
        response.raise_for_status()
        if response.status_code == 200:
            print("SKU updated successfully!")
            return response.json()
        else:
            print(f"Failed to update SKU with ID {sku_id}:", response.text)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error updating SKU with ID {sku_id}:", e)
        return None


def delete_sku(sku_id):
    """
    Delete a specific SKU by its ID from the API.

    Args:
        sku_id (str): ID of the SKU to delete.
    """
    try:
        url = f"{BASE_URL}/{sku_id}"
        response = requests.delete(url)
        response.raise_for_status()
        if response.status_code == 204:
            print("SKU deleted successfully!")
        else:
            print(f"Failed to delete SKU with ID {sku_id}:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error deleting SKU with ID {sku_id}:", e)
